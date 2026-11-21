"""Camada Front do COGME — serviço FastAPI com Jinja2 e proxy para o back.

Sirve os templates de interface (index, invoice_form) renderizados
server-side e encaminha /v1/* para o back:8000. Sem CORS: mesma origem.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from datetime import datetime
from decimal import Decimal
from pathlib import Path

from fastapi import FastAPI, Form, Request, Response
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
import httpx
from jinja2 import Environment, FileSystemLoader, select_autoescape


@asynccontextmanager
async def _lifespan(_app: FastAPI) -> AsyncIterator[None]:
    """Fecha o cliente HTTP do back no encerramento."""
    yield
    if _client is not None:
        await _client.aclose()


app = FastAPI(title="COGME Front", lifespan=_lifespan)
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).resolve().parent / "static"),
    name="static",
)


def _br_number(value: str, places: int) -> str:
    """Formata um decimal em pt-BR sem passar por float."""
    formatted = f"{Decimal(value):,.{places}f}"
    translation: dict[str, str | int | None] = {",": ".", ".": ",", " ": "."}
    return formatted.translate(str.maketrans(translation))


def _br_datetime(value: str) -> str:
    """Formata um instante UTC em pt-BR."""
    return datetime.fromisoformat(value.replace("Z", "+00:00")).strftime(
        "%d/%m/%Y, %H:%M:%S UTC"
    )


env = Environment(
    loader=FileSystemLoader(str(Path(__file__).resolve().parent / "templates")),
    autoescape=select_autoescape(["html", "xml"]),
    auto_reload=False,
)
env.filters["br_number"] = _br_number
env.filters["br_datetime"] = _br_datetime


def render(name: str, **context: object) -> HTMLResponse:
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


# --- rotas de interface ---

@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    """Tela de simulação."""
    return render("index.html", request=request)


@app.get("/invoice", response_class=HTMLResponse)
async def invoice_form(request: Request) -> HTMLResponse:
    """Tela de emissão de invoice. Aceita query params para pré-preencher simulação."""
    sim_data = None
    if request.query_params.get("currency"):
        sim_data = {
            "currency": request.query_params.get("currency"),
            "regime": request.query_params.get("regime"),
            "amount": request.query_params.get("amount"),
            "quantity": request.query_params.get("quantity"),
            "spread_pct": request.query_params.get("spread_pct"),
            "iof_pct": request.query_params.get("iof_pct"),
        }
    return render("invoice_form.html", request=request, sim=sim_data)


@app.get("/auth/login", response_class=HTMLResponse)
async def auth_login(request: Request) -> HTMLResponse:
    """Tela de login."""
    return render("auth/login.html", request=request)


@app.get("/auth/register", response_class=HTMLResponse)
async def auth_register(request: Request) -> HTMLResponse:
    """Tela de cadastro."""
    return render("auth/register.html", request=request)


@app.get("/auth/verify-email", response_class=HTMLResponse)
async def auth_verify_email(request: Request) -> HTMLResponse:
    """Tela de verificação de e-mail (token via query param)."""
    token = request.query_params.get("token", "")
    return render("auth/verify_email.html", request=request, token=token)


@app.get("/auth/reset", response_class=HTMLResponse)
async def auth_reset(request: Request) -> HTMLResponse:
    """Tela de redefinição de senha (token via query param)."""
    token = request.query_params.get("token", "")
    return render("auth/reset.html", request=request, token=token)


# --- rotas server-side (fluxo sem JS, R-INT-05) ---

def _normalize_decimal(value: str) -> str:
    """Converte separador decimal vírgula para ponto."""
    return value.replace(",", ".")


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
        "amount": _normalize_decimal(amount),
        "quantity": None if regime == "fixed" else _normalize_decimal(quantity) if quantity else None,
        "spread_pct": _normalize_decimal(spread_pct),
        "iof_pct": _normalize_decimal(iof_pct),
    }
    try:
        resp = await client.post("/v1/simulate", json=body)
    except httpx.RequestError:
        return HTMLResponse(
            env.get_template("index.html").render(
                request=request,
                error="Não foi possível conectar ao serviço de simulação. Tente novamente.",
                values=body,
            ),
            status_code=503,
        )

    if resp.status_code != 200:
        error = (
            "Cotação indisponível. Tente novamente."
            if resp.status_code == 503
            else "Erro na simulação. Tente novamente."
        )
        details: list[dict[str, str]] = []
        try:
            payload = resp.json()
        except ValueError:
            payload = {}
        if not isinstance(payload, dict):
            payload = {}
        error_payload = payload.get("error") or {}
        if not isinstance(error_payload, dict):
            error_payload = {}
        error = error_payload.get("message") or error
        raw_details = error_payload.get("details") or []
        details = raw_details if isinstance(raw_details, list) else []
        return HTMLResponse(
            env.get_template("index.html").render(
                request=request,
                error=error,
                details=details,
                values=body,
            ),
            status_code=resp.status_code,
        )
    data = resp.json()
    # values para o template usa o formato original (com vírgula) para reexibir no form
    display_values = {
        "currency": currency,
        "regime": regime,
        "amount": amount,
        "quantity": quantity,
        "spread_pct": spread_pct,
        "iof_pct": iof_pct,
    }
    return render("index.html", request=request, sim=data, values=display_values)


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
) -> Response:
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
            "content-disposition": resp.headers.get(
                "content-disposition", 'attachment; filename="invoice.pdf"'
            ),
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
    url = httpx.URL(BACK_BASE + "/v1/" + path)
    body = await request.body()
    headers = {k: v for k, v in request.headers.items() if k.lower() != "host"}
    resp = await client.request(
        method=request.method,
        url=url,
        params=request.query_params,
        content=body,
        headers=headers,
    )
    return StreamingResponse(
        resp.aiter_bytes(),
        status_code=resp.status_code,
        headers={
            k: v
            for k, v in resp.headers.items()
            if k.lower() not in ("content-length", "transfer-encoding")
        },
        media_type=resp.headers.get("content-type"),
    )
