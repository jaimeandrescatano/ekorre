#!/usr/bin/env python

# Control de una base de datos en MySQL con Python

# 16072012

# Este programa accede a una base de datos previamente creada en MySQL 
# desde PHPMyAdmin, permite realizar las operaciones principales de un
# sistema CRUD
# 
# - Create: crea un registro en una tabla
# - Retrieve: permite buscar y presentar un registro de una tabla
# - Update: permite actualizar un registro de una tabla
# - Delete: permite eliminar el registro de una tabla

import MySQLdb as mdb
import sys
import os

os.system("clear")

con = None

print "Conectando con servidor MySQL \n"
try:

    con = mdb.connect('localhost', 'root', '1milliondollar', 'PythonTest1');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    data = cur.fetchone()
    
    print "Database version : %s " % data
    print "System ready! \n"
    
except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

while True:
    print "0- Show current tables \n"
    print "1- Add data \n"
    print "2- Search \n"
    print "3- Update data \n"
    print "4- Delete register \n"
    print "5- Exit program \n"
    
    dato = raw_input()
    
    if dato == "0":
        
        os.system("clear")
        print "The database has this tables: \n"
        texto="SHOW tables"  
        cur.execute(texto)
        con.commit()
        
        numrows = int(cur.rowcount)
        
        for i in range(numrows):
            row = cur.fetchone()
            print row[0]
            
        raw_input("\nPress any key to return")
        os.system("clear")
        
    if dato == "1":
        
        os.system("clear")
        tabla = raw_input("\nAdd data \nSelect table: ")
        nombre = raw_input("Nombre: ")
        telefono = raw_input("telefono: ")
        
        texto="INSERT INTO "+tabla+"(Name,Phone) VALUES('"+nombre+"','"+telefono+"')"  
        cur.execute(texto)
        con.commit()
        
        print "\n"+nombre+" info has been added to "+tabla+"! \n"
        
        raw_input("\nPress any key to return")
        os.system("clear")
    
    if dato == "2":
        
        os.system("clear")
        tabla = raw_input("\nSearch \nSelect table to search data: ")
        campo = raw_input("Choose search field: ")
        parametro = raw_input("Search data: ")
        texto="SELECT * FROM "+tabla+" WHERE "+campo+" LIKE '%"+parametro+"%'"
        cur.execute(texto)
        con.commit()
        
        numrows = int(cur.rowcount)
        
        for i in range(numrows):
            row = cur.fetchone()
            print row[0], row[1]
            
        raw_input("\nPress any key to return")
        os.system("clear")
    
    if dato == "3":
        os.system("clear")
        tabla = raw_input("\nUpdate \nIn which table is the data?: ")
        parametro = raw_input("Id of the register: ")
        campo = raw_input("Which field to update: ")
        datonuevo = raw_input("New data: ")
        
        texto="UPDATE "+tabla+" SET "+campo+" = '"+datonuevo+"' WHERE ID = "+parametro
        #~ print texto
        cur.execute(texto)
        con.commit()
        print "Register "+parametro+" has been updated!\n"
        
        raw_input("\nPress any key to return")
        os.system("clear")
        
    if dato == "4":
        os.system("clear")
        tabla = raw_input("\nDelete \nIn which table is the data?: ")
        parametro = raw_input("Id of the register that you want to delete? ")
        texto="DELETE FROM "+tabla+" WHERE Id = "+parametro
        cur.execute(texto)
        con.commit()
        print "Register "+parametro+" has been deleted!\n"
        
        raw_input("\nPress any key to return")
        os.system("clear")
    
    if dato == "5":
        break    

print "Bye bye!"

if con:
    con.close()
