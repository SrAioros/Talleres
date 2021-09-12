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

if(precio <= 0 or cantidad <= 0):
    print('Los datos no pueden ser menor a 1')
elif (cantidad >= 3):
    descuento = subtotal * 0.3
    total = subtotal - descuento
    print(f"El total a pagar es: ${total}")
    print(f"El descuento aplicado es: ${descuento}")
else:
    descuento = subtotal * 0.1
    total = subtotal - descuento
    print(f"El total a pagar es: ${total}")
    print(f"El descuento aplicado es: ${descuento}")






















