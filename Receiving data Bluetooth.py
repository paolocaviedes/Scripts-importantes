import os
import time
import serial
import datetime
from zeus import client

flag=True

# Iniciando conexion serial
arduinoPort = serial.Serial('COM8', 9600, timeout=1)
flagCharacter = 'k'

time.sleep(1.8)
arduinoPort.write(flagCharacter)


while flag:



    #timestamp de la hora del sistema
    #timestamp= int(time.mktime(datetime.datetime.strptime(systemTime,"%c").timetuple()))

    getSerialValue = arduinoPort.readline()
    listaSenales=getSerialValue.strip().split("*")
    identificador=listaSenales[0]
    enganche=listaSenales[1]
    gas=listaSenales[2]
    ruido=listaSenales[3]
    presion=listaSenales[4]
    temperatura=listaSenales[5]
    altimetro=listaSenales[6]
    oxigenacion=listaSenales[7]

    print getSerialValue


arduinoPort.close()

raw_input()