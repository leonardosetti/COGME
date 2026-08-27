const encoder = new TextEncoder();

export const SESSION_COOKIE = "cogme_session";
const SESSION_TTL_SECONDS = 60 * 60 * 8;
const PBKDF2_ITERATIONS = 120000;
const DEMO_HASH =
  "pbkdf2$sha256$120000$Y29nbWUtc2FsdC12MQ$Cm6JgDOZRiGBEY8Ddt4NicWRJ8EbrGJ_WQIBMr0iaIs";

export type Session = {
  sub: string;
  email: string;
  name: string;
  exp: number;
};

function toBase64Url(bytes: Uint8Array) {
  let binary = "";
  bytes.forEach((byte) => (binary += String.fromCharCode(byte)));
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

function fromBase64Url(value: string) {
  const padded = value.replace(/-/g, "+").replace(/_/g, "/").padEnd(Math.ceil(value.length / 4) * 4, "=");
  const binary = atob(padded);
  return Uint8Array.from(binary, (char) => char.charCodeAt(0));
}

function getAuthSecret() {
  const secret = process.env.AUTH_SECRET || "development-only-change-this-secret";
  if (process.env.NODE_ENV === "production" && secret === "development-only-change-this-secret") {
    throw new Error("AUTH_SECRET precisa ser definido em produção.");
  }
  return secret;
}

export async function hashPassword(password: string, salt = "cogme-salt-v1") {
  const key = await crypto.subtle.importKey("raw", encoder.encode(password), "PBKDF2", false, ["deriveBits"]);
  const bits = await crypto.subtle.deriveBits(
    { name: "PBKDF2", salt: encoder.encode(salt), iterations: PBKDF2_ITERATIONS, hash: "SHA-256" },
    key,
    256,
  );
  return "pbkdf2$sha256$" + PBKDF2_ITERATIONS + "$" + toBase64Url(encoder.encode(salt)) + "$" + toBase64Url(new Uint8Array(bits));
}

export async function verifyPassword(password: string, encodedHash: string) {
  const [algorithm, digest, iterations, encodedSalt, expected] = encodedHash.split("$");
  if (algorithm !== "pbkdf2" || digest !== "sha256" || !iterations || !encodedSalt || !expected) return false;

  const salt = new TextDecoder().decode(fromBase64Url(encodedSalt));
  const key = await crypto.subtle.importKey("raw", encoder.encode(password), "PBKDF2", false, ["deriveBits"]);
  const bits = await crypto.subtle.deriveBits(
    { name: "PBKDF2", salt: encoder.encode(salt), iterations: Number(iterations), hash: "SHA-256" },
    key,
    256,
  );
  const actual = toBase64Url(new Uint8Array(bits));
  if (actual.length !== expected.length) return false;
  let difference = 0;
  for (let index = 0; index < actual.length; index += 1) difference |= actual.charCodeAt(index) ^ expected.charCodeAt(index);
  return difference === 0;
}

async function sign(value: string) {
  const key = await crypto.subtle.importKey("raw", encoder.encode(getAuthSecret()), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  return toBase64Url(new Uint8Array(await crypto.subtle.sign("HMAC", key, encoder.encode(value))));
}

export async function createSessionToken(session: Omit<Session, "exp">) {
  const payload: Session = { ...session, exp: Math.floor(Date.now() / 1000) + SESSION_TTL_SECONDS };
  const encodedPayload = toBase64Url(encoder.encode(JSON.stringify(payload)));
  return encodedPayload + "." + (await sign(encodedPayload));
}

export async function verifySessionToken(token: string): Promise<Session | null> {
  try {
    const [encodedPayload, providedSignature] = token.split(".");
    if (!encodedPayload || !providedSignature) return null;
    const expectedSignature = await sign(encodedPayload);
    if (expectedSignature.length !== providedSignature.length) return null;
    let difference = 0;
    for (let index = 0; index < expectedSignature.length; index += 1) {
      difference |= expectedSignature.charCodeAt(index) ^ providedSignature.charCodeAt(index);
    }
    if (difference !== 0) return null;
    const payload = JSON.parse(new TextDecoder().decode(fromBase64Url(encodedPayload))) as Session;
    return payload.exp > Math.floor(Date.now() / 1000) ? payload : null;
  } catch {
    return null;
  }
}

export function getConfiguredCredentials() {
  return {
    email: (process.env.ADMIN_EMAIL || "admin@cogme.local").toLowerCase(),
    passwordHash: process.env.ADMIN_PASSWORD_HASH || DEMO_HASH,
    name: process.env.ADMIN_NAME || "Administrador COGME",
  };
}

export const sessionCookieOptions = {
  httpOnly: true,
  sameSite: "lax" as const,
  secure: process.env.NODE_ENV === "production",
  path: "/",
  maxAge: SESSION_TTL_SECONDS,
};
