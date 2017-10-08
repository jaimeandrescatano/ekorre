#!usr/bin/env python  
#coding=utf-8

# Es necesario editar 
# sudo vim /etc/crontab
# Edicionar: */15 * * * * root python /JAIMEANDRES/ArchivosSistema/BatteryAlarm.py
#
# Reiniciar servicio de cron: sudo service cron stop / start
#
# Este archivo requiere tener en su misma carpeta el archivo 
# ReproductorDeSonidos.py 
#
# Para generar los archivos de sonido .WAV usar: 
# espeak -s 150 -v es-la -w BateriaCargada.wav "La bateria esta cargada, por favor desconectar el cargador."
#
# O tambien usar: 
# echo The battery is at 15% of charge, please plug the charger now. | text2wave >job.wav
# Y para abrir el archivo .wav desde la consola:
# aplay job.wav

# Leo el archivo que almacena el valor actual de carga en la bateria
with open("/sys/class/power_supply/BAT0/capacity") as f:
    content = f.readlines()
# Convierto el texto a entero
valor = int(content[0])

#~ print valor

# Cierro el archivo
f.close()

# Obtengo el estado actual
with open("/sys/class/power_supply/BAT0/status") as f:
    content = f.readlines()
estado = str(content[0])

# Cierro el archivo
f.close()

# Quito caracteres adicionales de la variable "estado"
estado = estado.replace(" ", "")
estado = estado.replace("\r", "")
estado = estado.replace("\n", "")

from ReproductorDeSonidos import ReproductorWAV

# Creo las funciones de reproduccion de sonido
def BateriaCargada():
    Rep = ReproductorWAV("/JAIMEANDRES/ArchivosSistema/BateriaCargada.wav")
    Rep.Reproducir()

def BateriaDescargada():
    Rep = ReproductorWAV("/JAIMEANDRES/ArchivosSistema/BatteryAlert.wav")
    Rep.Reproducir()

# Analizo el estado de la bateria
if valor > 95:
    if estado != "Discharging":
        BateriaCargada()
if valor <= 15:
    if estado == "Discharging":
        BateriaDescargada() 
       
