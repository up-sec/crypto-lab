# crypto-lab

Hands-on applied cryptography labs, built from scratch to understand how the algorithms work internally, not just how to call a library.

Part of my training path toward applied cryptography, PKI and post-quantum cryptography (PQC) for financial infrastructure.

## Labs

| # | Lab | Status |
|---|-----|--------|
| 01 | [DES key schedule](01-des-key-schedule/): generating the 16 round subkeys (PC-1, rotations, PC-2) in Python | Complete |
| 02 | [AES modes: ECB vs CBC](02-aes-modes/): encrypting an image to show how ECB leaks patterns and why CBC needs a random IV | Complete |
| 03 | [AES-GCM](03-aes-gcm/): authenticated encryption (AEAD); a single flipped bit is detected and rejected (`InvalidTag`) | Complete |
| 04 | [AES with OpenSSL](04-aes-openssl/): file encryption with AES-256-CBC + PBKDF2 (600k iterations); why `openssl enc` lacks integrity | Complete |

## Roadmap

- Hashing and HMAC
- RSA and elliptic curve cryptography
- Digital signatures
- PKI with OpenSSL
- Post-quantum cryptography: ML-KEM, ML-DSA, SLH-DSA

## Disclaimer

These are educational implementations. Never use them to protect real data; production systems must use vetted, audited cryptographic libraries.

## Environment

Ubuntu on WSL2 (previously Parrot OS) · Python 3 · OpenSSL 3.0 · Git

## Key takeaways

- **The mode matters as much as the algorithm**: AES-256 in ECB still leaks the shape of the data.
- **IV / nonce**: not secret, but must never repeat with the same key. Nonce reuse in GCM breaks both confidentiality and authenticity.
- **Encryption ≠ integrity**: CBC alone is malleable (bit flipping). Use AEAD (AES-GCM) or encrypt-then-MAC.
