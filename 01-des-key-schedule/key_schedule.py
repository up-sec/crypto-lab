def shift_normal(bits, n):
    return bits[n:] + "0" * n   

def rotar(bits, n):
    return bits[n:] + bits[:n]
      

ejemplo = "10110010"
print("Original:", ejemplo)
print("Shift   :", shift_normal(ejemplo, 1))
print("Rotación:", rotar(ejemplo, 1))


ROTACIONES = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
c = "1111000011110000111100001111"
original = c

for r in ROTACIONES:

    c = rotar(c, r)                          

print("¿Regresó al original?", c == original)   

# ===== Fase 2: PC-1 =====

PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4,
]

def hex_a_bits(hex_str):
    # Convierte una llave hexadecimal en 64 bits de texto
    return format(int(hex_str, 16), "064b")

def permutar(bits, tabla):
    resultado = ""
    for n in tabla:
        resultado = resultado + bits[n-1]
    return resultado

llave = hex_a_bits("133457799BBCDFF1")
k_mas = permutar(llave, PC1)

print("Llave (64):", llave)
print("PC-1  (56):", k_mas, len(k_mas))
print("C0:", k_mas[:28])
print("D0:", k_mas[28:])

esperado = "11110000110011001010101011110101010101100110011110001111"
print("¿Correcto?", k_mas == esperado)

# ===== Fase 3: C y D + 16 rotaciones =====

ROTACIONES = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

c = k_mas[:28]
d = k_mas[28:]
historial = []

for ronda, n in enumerate(ROTACIONES, start=1):
    c = c[n:] + c[:n]
    d = d[n:] + d[:n]
    historial.append((c, d))
    print(f"Ronda {ronda:2}: C={c}  D={d}")

print("¿C1 correcto?", historial[0][0] == "1110000110011001010101011111")
print("¿D1 correcto?", historial[0][1] == "1010101011001100111100011110")
print("¿C16 == C0?", c == k_mas[:28])
print("¿D16 == D0?", d == k_mas[28:])
