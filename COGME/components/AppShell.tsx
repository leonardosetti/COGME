"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import type { Session } from "@/lib/auth";

export default function AppShell({ children, session }: { children: React.ReactNode; session: Session }) {
  const pathname = usePathname();
  const links = [
    { href: "/dashboard", label: "Visão geral", icon: "⌂" },
    { href: "/simulacoes", label: "Nova simulação", icon: "＋" },
    { href: "/invoices", label: "Minhas invoices", icon: "▤" },
  ];
  async function logout() {
    await fetch("/api/auth/logout", { method: "POST" });
    window.location.href = "/login";
  }

  return <div className="app-shell">
    <aside className="sidebar">
      <div className="brand-mark"><span>C</span> COGME</div>
      <nav className="nav">{links.map((link) => <Link className={pathname === link.href ? "active" : ""} href={link.href} key={link.href}><span aria-hidden="true">{link.icon}</span> &nbsp;{link.label}</Link>)}</nav>
      <div className="sidebar-footer"><small>{session.email}</small><button className="logout-button" onClick={logout}>↪ &nbsp; Sair da conta</button></div>
    </aside>
    <main className="main-content">{children}</main>
  </div>;
}
