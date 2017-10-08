# -*- coding: utf-8 -*-
import os


while True:
    print 'Ingrese el color a convertir'
    color = raw_input()
    print color
    
    print 'Descompongo en colores RGB'
    r = color[:2]
    g = color[2:4]
    b = color[4:]
    
    r=int(r,16)
    g=int(g,16)
    b=int(b,16)
    
    print r
    print g
    print b
    
    print 'Calculo los colores invertidos'
    r_in=255-r
    g_in=255-g
    b_in=255-b
    
    if r_in == 0:
        r_in = '00'
    else:
        r_in = str(hex(r_in))[2:]
        
    if g_in == 0:
        g_in = '00'
    else:
        g_in = str(hex(g_in))[2:]
        
    if b_in == 0:
        b_in = '00'
    else:
        b_in = str(hex(b_in))[2:]
    
    print r_in
    print g_in
    print b_in
    
    print 'Color invertido'
    color = r_in+g_in+b_in
    print color
    
    print 'presione enter'
    ok = raw_input()
    os.system("clear")
