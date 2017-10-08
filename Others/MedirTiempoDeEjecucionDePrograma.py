#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Medicion de tiempo de ejecucion de programa
# Creado por Ing. Jaime Andres Cataño Bernal
# 12102012
#
# Este programa presenta un comportamiento adecuado en ubuntu 12.04 64bit
# en un PC Asus eeePC 1005pe
# Donde la el tiempo medido es alrededor de 5.005 segundos para el retardo
# de 5 segundos definido con la funcion sleep.

import time

text = """
Este programa iniciara un temporizador, luego hara un retardo de 5 segundos
y finalmente detendra el temporizador para medir el tiempo que tomo el 
programa en ser ejecutado
"""

print text

tiempoinicio=time.time()

time.sleep(5)

tiempofinal=time.time()-tiempoinicio

print "Tiempo de ejecucion: ", tiempofinal, "segundos"
