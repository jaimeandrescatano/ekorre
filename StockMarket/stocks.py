#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
2016086
Captura de datos desde pagina web para analisis de stocks 

Objetivo: 
    Poder descargar de internet los valores de las acciones en las que se esta invirtiendo para su posterior analisis 

Fuentes:
    Buscar en internet: web scraping 
    https://www.youtube.com/watch?v=Mjjt__c4syY

Notas: 
    El principio es simple: detectar en la pagina web el codigo html donde esta el dato que quiero obtener, de hecho puedo conseguir mas informacion de otras fuentes. 
    
    PILAS!!!! para yahoo, o google el comando usado para mirar el precio de acciones es diferente al comando usado para mirar el precio de monedas 
    
    Bid: el precio del que quiere comprar 
    Ask: el precio del que quiere vender 
    Spread: la diferencia entre Bid y Ask 
    
    Indicadores:
    SMA muy interesante, puedo ver explicitamente que si se puede predecir la tendencia 

Keywords:
    stocks, web scraping, acciones, 

Estado:
    Toda identificar el dato del precio de cierre de la accion, porque estoy tomando un valor promedio pilas, tambien considerar tomar el precio de google para tener 2 referecias de diferentes fuentes. 
    
    La idea de un programa seria: tengo un programa en el servidor que lee cada cierto tiempo el valor de as acciones en las que estoy inviertiendo, cuando el valor de cada una de ellas alcanza un precio determinado entonces el programa me envia un email reportandome lo que debo hacer. De esta forma podria definir una serie de parametros para establecer diferentes acciones que me ayuden a tomar desiciones de forma rapida. Quizas el servidor podria eviarme la grafica de los valores capturados para yo poder analizar la tendencia, el volumen de acciones manejado etc. 

Autor: Jaime Andres Cataño Bernal 
"""

import urllib
import re 

symbolslist = ["ELTEL.ST", "AAPL", "GOOG", "PBR-A"]

i = 0
"""
while i < len(symbolslist):
    # url = "http://finance.yahoo.com/q?s=" + symbolslist[i] + "&ql=1"
    url = "http://finance.yahoo.com/quote/"+ symbolslist[i] +"=X/news?p="+ symbolslist[i] +"=X"
    # print url
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    # regex = '<span id="yfs_184_' + symbolslist[i] + '"(.+?)></span>'
    regex = '"ask":{"raw":(.+?),"fmt":"'
    pattern = re.compile(regex)
    price = re.findall(pattern,htmltext)
    print "The price of ", symbolslist[i], " is " , price
    i = i+1
"""

# Usar este para los valores de monedas
# url = "http://finance.yahoo.com/quote/"+ symbolslist[i] +"=X/news?p="+ symbolslist[i] +"=X"

# Usar este para los valores de acciones de empresas 
# i=0
# while i < len(symbolslist): 
    # url = "http://finance.yahoo.com/quote/"+ symbolslist[i] +"/?p="+ symbolslist[i] 
    # htmlfile = urllib.urlopen(url)
    # htmltext = htmlfile.read()
    ## regex = '<span id="yfs_184_' + symbolslist[i] + '"(.+?)></span>'
    ## "ask":{"raw":8.68262,"fmt":"8.68"}
    ## "ask":{"raw":102.9,"fmt":"102.90"},
    # regex = 'ask":{"raw":(.+?),'
    # pattern = re.compile(regex)
    # price = re.findall(pattern,htmltext)
    # print "The price of ", symbolslist[i], " is " , price
    # i= i+1

def YahooStockValue(StockSymbol):
    url = "http://finance.yahoo.com/quote/"+ StockSymbol +"/?p="+ StockSymbol
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    
    bid = '"bid":{"raw":(.+?),'
    pattern = re.compile(bid)
    
    bid_price = re.findall(pattern,htmltext)
    
    ask = '"ask":{"raw":(.+?),'
    pattern = re.compile(ask)
    
    ask_price = re.findall(pattern,htmltext)
    
    return(bid_price, ask_price)
    
def GoogleStockValue(StockSymbol):
    url = "https://www.google.com/finance?q="+ StockSymbol
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    
    # bid = '<span id="ref_413912260295883_l">(.+?)</span>'
    bid = '''<meta itemprop="price"
        content="(.+?)" />'''
    pattern = re.compile(bid)
    
    bid_price = re.findall(pattern,htmltext)
    
    return(bid_price)

print "Eltel"

YahooStockSymbol = 'ELTEL.ST'
GoogleStockSymbol = 'STO%3AELTEL' # Tomado de la barra de direcciones 

Stock1_bid_Yahoo, Stock1_ask_Yahoo = YahooStockValue(YahooStockSymbol)
Stock1_bid_Google = GoogleStockValue(GoogleStockSymbol)

print "Yahoo"
print "The bid (el precio del que quiere comprar) price of ", YahooStockSymbol, " is " , Stock1_bid_Yahoo
print "The ask (el precio del vendedor) price of ", YahooStockSymbol, " is " , Stock1_ask_Yahoo

print "Google"    
print "The bid (el precio del que quiere comprar) price of ", GoogleStockSymbol, " is " , Stock1_bid_Google




print "\n\nPetrobras:"

YahooStockSymbol = 'PBR-A'
GoogleStockSymbol = 'NYSE%3APBR.A' # Tomado de la barra de direcciones 

Stock1_bid_Yahoo, Stock1_ask_Yahoo = YahooStockValue(YahooStockSymbol)
Stock1_bid_Google = GoogleStockValue(GoogleStockSymbol)

print "Yahoo"
print "The bid (el precio del que quiere comprar) price of ", YahooStockSymbol, " is " , Stock1_bid_Yahoo
print "The ask (el precio del vendedor) price of ", YahooStockSymbol, " is " , Stock1_ask_Yahoo

print "Google"    
print "The bid (el precio del que quiere comprar) price of ", GoogleStockSymbol, " is " , Stock1_bid_Google




print "\n\nFord:"

YahooStockSymbol = 'F'
GoogleStockSymbol = 'NYSE%3AF' # Tomado de la barra de direcciones 

Stock1_bid_Yahoo, Stock1_ask_Yahoo = YahooStockValue(YahooStockSymbol)
Stock1_bid_Google = GoogleStockValue(GoogleStockSymbol)

print "Yahoo"
print "The bid (el precio del que quiere comprar) price of ", YahooStockSymbol, " is " , Stock1_bid_Yahoo
print "The ask (el precio del vendedor) price of ", YahooStockSymbol, " is " , Stock1_ask_Yahoo

print "Google"    
print "The bid (el precio del que quiere comprar) price of ", GoogleStockSymbol, " is " , Stock1_bid_Google

