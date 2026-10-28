"use client";

import { FormEvent, useEffect, useState } from "react";

export default function LoginPage() {
  const [next, setNext] = useState("/dashboard");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const requestedPath = new URLSearchParams(window.location.search).get("next");
    if (requestedPath?.startsWith("/")) setNext(requestedPath);
  }, []);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError("");
    setLoading(true);
    try {
      const response = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      const data = (await response.json()) as { error?: string };
      if (!response.ok) throw new Error(data.error || "Não foi possível entrar.");
      window.location.href = next;
    } catch (loginError) {
      setError(loginError instanceof Error ? loginError.message : "Não foi possível entrar.");
      setLoading(false);
    }
  }

  return <main className="login-page">
    <section className="login-brand">
      <div className="brand-mark"><span>C</span> COGME</div>
      <div>
        <div className="eyebrow">Conversão de ganhos em moeda estrangeira</div>
        <h1>Clareza para cada ganho internacional.</h1>
        <p>Simule sua remuneração em dólar ou euro, compare regimes e entenda o valor que chega ao seu bolso.</p>
      </div>
      <div className="brand-note">MVP acadêmico · FATEC Marlene Maria Miletta Servidoni</div>
    </section>
    <section className="login-panel">
      <div className="login-card">
        <div className="eyebrow">Acesso restrito</div>
        <h2>Entrar no COGME</h2>
        <p>Use suas credenciais para acessar suas simulações e invoices.</p>
        <form className="form-stack" onSubmit={handleSubmit}>
          <div className="field"><label htmlFor="email">E-mail</label><input id="email" type="email" value={email} onChange={(event) => setEmail(event.target.value)} required autoComplete="username" placeholder="voce@empresa.com" /></div>
          <div className="field"><label htmlFor="password">Senha</label><div className="password-wrap"><input id="password" type={showPassword ? "text" : "password"} value={password} onChange={(event) => setPassword(event.target.value)} required autoComplete="current-password" placeholder="Sua senha" /><button className="password-toggle" type="button" onClick={() => setShowPassword((visible) => !visible)}>{showPassword ? "Ocultar" : "Exibir"}</button></div></div>
          {error && <p className="error-message" role="alert">{error}</p>}
          <button className="primary-button" type="submit" disabled={loading}>{loading ? "Validando..." : "Entrar na plataforma"}</button>
        </form>
        <div className="demo-hint">Ambiente de demonstração: <strong>admin@cogme.local</strong> · senha <strong>COGME2026!</strong></div>
      </div>
    </section>
  </main>;
}
