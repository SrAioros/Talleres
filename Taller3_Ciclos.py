# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 23:56:09 2021

@author: Administrador
"""

# 1.

# Al ejecutar ingresoAutos() poner el numero de autos que ingresan a la ciudad
# como parametro.

def ingresoAutos(num_autos):
    
    amarilla = 0
    rosa = 0
    roja = 0
    verde = 0
    azul = 0
# Ciclo que recorre el rango desde 1 hasta la cantidad digitado de autos que 
# ingresan a la ciudad con incremento    
    for i in range(1, num_autos + 1):
        placa = int(input('Digite el último digito de la placa del vehiculo:'))
# Condicionales que incrementan los contadores de acuerdo a la placa digitada        
        if(placa == 1 or placa == 2):
            amarilla = amarilla + 1
        elif(placa == 3 or placa == 4):
            rosa = rosa + 1
        elif(placa == 5 or placa == 6):
            roja = roja + 1
        elif(placa == 7 or placa == 8):
            verde = verde + 1            
        elif(placa == 9 or placa == 0):
            azul = azul + 1
            
    print(f'La cantidad de autos con calcomania Amarilla es: {amarilla}')
    print(f'La cantidad de autos con calcomania Rosa es: {rosa}')        
    print(f'La cantidad de autos con calcomania Roja es: {roja}')
    print(f'La cantidad de autos con calcomania Verde es: {verde}')
    print(f'La cantidad de autos con calcomania Azul es: {azul}')
