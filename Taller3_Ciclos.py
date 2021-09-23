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

# 2.

# Al ejecutar porcentajesAnimales() sin parametros pide a qué tipo de animales
# se va a realizar el estudio
def porcentajesAnimales():
    
    categoria1 = 0
    categoria2 = 0
    categoria3 = 0
    print('1 = Elefantes')
    print('2 = Jirafas')
    print('3 = Chimpances')
    poblacion = int(input('De acuerdo al menú anterior elija el animal que se estudiará: '))
 
# Condicional para que de acuerdo al animal elegido se tome el número de muestras
# correspondiente
    if poblacion > 0:
       if poblacion == 1:
           animal = 'Elefantes'
           total = 20
       elif poblacion == 2:
            animal = 'Jirafas'
            total = 15
       elif poblacion == 3:
            animal = 'Chimpances'
            total = 40     
    else:
        print('Digite un numero dentro del rango permitido del 1 al 3')
    
# Ciclo que ejecuta el número de edades a pedir de acuerdo al animal 
    for i in range(1,total + 1):
        edad = int(input('Ingrese la edad del animal: '))
        if(edad >= 0 and edad <= 1):
            categoria1= categoria1 + 1
        elif(edad > 1 and edad < 3):
            categoria2 = categoria2 + 1
        elif(edad >= 3):
            categoria3 = categoria3 + 1   
# Cálculo de porcentajes
    calculo1 = float((categoria1/total))*100
    calculo2 = float((categoria2/total))*100
    calculo3 = float((categoria3/total))*100
    
# Imprime el animal estudiado, rango de edad y porcentaje 
    if(edad >= 0 and edad <= 1):        
        print(f'Animal estudiado: {animal}')
        print (f'{calculo1} % de 0 a 1 año' )       
    elif(edad > 1 and edad < 3):    
        print(f'Animal estudiado: {animal}')
        print(f'{calculo2} % de mas de 1 año y menos de 3')        
    elif(edad >= 3):
        print(f'Animal estudiado: {animal}')        
        print(f'{calculo3} % de 3 o mas años')     
        

# 3. 

# Al ejecutar calcularSalario() poner el número de obreros que ingresa a la 
# empresa como parametro
def calcularSalario(num_obreros):
    
    salario = 0
    horas = 0
    h_extras = 0
    obrero = 1
# Condicional de verificación de datos
    if(num_obreros >= 1):
# Ciclo para pedir las horas trabajadas a cada obrero de acuerdo al parámetro
        for obrero in range(0,num_obreros + 1):
            horas = int(input('Digite el número de horas trabajadas:'))
# Condicional para pagar horas trabajadas normales o horas extras    
            if horas >=1 and horas <=40:
                salario = float(horas * 20)                
            else:
                h_extras = horas - 40
                salario = 40 * 20 + (h_extras * 25)
                
            obrero = obrero + 1    
            print(f'El salario del obrero {obrero} es:  {salario}')   
    else:
        print('Digite un número válido en el parámetro')


