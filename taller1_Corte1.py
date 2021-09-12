# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 17:55:21 2021

@author: Desarrollo
"""

# dngdhn

"""
TALLER PARTE 1

"""

# 1. 
# y=((5+2-5)^2*5+8/2-30)/2*5-3

base = 5+2-5
potencia = base ** 2

y = ((potencia * 5 + (8/2)-30) / 2)* 5 - 3

print(y)

# 2. 
# z=5, n=3, m=z-n
# y=(((z+2-n)^2*m+8/2-30)/2*5-3)^5+15*3-9/3

z = 5
n = 3
m = z - n

y = float((((((z + 2 - n)** 2) * m + 8 / 2 - 30) / 2) * 5 - 3)** 5 + 15 * 3 - (9 / 3))

print (y)

# 3. 
# z=5
# n= ((8+2-4)^2*5+8+7/2-30*5)/2*5-3 
# m= z^2*3+n
# y= ((((z+2-n)^2 x m+8/2-30)/2*5-3)^5+15*3-9/3)^2-5/4

z = 5
n = float((((8 + 2 - 4) ** 2) * 5 + 8 + 7 / 2 - 30 * 5) / 2 * 5 - 3)
m = float(((z ** 2 ) * 3 + n))

y = (((((((z + 2 - n) ** 2)* m + 8/2 - 30)/ 2 * 5 - 3) ** 5) + 15 * 3 - 9/3) ** 2 ) - 5/4

print(y)

"""
TALLER PARTE 2

"""

# 1.

presion = float(input('digite el valor de la presión: '))
volumen = float(input('digite el valor del volumen: '))
temperatura = float(input('digite el valor de la temperatura: '))

masa = (presion*volumen)/(0.37*(temperatura+460))

print(f'El valor de la masa es: {masa}')

# 2. 

edad = int(input('digite la edad de la persona: '))

pulsaciones = (200-edad)/10

print(f'La persona debe tener {pulsaciones} por cada 10 segundos')

# 3.

socio_uno = float(input('digite el valor invertido por el primer socio: $ '))
socio_dos = float(input('digite el valor invertido por el segundo socio: $ '))
socio_tres = float(input('digite el valor invertido por el tercer socio: $ '))

inversionTotal = socio_uno + socio_dos + socio_tres

porcentaje1 = (socio_uno/inversionTotal)*100 
porcentaje2 = (socio_dos/inversionTotal)*100
porcentaje3 = (socio_tres/inversionTotal)*100

print(f'El porcentaje que invirtió el primer socio es: {porcentaje1} %')
print(f'El porcentaje que invirtió el segundo socio es: {porcentaje2} %')
print(f'El porcentaje que invirtió el tercer socio es: {porcentaje3} %')

# 4.

saldo_inicial = float(input('digite el saldo inicial: $'))
interes = saldo_inicial * 0.015
saldo_final = saldo_inicial - interes

print(f'El saldo final del ahorrador es: ${saldo_final}')

# 5.

sueldo_base = float(input('Digite el sueldo base: $'))
ley_publica = sueldo_base * 0.01
seguro_social = sueldo_base * 0.04
seguro_forzoso = sueldo_base * 0.005
caja_ahorro = sueldo_base * 0.05

total_descuentos = ley_publica + seguro_social + seguro_forzoso + caja_ahorro

print(f'El descueto de la ley publica es: ${ley_publica}')
print(f'El descueto del seguro social es: ${seguro_social}')
print(f'El descueto del seguro forzoso es: ${seguro_forzoso}')
print(f'El descueto por caja de ahorro es: ${caja_ahorro}')

print(f'El total a pagar es: ${total_descuentos}')

# 6.

cantidad_palabras = int(input('Digite la cantidad de palabras del aviso: '))
centimetros = int(input('Digite los centimetros que ocupa el aviso: '))
colores = int(input('Digite la cantidad de colores del aviso: '))

costo_palabras = cantidad_palabras * 20000
costo_centimetros = centimetros * 15000
costo_colores = colores * 25000

costo_aviso = costo_palabras + costo_centimetros + costo_colores

print(f'El total a pagar por el aviso es: ${costo_aviso}')

# 7. 

antiguedad = float(input('Digite la cantidad de años elaborados en la empresa: '))

if antiguedad == 1:
    bono = 100000
    print(f'El valor de su bono es: ${bono}')
else:
    bono = (antiguedad * 120000)-20000
    print(f'El valor de su bono es: ${bono}')

# 8.

horas = int(input('Digite la cantidad de horas trabajadas: '))

salario = horas * 20000
desc = salario * 0.05
sueldo = salario - desc

print(f'El sueldo del profesor es: ${sueldo}')

# 9. 

monto_inicial = int(input('Digite el monto inicial de la tarjeta: '))
print('Aviso: El monto final no debe ser mayor al monto inicial')
monto_final = int(input('Digite el monto final de la tarjeta: '))

valor_llamada = (monto_inicial - monto_final) * 1.20 

print(f'El costo de la llamada es: ${valor_llamada}')

# 10. 

fotos = int(input('Digite la cantidad de fotos a revelar: '))
valor = (fotos *1500 )*1.16

print(f'El monto total a pagar es: ${valor} iva incluido')

# 11.

presupuesto = float(input('Digite el monto presupuestal total: $'))

ginecologia = presupuesto * 0.4
traumatologia = presupuesto * 0.3
pediatria = presupuesto * 0.3

print(f'El presupuesto de Ginecología es de: ${ginecologia}')
print(f'El presupuesto de Traumatología es de: ${traumatologia}')
print(f'El presupuesto de Pediatría es de: ${pediatria}')

# 12.

peliculas = int(input('Digite la cantidad de peliculas a alquilar: '))
dias = int(input('Digite la cantidad de días que tendrá las peliculas: '))

if peliculas == 1:
    precio = (peliculas * 1500) * dias
    print(f'El valor a pagar por el alquiler es: ${precio}')
else: 
    promocion = 1500
    precio = ((peliculas * 1500) * dias ) - promocion
    print(f'El valor a pagar por el alquiler es: ${precio}')

# 13.

familia = int(input('Digite la cantidad de personas en la famimlia: '))
dias = int(input('Digite la cantidad de dias del tour: '))

precioBase = (familia * 25000) * dias 
IVA = (precioBase * 12) / 100
precioTotal = precioBase + IVA

print(f'El valor a pagar por el tour es: ${precioTotal}')

# 14. 

dias = float(input('Digite la cantidad de dias durante la estadía: '))

if dias == 1:
    valor = 100000
    print(f'El valor por su estadía es de: ${valor}')
else:
    valor = (dias * 200000)-100000
    print(f'El valor de su bono es: ${valor}')

# 15.

prestamo = float(input('Digite la cantidad prestada al empresario: $'))

base_cuotaEsp = prestamo/2
cuotaEsp = base_cuotaEsp / 4
valor_cuotaEsp = cuotaEsp + (cuotaEsp * 0.24)

print(f'El valor de cada cuota especial es de: ${valor_cuotaEsp}')

base_cuotaOrdinaria = prestamo / 2
cuotaOrdinaria = base_cuotaOrdinaria / 20
valor_cuotaOrdinaria = cuotaOrdinaria + (cuotaOrdinaria * 0.24)

print(f'El valor de cada cuota ordinaria es de: ${valor_cuotaOrdinaria}')

paga_total = (valor_cuotaEsp * 4) + (valor_cuotaOrdinaria * 20)

print(f'El monto total a pagar es de: ${paga_total}')


