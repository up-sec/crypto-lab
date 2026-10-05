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
