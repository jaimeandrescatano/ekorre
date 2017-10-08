#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
20150624
Obtener la fecha actual, la de manana y la del dia anterior

Objetivo: obtener los numeros del ano dia y mes para manipularlos 

Fuentes:
    
Notas: 
    
Keywords:
    fechas, operaciones con fechas 
    
Autor: Jaime Andres Cataño Bernal 
"""

from datetime import datetime, timedelta

objetofecha = datetime(2015, 07, 24)

ayer = objetofecha - timedelta(days=1)
manana = objetofecha + timedelta(days=1)

print manana.year 
print manana.month
print manana.day

print 'Anterior: %s Actual: %s Siguiente: %s' % (ayer, objetofecha, manana)
