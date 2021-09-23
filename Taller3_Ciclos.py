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


# 4.

# Al ejecutar promedioEdad(total_alumnos) poner la cantidad de alumnos 
# como parametro
def promedioEdad(total_alumnos):
    poblacion = 0
    total_edadesM = 0 
    total_edadesF = 0
    total_hombres = 0
    total_mujeres = 0
    
    for poblacion in range(1,total_alumnos + 1):
        edad = int(input('Digite la edad: '))
        genero = input('Ingrese el género (M o F): ')
        
        if(genero == 'M' or genero == 'm'):
            total_hombres = total_hombres + 1
            total_edadesM =  total_edadesM + edad
            promedioM = total_edadesM / total_hombres
            
        elif(genero == 'F'  or genero == 'f'):
            total_mujeres = total_mujeres + 1
            total_edadesF = total_edadesF + edad
            promedioF = total_edadesF / total_mujeres
        poblacion = poblacion + 1
        
        promedio_global = (total_edadesM + total_edadesF)/total_alumnos
        
    print(f'El promedio de edades de todo el grupo es de: {promedio_global}')    
    if(total_edadesM == 0):
        print('No hay hombres en la poblacion')
    else:
        print(f'El promedio de edades de Hombres es de: {promedioM}')
    if(total_edadesF == 0):
        print('No hay mujeres en la poblacion')
    else:
        print(f'El promedio de edades de Mujeres es de: {promedioF}')

# 5.

# Al ejecutar menor(num) poner la cantidad de números totales para sacar 
# el num menor
def menor(num):
    i  = 1
    for i in range(1,num + 1):
        n = int(input('Digite un número: '))
        if(i ==1):
            num_menor = n
        elif(n < num_menor):
            num_menor = n  
        i= i + 1       
    print(f'El número menor es: {num_menor}')
        


# 6.

def calcularPeso():
    
    peso_miembro1 = float(input('Digite el peso promedio de la última reunión del miembro 1: '))
    peso_miembro2 = float(input('Digite el peso promedio de la última reunión del miembro 2: '))
    peso_miembro3 = float(input('Digite el peso promedio de la última reunión del miembro 3: '))
    peso_miembro4 = float(input('Digite el peso promedio de la última reunión del miembro 4: '))
    peso_miembro5 = float(input('Digite el peso promedio de la última reunión del miembro 5: '))

    bascula = 1
    suma1 = 0
    suma2 = 0
    suma3 = 0
    suma4 = 0
    suma5 = 0
    
    for bascula in range(1, 10 + 1):
        peso = float(input(f'Digite el peso de la bascula {bascula} para el  miembro 1: '))
        suma1 = peso + suma1
        promedio1 = suma1 / 10
        bascula = bascula + 1
        
    print(promedio1)    
    if(peso_miembro1 < promedio1):
        print('El miembro 1 subio de peso')
    else:
        print('El miembro 1 bajó de peso')

    for bascula in range(1, 10 + 1):
        peso = float(input(f'Digite el peso de la bascula {bascula} para el miembro 2: '))
        suma2 = peso + suma2
        promedio2 = suma2 / 10
        bascula = bascula + 1
        
    print(promedio2)    
    if(peso_miembro2 < promedio2):
        print('El miembro 2 subio de peso')
    else:
        print('El miembro 2 bajó de peso')

    for bascula in range(1, 10 + 1):
        peso = float(input(f'Digite el peso de la bascula {bascula} para el miembro 3: '))
        suma3 = peso + suma3
        promedio3 = suma3 / 10
        bascula = bascula + 1
        
    print(promedio3)    
    if(peso_miembro3 < promedio3):
        print('El miembro 3 subio de peso')
    else:
        print('El miembro 3 bajó de peso')

    for bascula in range(1, 10 + 1):
        peso = float(input(f'Digite el peso de la bascula {bascula} para el miembro 4: '))
        suma4 = peso + suma4
        promedio4 = suma4 / 10
        bascula = bascula + 1
        
    print(promedio4)    
    if(peso_miembro4 < promedio4):
        print('El miembro 4 subio de peso')
    else:
        print('El miembro 4 bajó de peso')

    for bascula in range(1, 10 + 1):
        peso = float(input(f'Digite el peso de la bascula {bascula} para el miembro 5: '))
        suma5 = peso + suma5
        promedio5 = suma5 / 10
        bascula = bascula + 1
        
    print(promedio5)    
    if(peso_miembro5 < promedio5):
        print('El miembro 5 subio de peso')
    else:
        print('El miembro 5 bajó de peso')





