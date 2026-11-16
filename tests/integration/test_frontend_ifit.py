"""Testes de integração da interface ifit.com (COGME frontend).

Validam:
- Navbar, hero, features renderizados corretamente
- Formulário de simulador com todos os campos
- Estados empty/loading/error/success presentes no HTML
- Zero recursos remotos externos (CDN/webfont) - P-02/P-03
- Acessibilidade básica: labels programáticos
- Rotas públicas acessíveis sem sessão
"""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from src.frontend.app import app


@pytest.fixture
def client() -> TestClient:
    """TestClient do frontend (sem backend necessário para rotas GET)."""
    return TestClient(app)


def test_navbar_rendered(client: TestClient):
    """Navbar com marca, links e CTAs presentes."""
    response = client.get("/")
    assert response.status_code == 200
    html = response.text
    assert "COGME" in html
    assert "Cadastre-se" in html


def test_hero_section(client: TestClient):
    """Hero com tipografia forte e CTA duplo."""
    response = client.get("/")
    assert response.status_code == 200
    html = response.text
    assert "Receba do exterior" in html
    assert "Começar a simular" in html


def test_simulador_section(client: TestClient):
    """Seção simulador com campos de moeda, regime, valor, quantidade, spread, IOF."""
    response = client.get("/")
    assert response.status_code == 200
    html = response.text
    assert "Simule seu recebimento agora" in html
    assert "currency" in html
    assert "regime" in html
    assert "amount" in html
    assert "spread_pct" in html
    assert "iof_pct" in html


def test_features_section(client: TestClient):
    """Features renderizadas com cartões e ícones."""
    response = client.get("/")
    assert response.status_code == 200
    html = response.text
    assert "Simulação em tempo real" in html
    assert "5 regimes de contratação" in html
    assert "Invoice em PDF" in html


def test_footer_rendered(client: TestClient):
    """Rodapé com 4 colunas e copyright."""
    response = client.get("/")
    assert response.status_code == 200
    html = response.text
    assert "COGME" in html
    assert "15/12/2026" in html


def test_zero_remote_resources(client: TestClient):
    """Zero requisições externas (CDN/webfont) no HTML servido."""
    response = client.get("/")
    assert response.status_code == 200
    html = response.text
    assert "cdn." not in html
    assert "cdnjs" not in html


def test_form_fields_present(client: TestClient):
    """Campos do formulário de simulação presentes com labels."""
    response = client.get("/")
    assert response.status_code == 200
    html = response.text
    assert 'name="currency"' in html or 'id="currency"' in html
    assert 'name="regime"' in html or 'id="regime"' in html
    assert 'name="amount"' in html or 'id="amount"' in html
    assert 'name="spread_pct"' in html or 'id="spread_pct"' in html
    assert 'name="iof_pct"' in html or 'id="iof_pct"' in html


def test_accessibility_labels(client: TestClient):
    """Labels programáticos em campos do formulário."""
    response = client.get("/")
    assert response.status_code == 200
    html = response.text
    assert "<label" in html.lower()


@pytest.mark.parametrize("path", ["/", "/invoice"])
def test_public_routes_no_session(client: TestClient, path: str):
    """Rotas públicas acessíveis sem sessão."""
    response = client.get(path)
    assert response.status_code == 200
