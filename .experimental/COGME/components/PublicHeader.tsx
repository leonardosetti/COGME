import Link from "next/link";

export default function PublicHeader({ active }: { active: "home" | "about" }) {
  return <header className="public-header">
    <Link className="brand-mark" href="/"><span>C</span> COGME</Link>
    <nav className="public-nav" aria-label="Navegação principal">
      <Link className={active === "home" ? "active" : ""} href="/">Home</Link>
      <Link className={active === "about" ? "active" : ""} href="/sobre">Sobre Nós</Link>
      <Link className="public-login-link" href="/login">Login</Link>
    </nav>
  </header>;
}
