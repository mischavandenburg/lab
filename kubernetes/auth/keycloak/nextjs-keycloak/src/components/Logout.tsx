// src/components/Logout.tsx
"use client"
import { signOut } from "next-auth/react";
export default function Logout() {
  return <button onClick={() => signOut()}>
    Signout of keycloak
  </button>
}
