import { NextResponse } from "next/server";
import { createSessionToken, getConfiguredCredentials, SESSION_COOKIE, sessionCookieOptions, verifyPassword } from "@/lib/auth";

export async function POST(request: Request) {
  try {
    const body = (await request.json()) as { email?: string; password?: string };
    const email = body.email?.trim().toLowerCase();
    const password = body.password || "";
    if (!email || !password) return NextResponse.json({ error: "Informe e-mail e senha." }, { status: 400 });

    const credentials = getConfiguredCredentials();
    const validEmail = email === credentials.email;
    const validPassword = await verifyPassword(password, credentials.passwordHash);
    if (!validEmail || !validPassword) return NextResponse.json({ error: "E-mail ou senha inválidos." }, { status: 401 });

    const token = await createSessionToken({ sub: credentials.email, email: credentials.email, name: credentials.name });
    const response = NextResponse.json({ ok: true });
    response.cookies.set(SESSION_COOKIE, token, sessionCookieOptions);
    return response;
  } catch {
    return NextResponse.json({ error: "Não foi possível processar o login." }, { status: 500 });
  }
}
