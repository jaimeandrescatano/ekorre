#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
20141231
Este programa lee un archivo de CSV y procesa la informacion considerando la teoria de la estadistica con el objetivo de encontrar la distribucion que mas se aproxime a los datos 

Para el manejo de los datos se esta usando el modulo PANDAS

Desde la hoja de excel se tiene que: 
    - Exportar la tabla desde excel a .csv en libreoffice. Separar los campos por comas. y usar UTF-8

References: 
Comandos para analizar los datos:
    http://pandas.pydata.org/pandas-docs/stable/api.html#computations-descriptive-stats

Autor: Jaime Andres Cataño Bernal 
"""

from pandas import read_csv, period_range
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

f = read_csv('DatosDeSimulacion.csv', header=None, skiprows=1 ) # Le digo que no incluya la primer fila 

# print f # Notar que se crea una columna y una fila al inicio de la tabla para numerar las filas y las columnas 

f.columns = ['Sistema1',  'Sistema2', 'Sistema3', 'Sistema4', 'Sistema5'] # Le coloco un nombre a las columnas, para reemplazar los numeros automaticos 
# f.index = period_range('1-1970', '12-1991', freq='Q')

print f
print f['Sistema1'] # Presento una columna
print f['Sistema2'] # Presento una columna 
print f['Sistema3'][4] # Presento un dato exacto de una columna 
print f[f["Sistema4"] == 9.71] # Presento las filas que cumplan con una condicion especifica 
# print f[f["PIB"] > 3000 and f["IDP"] == 2272] # COMO HAGO ESTO? OSEA, USAR 2 o mas condiciones  

print "\nProcesado de la informacion con comandos de pandas\n" + "-" * 50     

print "La media de cada columna es: " 
print f.mean()

print "\nLa media de la columna Sistema1 es %s " % f["Sistema1"].mean() # Tomo el valor de la media de solo una columna 

print "\nPresentando la informacion con el comando 'describe'"
print f["Sistema1"].describe() # Presento varios datos con un solo comando 
var1 = f["Sistema1"].describe() # Presento varios datos con un solo comando 
# print type(var1) # Presento el tipo de var1

print "\nTomo algunos datos particulares que me da el comando 'describe'"
print "De la funcion 'describe' presento solo la std: %s " % var1["std"] # Notar como llamo cada valor
print "De la funcion 'describe' presento solo max: %s " % var1["max"]

print "\nAplico otros comandos a los datos"
print "La media de la columna Sistema1 es %s " % f["Sistema1"].mean() # Tomo el valor de la media de solo una columna 
print "La moda de la columna Sistema1 es %s " % f["Sistema1"].mode() # Tomo el valor de la media de solo una columna 
print "La suma de la columna Sistema1 es %s " % f["Sistema1"].sum() # Tomo el valor de la media de solo una columna 
print "La mean de la columna Sistema2 para los valores de Sistema1 que sean mayores a 35 es %s" % f[f["Sistema1"] > 35]["Sistema2"].mean()

print "\nPresento el Histograma de una serie de datos y una linea de ajuste\n" + "-" * 50     

mu = f["Sistema1"].mean() # mean of distribution
sigma = f["Sistema1"].std() # standard deviation of distribution
# x = mu + sigma * np.random.randn(10000)
x = f['Sistema1']

num_bins = 50
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, normed=1, color='green', alpha=0.5)

# print "Valor de n = %s" % n
# print "Valor de bins = %s" % bins
# print "Valor de patches = %s" % patches

y = mlab.normpdf(bins, mu, sigma) # add a 'best fit' line OJO esta estaba seleccionada por el ejemplo pero la idea es buscar la que mas se ajuste 

plt.plot(bins, y, 'r--')

plt.xlabel('Smarts')
plt.ylabel('Probability')
# print("{0:.2f}".format(sigma)) # Asi limito a solo 2 decimales
var2 = 'Histograma del {0}: $\mu= {1}$ y  $\sigma= {2}$'.format(unicode(f.columns[0],'utf-8'),  "{0:.2f}".format(mu),  "{0:.2f}".format(sigma))
plt.title(var2)
# plt.subplots_adjust(left=0.15) # Tweak spacing to prevent clipping of ylabel A mi me funciona bien 
print "\n   Notar que la funcion normal no se acerca en lo absoluto a los datos dados."
plt.show()

print "\nBuscando la mejor distribucion posible\n" + "-" * 50     
"""
Ahora, la idea es poder encontrar una funcion que se ajuste a la distribucion de los datos, las distribuciones que maneja el programa Automod son:
    Uniform
        exponencial 
        normal 
        triangular
        uniform
        lognormal - usar esta en vez de la gamma, mirar imagenes, esta tiene una propiedad de simetria 
        gamma - igualita a la lognormal no veo diferencia  
        weibull
        
    Discrete
        poisson 
        binomial 
        geometric 
"""
