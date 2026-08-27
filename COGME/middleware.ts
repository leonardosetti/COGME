import { NextRequest, NextResponse } from "next/server";
import { SESSION_COOKIE, verifySessionToken } from "@/lib/auth";

const protectedPaths = ["/dashboard", "/simulacoes", "/invoices", "/api/quote", "/api/news/update", "/api/simulations"];

function isProtectedPath(pathname: string) {
  return protectedPaths.some((path) => pathname === path || pathname.startsWith(path + "/"));
}

function isAuthorizedNewsJob(request: NextRequest) {
  const configuredSecret = process.env.NEWS_JOB_SECRET;
  return request.nextUrl.pathname === "/api/news/update" &&
    Boolean(configuredSecret) &&
    request.headers.get("authorization") === "Bearer " + configuredSecret;
}

export async function middleware(request: NextRequest) {
  const token = request.cookies.get(SESSION_COOKIE)?.value;
  const session = token ? await verifySessionToken(token) : null;

  if (isProtectedPath(request.nextUrl.pathname) && !session && !isAuthorizedNewsJob(request)) {
    if (request.nextUrl.pathname.startsWith("/api/")) {
      return NextResponse.json({ error: "Não autenticado." }, { status: 401 });
    }
    const loginUrl = new URL("/login", request.url);
    loginUrl.searchParams.set("next", request.nextUrl.pathname);
    return NextResponse.redirect(loginUrl);
  }

  if (request.nextUrl.pathname === "/login" && session) {
    return NextResponse.redirect(new URL("/dashboard", request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico).*)"],
};
