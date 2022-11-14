# -*- coding: utf-8 -*- Line 2
#----------------------------------------------------------------------------
# Creado por: Pedro Pablo Arriola Jimenez (20188)   
# Fecha de creación: 13/11/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Proyecto 2: Definición de funciones lambda""" 
# ---------------------------------------------------------------------------


# Definición de la funcion cero, la cual llama cero veces a la funcion especificada
cero = lambda f: lambda x: x

# Definición de la funcion uno, la cual llama una vez a la funcion especificada
uno = lambda f: lambda x: f(x)

# Definición de la funcion dos, la cual llama dos veces a la funcion especificada
dos = lambda f: lambda x: f(f(x))

# Definición de la funcion tres, la cual llama tres veces a la funcion especificada
tres = lambda f: lambda x: f(f(f(x)))


# Definición de la funcion sucesor (n + 1)
sucesor = lambda n, f: lambda x: f(n(f(x)))


# Definición de la funcion suma (a + b)
suma = lambda a, b, f: lambda x: a(f(b(f(x))))


# Definición de la funcion multiplicacion (a * b)
multiplicacion = lambda a, b, f: lambda x: a(b(f(x)))


# Definición de la funcion potencia (a ** b)
potencia = lambda a, b, f: lambda x: a(a(b(b(f(x)))))



# Funciones con operaciones aritmeticas basicas
alpha = lambda x: x + 1
beta = lambda x: 2 * x