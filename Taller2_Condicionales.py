# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:53:51 2021

@author: Administrador
"""

# 1.

# Precio por el valor de camisa
precio = float(input('Digite el precio de la camisa: $'))
cantidad = int(input('Digite cantidad de camisas a comprar: '))
# Subtotal para aplicar descuento
subtotal = precio * cantidad
# descuento para que aplique a la compra de las camisas
descuento = 0
# total para precio a pagar por las camisas
total = 0

# Condicional para que los datos digitados sean válidos
if(precio <= 0 or cantidad <= 0):  
    print('Los datos no pueden ser menor o igual a 0')
# Condicional para el descuento del 30% si la cantidad de camisas es igual o 
# mayor a 3
elif (cantidad >= 3):
    descuento = subtotal * 0.3
    total = subtotal - descuento
    print(f'El total a pagar es: ${total}')
    print(f'El descuento aplicado es: ${descuento}')
# Condicional para el descuento del 10% si la cantidad de camisas es menor a 3
else:
    descuento = subtotal * 0.1
    total = subtotal - descuento
    print(f'El total a pagar es: ${total}')
    print(f'El descuento aplicado es: ${descuento}')

# 2.

# Precio2 por el total por la compra del mercado
precio2 = float(input('Digite el total de la compra: $'))
num_azar = int(input('Digite un número al azar mayor a 0: '))
# descuento2 para que aplique al mercado
descuento2 = 0
# total2 para el precio a pagar por el mercado
total2 = 0

# Condicional para que los datos digitados sean válidos 
if(precio2 <= 0 or num_azar <= 0):
    print('Los datos no pueden ser menor o igual a 0')
# Condicional para el descuento del 15% si el número al azar es menor a 75
elif(num_azar <= 74):
    descuento2 = precio2 * 0.15
    total2 = precio2 - descuento2
# Condicional para el descuento del 20% si el número al azar es mayor a 74
else:
    descuento2 = precio2 * 0.2
    total2 = precio2 - descuento2
    print(f'El total a pagar es: ${total2}')
    print(f'El descuento aplicado es: ${descuento2}')

# 3.

monto_inicial = float(input('Digite el total del monto a financiar: $'))
intereses = 0
# Condicional para que los datos digitados sean válidos 
if(monto_inicial <= 0):
    print('Los datos no pueden ser menor o igual a 0')
# Condicional para intereses con un monto inicial menor o igual a $50.000
elif(monto_inicial <= 50000):
    intereses = 0.03
    cuota = monto_inicial * intereses
# Condicional para intereses con un monto inicial mayor a $50.000
else:
    intereses = 0.02
    cuota = monto_inicial * intereses
    print(f'El total del monto a financiar es: ${monto_inicial}')
    print(f'El porcentaje aplicado es: {intereses} ')
    print(f'El valor de la cuota es: ${cuota}')

# 4. 

puntaje_dia1 = float(input('Digite los puntos del primer día: '))
puntaje_dia2 = float(input('Digite los puntos del segundo día: '))
puntaje_dia3 = float(input('Digite los puntos del tercer día: '))
puntaje_dia4 = float(input('Digite los punto del cuarto día: '))
puntaje_dia5 = float(input('Digite los punto del quinto día: '))

ganancias_dia1 = float(input('Digite las ganacias del primer día: '))
ganancias_dia2 = float(input('Digite las ganacias segundo día: '))
ganancias_dia3 = float(input('Digite las ganacias del tercer día: '))
ganancias_dia4 = float(input('Digite las ganacias del cuarto día: '))
ganancias_dia5 = float(input('Digite las ganacias del quinto día: '))

promedio = (puntaje_dia1 + puntaje_dia2 + puntaje_dia3 + puntaje_dia4 + puntaje_dia5) / 5
ganancias = (ganancias_dia1 + ganancias_dia2 + ganancias_dia3 + ganancias_dia4 + ganancias_dia5)
multa = 0

# Condicional para que los datos digitados sean válidos
if(puntaje_dia1 < 0 or puntaje_dia2 < 0 or puntaje_dia3 < 0 
   or puntaje_dia4 < 0 or puntaje_dia5 < 0
   or ganancias_dia1 < 0 or ganancias_dia2 < 0 or ganancias_dia3 < 0
   or ganancias_dia4 < 0 or ganancias_dia5 < 0):
    print('Los datos no pueden ser menor a 0')
# Condicional para aplicar multa
elif(promedio > 170):
    multa = ganancias * 0.5
    print(f'El promedio de puntos es: {promedio}')
    print(f'Se efectua la multa de: ${multa}')
# Condicional para cuando el puntaje de contaminación es leve
else:
    print('Todo esta en orden y no aplica multa')
 
# 5.

# Precio3 por el valor del terreno o automóvil
precio3 = float(input('Digite el precio del terreno o automovil: '))
porcentaje_incremento_terrenal = float(input('Digite el porcentaje del incremento anual del terreno: '))
porcentaje_devaluacion_automovil = float(input('Digite el porcentaje de la devaluación anual del automovil: ' ))

incremento = (((precio3 * porcentaje_incremento_terrenal) / 100) * 3) / 2
devaluacion = ((precio3 * porcentaje_devaluacion_automovil) / 100) * 3

print(f'La mitad del incremento del terreno en 3 años es: ${incremento}')
print(f'La devaluacion del automovil en 3 años es: ${devaluacion}')
# Condicional para determinar qué es mejor comprar
if(devaluacion < incremento):
    print('Debería comprar el automóvil')
else:
    print('Debería comprar el terreno')

# 6. 

# Precio4 para el valor del computador
precio4 = 11000

# cantidad2 para el número de computadores
cantidad2 = int(input('Digite cantidad de computadores a comprar: '))

# Subtotal2 para aplicar descuentos
subtotal2 = precio4 * cantidad2

# descuento3 para que aplique a la compra de computadores
descuento3 = 0

# total3 para precio a pagar por los computadores
total3 = 0

# Condicional para que los datos digitados sean válidos
if(precio4 < 0):
    print('Los datos no pueden ser menor a 0')
# Condicional para descuento del 10% al ser menos de 5 unidades compradas
elif(cantidad2 < 5):
    descuento3 = subtotal2 * 0.1
    total3 = subtotal2 - descuento3
    print(f'El total a pagar es de: ${total3}')
    print(f"El descuento aplicado es de: ${descuento3}")
# Condicional para descuento del 20% si las unidades compradas están entre 
# mayor o igual a 5 y menor a 10 unidades
elif(cantidad2 >= 5 and cantidad2 < 10):
    descuento3 = subtotal2 * 0.2
    total3 = subtotal2 - descuento3
    print(f'El total a pagar es de: ${total3}')
    print(f"El descuento aplicado es de: ${descuento3}")
# Condicional para el descuento po compras mayores o iguales a 10 unidades 
else:
    descuento3 = subtotal2 * 0.4
    total3 = subtotal2 - descuento3
    print(f"El total a pagar es: ${total3}")
    print(f"El descuento aplicado es de: ${descuento3}")














