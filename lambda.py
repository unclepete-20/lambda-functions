# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Creado por: Pedro Pablo Arriola Jimenez (20188)   
# Fecha de creación: 13/11/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Proyecto 2: Definición de funciones lambda""" 
# ---------------------------------------------------------------------------


# Definición de la funcion uno, la cual representa el numero natural 0
cero = lambda f: lambda x: x

# Definición de la funcion uno, la cual representa el numero natural 1
uno = lambda f: lambda x: f(x)

# Definición de la funcion uno, la cual representa el numero natural 2
dos = lambda f: lambda x: f(f(x))

# Definición de la funcion uno, la cual representa el numero natural 3
tres = lambda f: lambda x: f(f(f(x)))

# Definición de la funcion uno, la cual representa el numero natural 4
cuatro = lambda f: lambda x: f(f(f(f(x))))

# Definición de la funcion uno, la cual representa el numero natural 5
cinco = lambda f: lambda x: f(f(f(f(f(x)))))


# Definición de la funcion sucesor (n + 1)
sucesor = lambda n: lambda f: lambda x: f(n(f)(x))


# Definición de la funcion suma (a + b)
suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))


# Definición de la funcion multiplicacion (a * b)
multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)


# Definición de la funcion potencia (a ** b)
potencia = lambda a: lambda b: lambda f: lambda x: a(f)(x)


# Funciones con operaciones aritmeticas basicas
alpha = lambda x: x + 1
beta = lambda x: 2 * x


#----------------------------------------------------------------------------
# Ejemplos de las definiciones escritas utilizando funciones lambda   
# ---------------------------------------------------------------------------

print('\n-------------------------------- EJEMPLOS DE LA EJECUCION DE FUNCIONES LAMBDA --------------------------------')

print('\n\n**EJEMPLOS DE LA FUNCION LAMBDA SUCESOR**\n')

print('Sucesor de 0 utilizando funcion alpha con parametro 0 = ' + str(sucesor(cero)(alpha)(0))) # Primer ejemplo de la funcion sucesor utilizando alpha
print('Sucesor de 1 utilizando funcion alpha con parametro 0 = ' + str(sucesor(uno)(alpha)(0))) # Segundo ejemplo de la funcion sucesor utilizando alpha
print('Sucesor de 2 utilizando funcion alpha con parametro 0 = ' + str(sucesor(dos)(alpha)(0))) # Tercer ejemplo de la funcion sucesor utilizando alpha
print('Sucesor de 3 utilizando funcion alpha con parametro 0 = ' + str(sucesor(tres)(alpha)(0))) # Cuarto ejemplo de la funcion sucesor utilizando alpha
print('Sucesor de 4 utilizando funcion alpha con parametro 0 = ' + str(sucesor(cuatro)(alpha)(0))) # Quinto ejemplo de la funcion sucesor utilizando alpha
print('Sucesor de 5 utilizando funcion alpha con parametro 0 = ' + str(sucesor(cinco)(alpha)(0))) # Sexto ejemplo de la funcion sucesor utilizando alpha

print('\n')

print('Sucesor de 0 utilizando funcion beta con parametro 1 = ' + str(sucesor(cero)(beta)(1))) # Primer ejemplo de la funcion sucesor utilizando beta
print('Sucesor de 1 utilizando funcion beta con parametro 1 = ' + str(sucesor(uno)(beta)(1))) # Segundo ejemplo de la funcion sucesor utilizando beta
print('Sucesor de 2 utilizando funcion beta con parametro 1 = ' + str(sucesor(dos)(beta)(1))) # Tercer ejemplo de la funcion sucesor utilizando beta
print('Sucesor de 3 utilizando funcion beta con parametro 1 = ' + str(sucesor(tres)(beta)(1))) # Cuarto ejemplo de la funcion sucesor utilizando beta
print('Sucesor de 4 utilizando funcion beta con parametro 1 = ' + str(sucesor(cuatro)(beta)(1))) # Quinto ejemplo de la funcion sucesor utilizando beta
print('Sucesor de 5 utilizando funcion beta con parametro 1 = ' + str(sucesor(cinco)(beta)(1))) # Sexto ejemplo de la funcion sucesor utilizando beta


print('\n\n**EJEMPLOS DE LA FUNCION LAMBDA SUMA**\n')

print('Suma de cero y uno con funcion alpha y parametro 0 = ' + str(suma(cero)(uno)(alpha)(0))) # Primer ejemplo de la funcion suma utilizando alpha
print('Suma de dos y tres con funcion alpha y parametro 0 = ' + str(suma(dos)(tres)(alpha)(0))) # Segundo ejemplo de la funcion suma utilizando alpha
print('Suma de cuatro y cinco con funcion alpha y parametro 0 = ' + str(suma(cuatro)(cinco)(alpha)(0))) # Primer ejemplo de la funcion suma utilizando alpha

print('\n')

print('Suma de cero y uno con funcion beta y parametro 0 = ' + str(suma(cero)(uno)(beta)(1))) # Primer ejemplo de la funcion suma utilizando beta
print('Suma de dos y tres con funcion beta y parametro 0 = ' + str(suma(dos)(tres)(beta)(1))) # Segundo ejemplo de la funcion suma utilizando beta
print('Suma de cuatro y cinco con funcion beta y parametro 0 = ' + str(suma(cuatro)(cinco)(beta)(1))) # Primer ejemplo de la funcion suma utilizando beta}


print('\n\n**EJEMPLOS DE LA FUNCION LAMBDA MULTIPLICACION**\n')

print('Multiplicacion de cero y uno con funcion alpha y parametro 0 = ' + str(multiplicacion(cero)(uno)(alpha)(0))) # Primer ejemplo de la funcion multiplicacion utilizando alpha
print('Multiplicacion de dos y tres con funcion alpha y parametro 0 = ' + str(multiplicacion(dos)(tres)(alpha)(0))) # Segundo ejemplo de la funcion multiplicacion utilizando alpha
print('Multiplicacion de cuatro y cinco con funcion alpha y parametro 0 = ' + str(multiplicacion(cuatro)(cinco)(alpha)(0))) # Primer ejemplo de la funcion multiplicacion utilizando alpha

print('\n')

print('Multiplicacion de cero y uno con funcion beta y parametro 0 = ' + str(multiplicacion(cero)(uno)(beta)(1))) # Primer ejemplo de la funcion multiplicacion utilizando beta
print('Multiplicacion de dos y tres con funcion beta y parametro 0 = ' + str(multiplicacion(dos)(tres)(beta)(1))) # Segundo ejemplo de la funcion multiplicacion utilizando beta
print('Multiplicacion de cuatro y cinco con funcion beta y parametro 0 = ' + str(multiplicacion(cuatro)(cinco)(beta)(1))) # Primer ejemplo de la funcion multiplicacion utilizando beta


print('\n\n**EJEMPLOS DE LA FUNCION LAMBDA POTENCIA**\n')

print('La potencia de cero elevado a uno con funcion alpha y parametro 0 = ' + str(potencia(cero)(uno)(alpha)(0))) # Primer ejemplo de la funcion potencia utilizando alpha
print('La potencia de dos elevado a tres con funcion alpha y parametro 0 = ' + str(potencia(dos)(tres)(alpha)(0))) # Primer ejemplo de la funcion potencia utilizando alpha
print('La potencia de cuatro elevado a cinco con funcion alpha y parametro 0 = ' + str(potencia(cuatro)(cinco)(alpha)(0))) # Primer ejemplo de la funcion potencia utilizando alpha

print('\n')

print('La potencia de cero elevado a uno con funcion beta y parametro 0 = ' + str(potencia(cero)(uno)(beta)(1))) # Primer ejemplo de la funcion potencia utilizando beta
print('La potencia de dos elevado a tres con funcion beta y parametro 0 = ' + str(potencia(dos)(tres)(beta)(1))) # Primer ejemplo de la funcion potencia utilizando beta
print('La potencia de cuatro elevado a cinco con funcion beta y parametro 0 = ' + str(potencia(cuatro)(cinco)(beta)(1))) # Primer ejemplo de la funcion potencia utilizando beta
