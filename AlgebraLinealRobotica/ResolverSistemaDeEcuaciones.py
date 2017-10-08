#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
20170425
Resolver sistema de ecuaciones usando algebra lineal

Objetivo: Tomar un sistema de ecuaciones y resolverlo usando algebra de matrices y vectores

Fuentes:
    video de youtube

Status:

Notas: 

    Se tiene el sistema de ecuaciones 
    
        1a + 1b = 35
        2a + 4b = 94
    
    Planteandolo en forma de matrices y vectores:
        
        AX = B
        
        Donde A es una matriz, X un vector y B un vector
        
        A = [1 1, 2 4]
        X = [A B]T
        B = [35 94]T
        
    Para encontrar X: 
        X = A_inversa * B

Keywords:
    robotica, matriz, resolver sistema ecuaciones, 
    
Autor: Jaime Andres Cataño Bernal 
        
"""


import numpy as np

# define matrices
A = np.matrix([[1,1],[2,4]])
B = np.matrix([[35],[94]])

# Find the inverse of A
A_inverse = np.linalg.inv(A)

# Solving for X 
X = A_inverse * B

print X
