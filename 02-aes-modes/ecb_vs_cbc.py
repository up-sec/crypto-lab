import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

ANCHO, ALTO = 256, 256


def crear_imagen():
    # Dibuja una imagen simple: fondo blanco, círculo oscuro y franja roja
    pixeles = bytearray()
    for y in range(ALTO):
        for x in range(ANCHO):
            if 40 <= y < 70:
                pixeles += bytes([0, 0, 200])        # rojo (BMP guarda BGR)
            elif (x - 128) ** 2 + (y - 128) ** 2 < 90 ** 2:
                pixeles += bytes([30, 30, 30])       # casi negro
            else:
                pixeles += bytes([255, 255, 255])    # blanco
    return bytes(pixeles)


def encabezado_bmp():
    # Los primeros 54 bytes le dicen al visor cómo leer la imagen.
    # NO se cifran: así el visor puede mostrar los pixeles cifrados.
    tam = ANCHO * ALTO * 3
    return (b"BM" + (54 + tam).to_bytes(4, "little") + b"\x00" * 4
            + (54).to_bytes(4, "little") + (40).to_bytes(4, "little")
            + ANCHO.to_bytes(4, "little") + ALTO.to_bytes(4, "little")
            + (1).to_bytes(2, "little") + (24).to_bytes(2, "little")
            + b"\x00" * 4 + tam.to_bytes(4, "little") + b"\x00" * 16)


def cifrar(datos, modo):
    cifrador = Cipher(algorithms.AES(LLAVE), modo).encryptor()
    return cifrador.update(datos) + cifrador.finalize()


LLAVE = os.urandom(32)          # 32 bytes aleatorios = AES-256
original = crear_imagen()
cabecera = encabezado_bmp()

with open("original.bmp", "wb") as f:
    f.write(cabecera + original)
with open("ecb.bmp", "wb") as f:
    f.write(cabecera + cifrar(original, modes.ECB()))
with open("cbc.bmp", "wb") as f:
    f.write(cabecera + cifrar(original, modes.CBC(os.urandom(16))))

print("Listo: original.bmp, ecb.bmp y cbc.bmp")
