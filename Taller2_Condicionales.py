# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:53:51 2021

@author: Administrador
"""

# 1.

precio = float(input('Digite el precio de la camisa: $'))
cantidad = int(input('Digite cantidad de camisas a comprar: '))
subtotal = precio * cantidad
descuento = 0

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

precio2 = float(input('Digite el total de la compra: $'))
num_azar = int(input('Digite un número al azar mayor a 0: '))
descuento2 = 0
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

















