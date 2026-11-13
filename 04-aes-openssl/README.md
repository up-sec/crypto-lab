# Lab 04 — AES file encryption with OpenSSL

```bash
# Encrypt (password → 256-bit key with PBKDF2, 600,000 iterations, random salt)
openssl enc -aes-256-cbc -pbkdf2 -iter 600000 -salt -in secreto.txt -out secreto.enc

# The file starts with the readable header "Salted__" followed by the 8-byte salt
head -c 8 secreto.enc

# Decrypt
openssl enc -d -aes-256-cbc -pbkdf2 -iter 600000 -in secreto.enc
```

## What I observed

- Wrong password → `bad decrypt ... ossl_cipher_unpadblock`: OpenSSL cannot check the password,
  it only notices invalid **padding**, and it still prints garbage. Roughly 1 in 256 wrong
  passwords produce valid-looking padding and no error at all.
- `openssl enc` does not support GCM (`AEAD ciphers not supported`), so this file has
  **confidentiality only**: no integrity or authenticity. An attacker can flip bits without the key.
- In practice: use an AEAD tool (`age`, GPG, or AES-GCM like [lab 03](../03-aes-gcm/)),
  or add an HMAC (encrypt-then-MAC).

The plaintext `secreto.txt` is intentionally not committed (`.gitignore`).
