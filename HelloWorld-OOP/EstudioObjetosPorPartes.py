# Objetos en Python por modulos
#
# Debido a que Pyside emplea solo objetos en su estructura profundizare un 
# poco en el empleo de objetos. Y ahora voy a partir el archivo en varios para 
# tener una especie de libreria de clases. 
#
# Notas: 
# - Ver que el archivo Clases se llama como si fuera un modulo cualquiera
# - Ver que para poder crear los objetos me toca usar la sintaxis 
# Modulo.Clase(args)

import os
import Clases


# Borro la pantalla
os.system('clear')
        
# Creo mi objeto
print "PROBANDO LA PRIMER CLASE: Calculadora\n"
num1 = raw_input("Ingrese el primer numero: ")
num2 = raw_input("Ingrese el segundo numero: ")
calculo1 = Clases.Calculadora(num1,num2)

# Realizo operaciones
calculo1.suma()
calculo1.resta()
calculo1.multiplica()
calculo1.divide()
calculo1.potencia()
calculo1.raiz()

# Creo un objeto de constantes
print "\n\nPROBANDO LA SEGUNDA CLASE: Constantes\n"
const1 = Clases.Constantes()
print const1.pi
print const1.e

# Creo un objeto de la clase Calculadora2 que hereda de Calculadora1 todos los metodos
print "\n\nPROBANDO LA TERCER CLASE: Calculadora2\n"
num1 = raw_input("Ingrese el primer numero: ")
num2 = raw_input("Ingrese el segundo numero: ")
calculodecolor1 = Clases.Calculadora2("calculodecolor1", num1, num2, "verde")
calculodecolor1.presentarcolor()
calculodecolor1.suma()


raw_input("\nPresione Enter para salir...")     
