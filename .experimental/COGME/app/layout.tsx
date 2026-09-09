import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "COGME | Conversor de ganhos",
  description: "Simule seus ganhos internacionais em reais com transparência.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="pt-BR"><body>{children}</body></html>;
}
