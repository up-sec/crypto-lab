import os
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

llave = AESGCM.generate_key(bit_length=256)   # AES-256
aes = AESGCM(llave)

mensaje = b"Transferencia: $500.00 a la cuenta 1234"
nonce = os.urandom(12)                        # 12 bytes, NUNCA se repite con la misma llave
cifrado = aes.encrypt(nonce, mensaje, None)   # incluye al final una etiqueta (tag) de 16 bytes

print("Original :", mensaje)
print("Cifrado  :", cifrado.hex())
print("Tamano   :", len(mensaje), "bytes ->", len(cifrado), "bytes (+16 de tag)")
print("Descifrado:", aes.decrypt(nonce, cifrado, None))

# Ataque: alguien cambia UN solo bit del mensaje cifrado en el camino
alterado = bytearray(cifrado)
alterado[0] ^= 0x01
try:
    aes.decrypt(nonce, bytes(alterado), None)
    print("Ataque   : el cambio NO se detecto")
except InvalidTag:
    print("Ataque   : DETECTADO -> InvalidTag, el mensaje fue alterado y se rechaza")
