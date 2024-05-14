// src/components/Login.tsx
"use client"
import { signIn } from "next-auth/react";
export default function Login() {
  return <button onClick={() => signIn("keycloak")}>
    Signin with keycloak
  </button>
}
