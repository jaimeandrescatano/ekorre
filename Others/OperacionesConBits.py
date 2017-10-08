dato = 0b11100011

"""
    Hacer shift a la derecha pero dejar 1 en vez de ceros
"""

for i in range(0,8):
    y = dato << i 
    y = y + ((2**i)-1)
    print bin(y) 
    

print "Secuencia requerida 1 11 111 1111"

for i in range(0,8):
    a = (2**i)-1
    print bin(a)




