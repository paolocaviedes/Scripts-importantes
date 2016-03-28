import GPRMCtoWGS84 as func
import os

import webbrowser
new = 2 # open in a new tab, if possible

#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import time
import serial

#Para uso interno de while
flag=True

# Iniciando conexion serial
arduinoPort = serial.Serial('COM4', 9600, timeout=1)
flagCharacter = 'k'

# Retardo para establecer la conexin serial
time.sleep(1.8)
arduinoPort.write(flagCharacter)
while flag:
    getSerialValue = arduinoPort.readline()

    #getSerialValue = arduinoPort.read()
    #getSerialValue = arduinoPort.read(6)
    if getSerialValue.startswith("$GPRMC"):
        lista=getSerialValue.strip().split(",")
        if lista[2]=="V":
            print "No connection GPS"
        elif lista[2]=="A": 

            flag=False
            print '\nValor retornado de Arduino: %s' % (getSerialValue)
            print "----------------------------------------------------"
        
            latitud=func.latitudGPRMCdegrees(float(lista[3]),lista[4])
            print latitud
            longitud=func.longitudGPRMCdegrees(float(lista[5]),lista[6])
            print longitud

            zoom=12

            #maptype: m for map, k for satellite, h for hybrid, p for terrain, e for earth
            maptype="m"
            
            url="http://maps.google.com/maps?z="+str(zoom)+"&t="+str(maptype)+"&q=loc:"+str(latitud)+"+"+str(longitud)

            #url = "http://www.facebook.com"
            webbrowser.open(url,new=new)



    #terminar=str(raw_input('0 para terminar: '))
        #os.system("pause")
        #raw_input("Press enter to continue")

    #if terminar==0:
    #    flag=False

# Cerrando puerto serial
arduinoPort.close()