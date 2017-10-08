# Este archivo es una coleccion de clases que se llamaran desde otros archivos

import math

class Calculadora: 
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)
        print "Los numeros a operar son: ", self.num1, "y", self.num2, "\n"
        
    def suma(self):
        print self.num1, "+", self.num2, "=", self.num1 + self.num2
    def resta(self):
        print self.num1, "-", self.num2, "=", self.num1 - self.num2    
    def multiplica(self):
        print self.num1, "*", self.num2, "=", self.num1 * self.num2    
    def divide(self):
        print self.num1, "/", self.num2, "=", self.num1 / self.num2
    def potencia(self):
        print self.num1, "^", self.num2, "=", math.pow(self.num1, self.num2)
    def raiz(self):
        print "sqrt(", self.num1, ")= ", math.sqrt(self.num1), "\n", "sqrt(",self.num2,")= ", math.sqrt(self.num2)

        
class Constantes:
    def __init__(self):
        self.pi = math.pi
        self.e = math.e

class Calculadora2(Calculadora):
    def __init__(self, nombre, numer1, numer2, color):
        self.name = nombre
        self.color = color
        self.num1 = float(numer1)
        self.num2 = float(numer2)
    def presentarcolor(self):
        print "El color de ", self.name, " es: ", self.color