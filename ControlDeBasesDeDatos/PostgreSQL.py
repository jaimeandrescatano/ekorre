#!/usr/bin/env python

"""
# Control de una base de datos en PostgreSQL con Python

# 20160905

# Este programa accede a una base de datos previamente creada en PostgreSQL
# desde PGadmin3
# 
# Probado en Postgresql 9.5.4 linux mint 17.2


Ejecutar estos comandos en pgadmin3 como usuario postgres
Estando en pgadmin3 servers > miserver > databases > postgres - estando sobre esta base de datos se habilita el comando del menu superior que es una lupa y permite ejecutar comandos directamente.

NOTAS:
    Despues de ejecutar cualquier comando seleccionar con el mouse el nombre del servidor en pgadmin3 y dar en refresh para ver los cambios, si no no funciona 

Siendo usuario postgres estando ejecutar:

/* Modelo para la creacion del usuario: pass: ingenieria pilas si no se si cambie en otros equipos en ese caso crear el usuario manualmente*/
    CREATE ROLE chepe LOGIN ENCRYPTED PASSWORD 'md5aac93a4ffd36b722eb000713eb664ace'
      NOINHERIT CREATEDB
       VALID UNTIL 'infinity';

/* Modelo para crear la base de datos: */
    CREATE DATABASE db1
      WITH ENCODING='UTF8'
           OWNER=chepe
           CONNECTION LIMIT=-1;

/* Ejecutar este comando despues de ejecutar el de creacion de la base de datos, no se porque no me deja hacerlo al tiempo */
REVOKE ALL ON DATABASE db1 FROM public;

Siendo usuario chepe estando en la conexion nueva propia de este usuario creada en pgadmin3 ejecutar:

/* Modelo para crear el schema: */
    
    CREATE SCHEMA mischema1
        AUTHORIZATION chepe;

/* Modelo de la tabla para la base de datos */

    CREATE TABLE mischema1.tabla1
    (
       id character varying(15), 
       nombre character varying(15), 
       telefono character varying(15), 
       CONSTRAINT id_pk PRIMARY KEY (id)
    ) 
    WITH (
      OIDS = FALSE
    )
    ;
    ALTER TABLE mischema1.tabla1
      OWNER TO chepe;


"""

import psycopg2
import sys
import os

os.system("clear")

con = None

print "Conectando con servidor PostgreSQL \n"
try:

    con = psycopg2.connect(host = 'localhost', port = "5432", user = 'chepe', password = 'ingenieria', database = 'db1');

    cur = con.cursor()
    cur.execute("SELECT VERSION();")

    data = cur.fetchall()
    
    print data
    print "\n"
    
    # Defino la tabla sobre la cual trabajare
    latabla = 'mischema1.tabla1'
    
    print 'Working table: %s\n' % latabla
    
    print "System ready! \n"
    
except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

while True:
    print "0- Show current information in the table \n"
    print "1- Add data \n"
    print "2- Search \n"
    print "3- Update data \n"
    print "4- Delete register \n"
    print "5- Exit program \n"
    
    dato = raw_input()
    
    if dato == "0":
        
        os.system("clear")
        print "The table schema1.tabla1 has this information: \n"
        # ## texto="SELECT * FROM pg_catalog.pg_tables"  
        texto="select * from mischema1.tabla1"  
        
        # print "The database has this tables: \n"
        ## texto="SELECT * FROM pg_catalog.pg_tables"  
        # texto="select * from pg_tables where schemaname='mischema1';"  
        cur.execute(texto)
        con.commit()
        salida = cur.fetchall()
        
        numrows = int(cur.rowcount)
        
        for x in xrange(numrows):
            print salida[x]
            
        raw_input("\nPress any key to return")
        os.system("clear")
        
        
    if dato == "1":
        
        os.system("clear")
        print ('Current table: %s' % (latabla)) 
        id_var = raw_input("id: ")
        nombre = raw_input("Nombre: ")
        telefono = raw_input("telefono: ")
        
        # texto='INSERT INTO %s (id, nombre, telefono) VALUES(\'%s\', \'%s\', \'%s\')' % (latabla, id_var, nombre, telefono)
        # cur.execute(texto)
        
        texto='INSERT INTO %s (id, nombre, telefono) VALUES(%s, %s, %s)'  % (latabla, '%s', '%s', '%s') # paso el nombre de la tabla porque no requiere comillas simples
        print texto
        cur.execute(texto, (id_var, nombre, telefono))
        con.commit()
        
        print "\n"+nombre+" info has been added to mischema1.table1! \n"
        
        raw_input("\nPress any key to return")
        os.system("clear")
    
    if dato == "2":
        
        os.system("clear")
        tabla = raw_input("\nSearch \nSelect table to search data: (tip: mischema1.tabla1 ;)  ) ")
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
        tabla = raw_input("\nUpdate \nIn which table is the data?: (tip: mischema1.tabla1 ;)  )")
        parametro = raw_input("Id of the register: ")
        campo = raw_input("Which field to update: ")
        datonuevo = raw_input("New data: ")
        
        texto="UPDATE "+tabla+" SET "+campo+" = '"+datonuevo+"' WHERE 'ID' LIKE '%"+parametro+"%'"
        print texto
        # UPDATE "mischema1"tabla1 SET nombre = 'kiko' WHERE 'ID' LIKE '%23%'
        cur.execute(texto)
        con.commit()
        print "Register "+parametro+" has been updated!\n"
        
        raw_input("\nPress any key to return")
        os.system("clear")
        
    if dato == "4":
        os.system("clear")
        tabla = raw_input("\nDelete \nIn which table is the data?: ")
        parametro = raw_input("Id of the register that you want to delete? ")
        texto="DELETE FROM "+tabla+" WHERE 'ID' LIKE '%"+parametro+"%'"
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
