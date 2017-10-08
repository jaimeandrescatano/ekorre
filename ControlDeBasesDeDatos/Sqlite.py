#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('Sqlite.db')


"""
    Verifico conexion con base de datos 
"""
with con:
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data 

"""
    Borro datos dentro de la tabla 
"""
# con = lite.connect('Sqlite-DATOS-RaspBerryPI.db')
# with con:
    # 
    # cur = con.cursor()    
    # cur.execute('DELETE FROM PeopleCounter')
    # 
    # data = cur.fetchone()
    # 
    # print "TABLA BORRADA!: %s" % data 
    
"""
    Presentar el ultimo id insertado 
"""
con = lite.connect('Sqlite-DATOS-RaspBerryPI.db')
with con:
    
    cur = con.cursor()    
    cur.execute('SELECT MAX(item) FROM PeopleCounter')
    
    data = cur.fetchone()
    
    print "Ultimo registro: %s" % data 
