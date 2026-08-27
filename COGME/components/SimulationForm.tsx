"use client";

import { useEffect, useMemo, useState } from "react";
import { calculateSimulation, regimeLabels, type Regime, type SimulationResult } from "@/lib/simulation";

const money = new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" });
const foreignMoney = (currency: "USD" | "EUR", value: number) => new Intl.NumberFormat("en-US", { style: "currency", currency }).format(value);

export default function SimulationForm() {
  const [currency, setCurrency] = useState<"USD" | "EUR">("USD");
  const [regime, setRegime] = useState<Regime>("month");
  const [unitRate, setUnitRate] = useState(3500);
  const [exchangeRate, setExchangeRate] = useState(5.42);
  const [spread, setSpread] = useState(1.5);
  const [iof, setIof] = useState(0.38);
  const [otherFees, setOtherFees] = useState(0);
  const [quoteSource, setQuoteSource] = useState("cotação inicial");
  const [loadingQuote, setLoadingQuote] = useState(false);
  const [saved, setSaved] = useState(false);
  const [saving, setSaving] = useState(false);
  const [saveError, setSaveError] = useState(false);

  const result = useMemo<SimulationResult>(() => calculateSimulation({
    currency,
    regime,
    unitRate: Number(unitRate) || 0,
    exchangeRate: Number(exchangeRate) || 0,
    spread: Number(spread) || 0,
    iof: Number(iof) || 0,
    otherFees: Number(otherFees) || 0,
  }), [currency, regime, unitRate, exchangeRate, spread, iof, otherFees]);
  const comparisons = useMemo(() => (Object.keys(regimeLabels) as Regime[]).map((comparisonRegime) => calculateSimulation({
    currency,
    regime: comparisonRegime,
    unitRate: Number(unitRate) || 0,
    exchangeRate: Number(exchangeRate) || 0,
    spread: Number(spread) || 0,
    iof: Number(iof) || 0,
    otherFees: Number(otherFees) || 0,
  })), [currency, unitRate, exchangeRate, spread, iof, otherFees]);

  useEffect(() => { void loadQuote(currency); }, [currency]);

  async function loadQuote(selectedCurrency: "USD" | "EUR") {
    setLoadingQuote(true);
    try {
      const response = await fetch("/api/quote?currency=" + selectedCurrency);
      const data = (await response.json()) as { rate?: number; source?: string };
      if (data.rate) {
        setExchangeRate(data.rate);
        setQuoteSource(data.source || "cotação atualizada");
      }
    } finally {
      setLoadingQuote(false);
    }
  }

  async function saveSimulation() {
    setSaving(true);
    setSaveError(false);
    try {
      const response = await fetch("/api/simulations", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          currency: result.currency,
          regime: result.regime,
          unitRate: result.unitRate,
          exchangeRate: result.exchangeRate,
          spread: result.spread,
          iof: result.iof,
          otherFees: result.otherFees,
        }),
      });
      if (!response.ok) throw new Error("Falha ao salvar");
      setSaved(true);
      window.setTimeout(() => setSaved(false), 2500);
      return true;
    } catch {
      setSaveError(true);
      return false;
    } finally {
      setSaving(false);
    }
  }

  async function exportInvoice() {
    if (await saveSimulation()) window.setTimeout(() => { window.location.href = "/invoices"; }, 200);
  }

  const unitHelp = regime === "month" ? "O cálculo considera 1 mês." : regime === "hour" ? "O cálculo considera 176 horas/mês." : regime === "day" ? "O cálculo considera 22 dias/mês." : regime === "week" ? "O cálculo considera 4,33 semanas/mês." : "Valor único, sem recorrência.";

  return <>
  <div className="calculator-layout">
    <section className="surface-card calculator-card">
      <h2>Configure sua simulação</h2>
      <p className="subtle">Os campos abaixo são usados apenas no seu navegador nesta primeira etapa.</p>
      <div className="form-grid">
        <div className="field"><label htmlFor="currency">Moeda de recebimento</label><select id="currency" value={currency} onChange={(event) => setCurrency(event.target.value as "USD" | "EUR")}><option value="USD">Dólar americano (USD)</option><option value="EUR">Euro (EUR)</option></select></div>
        <div className="field"><label htmlFor="regime">Regime de contratação</label><select id="regime" value={regime} onChange={(event) => setRegime(event.target.value as Regime)}>{Object.entries(regimeLabels).map(([value, label]) => <option value={value} key={value}>{label}</option>)}</select></div>
        <div className="field"><label htmlFor="unitRate">Valor {regime === "fixed" ? "do contrato" : "por unidade"} ({currency})</label><input id="unitRate" type="number" min="0" step="0.01" value={unitRate} onChange={(event) => setUnitRate(Number(event.target.value))} /><span className="helper">{unitHelp}</span></div>
        <div className="field"><label htmlFor="exchangeRate">Cotação {currency} → BRL</label><input id="exchangeRate" type="number" min="0" step="0.0001" value={exchangeRate} onChange={(event) => setExchangeRate(Number(event.target.value))} /><span className="source-badge">{loadingQuote ? "Atualizando..." : quoteSource}</span></div>
        <div className="field"><label htmlFor="spread">Spread da operação (%)</label><input id="spread" type="number" min="0" step="0.01" value={spread} onChange={(event) => setSpread(Number(event.target.value))} /></div>
        <div className="field"><label htmlFor="iof">IOF simulado (%)</label><input id="iof" type="number" min="0" step="0.01" value={iof} onChange={(event) => setIof(Number(event.target.value))} /></div>
        <div className="field full"><label htmlFor="otherFees">Outros encargos (%)</label><input id="otherFees" type="number" min="0" step="0.01" value={otherFees} onChange={(event) => setOtherFees(Number(event.target.value))} /><span className="helper">Os encargos são estimativas para comparação e não constituem orientação tributária.</span></div>
      </div>
      <div className="quote-status"><span>⟳ Cotação consultada em tempo real quando disponível</span><button className="secondary-button" type="button" onClick={() => void loadQuote(currency)}>Atualizar</button></div>
    </section>
    <section className="surface-card results-card">
      <h2>Resultado estimado</h2>
      <p className="subtle">Uma visão clara do valor bruto, encargos e ganho líquido.</p>
      <div className="result-main"><small>Ganho líquido mensal</small><strong>{money.format(result.netBRL)}</strong></div>
      <div className="result-row"><span>Recebimento</span><strong>{foreignMoney(currency, result.foreignAmount)}</strong></div>
      <div className="result-row"><span>Valor bruto em BRL</span><strong>{money.format(result.grossBRL)}</strong></div>
      <div className="result-row"><span>Encargos simulados</span><strong>- {money.format(result.feesBRL)}</strong></div>
      <div className="result-row"><span>Cotação efetiva líquida</span><strong>{money.format(result.effectiveRate)}</strong></div>
      <div className="button-row"><button className="secondary-button full-button" type="button" onClick={() => void saveSimulation()} disabled={saving}>{saving ? "Salvando..." : saved ? "✓ Salvo" : "Salvar simulação"}</button><button className="primary-button full-button" type="button" onClick={() => void exportInvoice()} disabled={saving}>Gerar invoice</button></div>
      {saveError && <span className="helper save-error">Não foi possível salvar. Verifique a conexão com o banco.</span>}
    </section>
  </div>
  <section className="surface-card comparison-card">
    <h2>Compare os regimes</h2>
    <p className="subtle">Veja como o mesmo valor unitário se comporta em cada frequência de contratação.</p>
    <table className="comparison-table"><thead><tr><th>Regime</th><th>Volume mensal</th><th>Ganho líquido estimado</th></tr></thead><tbody>{comparisons.map((comparison) => <tr className={comparison.regime === regime ? "current" : ""} key={comparison.regime}><td>{regimeLabels[comparison.regime]} {comparison.regime === regime ? "· atual" : ""}</td><td>{comparison.quantity.toLocaleString("pt-BR")}</td><td>{money.format(comparison.netBRL)}</td></tr>)}</tbody></table>
  </section>
  </>;
}
