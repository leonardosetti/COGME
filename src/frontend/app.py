"""Camada Front do COGME — serviço FastAPI com Jinja2 e proxy para o back.

Sirve os templates de interface (index, invoice_form) renderizados
server-side e encaminha /v1/* para o back:8000. Sem CORS: mesma origem.
"""

from __future__ import annotations

from decimal import Decimal
from typing import Any

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
import httpx
from jinja2 import Environment, FileSystemLoader, select_autoescape

app = FastAPI(title="COGME Front")
app.mount("/static", StaticFiles(directory="src/frontend/static"), name="static")

env = Environment(
    loader=FileSystemLoader("src/frontend/templates"),
    autoescape=select_autoescape(["html", "xml"]),
    auto_reload=False,
)


def render(name: str, **context) -> HTMLResponse:
    """Renderiza um template Jinja2 com ``request`` no contexto."""
    template = env.get_template(name)
    return HTMLResponse(template.render(**context))

BACK_BASE = "http://back:8000"

_client: httpx.AsyncClient | None = None


def _get_client() -> httpx.AsyncClient:
    global _client
    if _client is None:
        _client = httpx.AsyncClient(base_url=BACK_BASE, timeout=30.0)
    return _client


# --- filtros de formatação pt-BR (espelho dos do back, usados nos templates) ---

def _brl(value: Any) -> str:
    try:
        return "R$ " + format(Decimal(str(value)), ",.2f").replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return str(value)


def _percent_br(value: Any) -> str:
    try:
        return format(Decimal(str(value)), ".4f").replace(".", ",") + " %"
    except Exception:
        return str(value)


def _rate_br(value: Any) -> str:
    try:
        return format(Decimal(str(value)), ".6f").replace(".", ",") + " "
    except Exception:
        return str(value)


def _date_br(value: Any) -> str:
    return str(value)


def _datetime_br(value: Any) -> str:
    return str(value)


env.filters["brl"] = _brl
env.filters["percent_br"] = _percent_br
env.filters["rate_br"] = _rate_br
env.filters["date_br"] = _date_br
env.filters["datetime_br"] = _datetime_br


@app.on_event("shutdown")
async def _shutdown() -> None:
    global _client
    if _client is not None:
        await _client.aclose()
        _client = None


# --- rotas de interface ---

@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    """Tela de simulação."""
    return render("index.html", request=request)


@app.get("/invoice", response_class=HTMLResponse)
async def invoice_form(request: Request) -> HTMLResponse:
    """Tela de emissão de invoice."""
    return render("invoice_form.html", request=request)


# --- rotas server-side (fluxo sem JS, R-INT-05) ---

@app.post("/simulate", response_class=HTMLResponse)
async def simulate_server(
    request: Request,
    currency: str = Form(...),
    regime: str = Form(...),
    amount: str = Form(...),
    quantity: str | None = Form(None),
    spread_pct: str = Form(...),
    iof_pct: str = Form(...),
) -> HTMLResponse:
    """Recebe o formulário de simulação, chama o back e renderiza o resultado."""
    client = _get_client()
    body = {
        "currency": currency,
        "regime": regime,
        "amount": amount,
        "quantity": quantity,
        "spread_pct": spread_pct,
        "iof_pct": iof_pct,
    }
    resp = await client.post("/v1/simulate", json=body)
    if resp.status_code != 200:
        return HTMLResponse(
            env.get_template("index.html").render(
                request=request, error="Erro na simulação. Tente novamente."
            ),
            status_code=resp.status_code,
        )
    data = resp.json()
    return render("index.html", request=request, sim=data)


@app.post("/invoice", response_class=StreamingResponse)
async def invoice_server(
    request: Request,
    sim_currency: str = Form(..., alias="sim-currency"),
    sim_regime: str = Form(..., alias="sim-regime"),
    sim_amount: str = Form(..., alias="sim-amount"),
    sim_quantity: str | None = Form(None, alias="sim-quantity"),
    sim_spread_pct: str = Form(..., alias="sim-spread_pct"),
    sim_iof_pct: str = Form(..., alias="sim-iof_pct"),
    issuer_name: str = Form(..., alias="issuer-name"),
    issuer_tax_id: str | None = Form(None, alias="issuer-tax_id"),
    issuer_address: str | None = Form(None, alias="issuer-address"),
    client_name: str = Form(..., alias="client-name"),
    client_tax_id: str | None = Form(None, alias="client-tax_id"),
    client_address: str | None = Form(None, alias="client-address"),
    invoice_number: str = Form(...),
    issue_date: str = Form(...),
    description: str = Form(...),
) -> StreamingResponse:
    """Recebe o formulário de invoice, chama o back e devolve o PDF."""
    client = _get_client()
    body = {
        "simulation": {
            "currency": sim_currency,
            "regime": sim_regime,
            "amount": sim_amount,
            "quantity": sim_quantity,
            "spread_pct": sim_spread_pct,
            "iof_pct": sim_iof_pct,
        },
        "issuer": {
            "name": issuer_name,
            "tax_id": issuer_tax_id,
            "address": issuer_address,
        },
        "client": {
            "name": client_name,
            "tax_id": client_tax_id,
            "address": client_address,
        },
        "invoice_number": invoice_number,
        "issue_date": issue_date,
        "description": description,
    }
    resp = await client.post("/v1/invoice", json=body)
    if resp.status_code != 200:
        return HTMLResponse(
            env.get_template("invoice_form.html").render(
                request=request,
                error="Não foi possível gerar a invoice. Tente novamente.",
            ),
            status_code=resp.status_code,
        )
    return StreamingResponse(
        resp.aiter_bytes(),
        status_code=resp.status_code,
        headers={
            "content-type": resp.headers.get("content-type", "application/pdf"),
            "content-disposition": resp.headers.get("content-disposition", 'attachment; filename="invoice.pdf"'),
            "cache-control": "no-store",
        },
        media_type=resp.headers.get("content-type"),
    )


# --- proxy genérico /v1/* para o back (inter-camada de API) ---

@app.api_route(
    "/v1/{path:path}",
    methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"],
)
async def proxy_v1(path: str, request: Request) -> StreamingResponse:
    """Encaminha qualquer chamada /v1/* para o back:8000, preservando método,
    headers, query string e corpo. Arquitetura preparada para novos endpoints
    de inter-camada além do cálculo de câmbio (currency exchange)."""
    client = _get_client()
    url = httpx.URL(path=BACK_BASE + "/v1/" + path, params=request.url.params)
    body = await request.body()
    headers = {k: v for k, v in request.headers.items() if k.lower() != "host"}
    resp = await client.request(
        method=request.method,
        url=url,
        content=body,
        headers=headers,
    )
    return StreamingResponse(
        resp.aiter_bytes(),
        status_code=resp.status_code,
        headers={k: v for k, v in resp.headers.items() if k.lower() not in ("content-length", "transfer-encoding")},
        media_type=resp.headers.get("content-type"),
    )
