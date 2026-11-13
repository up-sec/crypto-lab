# Lab 05 — Hashing and HMAC

```bash
echo -n 'Transferencia: $500.00' | sha256sum   # deterministic: same input, same hash
echo -n 'Transferencia: $900.00' | sha256sum   # avalanche: one digit changes everything
sha256sum pago.txt > pago.sha256 && sha256sum -c pago.sha256   # integrity check
openssl dgst -sha256 -hmac "secret-key" pago.txt                 # HMAC: hash + secret key
```

## Takeaways
- A hash is one-way, fixed-size and deterministic, with an avalanche effect. It cannot be reversed, but predictable inputs can be guessed.
- A plain hash only detects accidental changes, or changes checked against a trusted hash. An attacker who can modify both the file and its hash just recomputes it (no key needed).
- HMAC adds a secret key: without the key nobody can produce a valid tag.
- HMAC uses a shared key, so it gives no non-repudiation. That requires digital signatures.
