
# coding: utf-8

################### Comenzando a programar en Python ###########################

# PYTHON COMO CALCULADORA

#Sumamos dos números
5 + 5

#Restamos dos números
11 - 5

#Multiplicamos dos números 
13 * 9

#Dividimos dos números
9 / 8

#Obtenemos el módulo, es decir, el resto de dividir dos números
9 % 8

#Hacemos uso del operador exponente
2 ** 5


# VARIABLES EN PYTHON 

#Le asignamos el valor 5 a la variable x
x = 5
#Mostramos el valor de la variable x
print(x)


# En una variable podemos almacenar valores y operar con las variables.

#Almacenamos el valor 5 en la variable x y el valor 6 en la variable 6
x = 5
y = 6
#Guardamos en la variable producto la multiplicación de estas dos variables
producto = x * y
#Mostramos el resultado 
print(producto)


# Además de tomar valores numéricos una variable puede tomar valores de tipo string o de tipo booleanos.

#Le asignamos el string Hola a la variable saludo
saludo = 'Hola'
#Mostramos por pantalla el contenido de saludo
print(saludo)


#Le asignamos el valor True a la variable boolean
boolean = True
#Mostramos por pantalla el valor de la variable boolean
print(boolean)


# Dependiendo del tipo de valor que tome una variable, los operadores suma,
#producto etc le afectarán de una forma u otra.

#Guardamos en las variables saludo y nombre dos strings
saludo = 'Hola'
nombre = 'Pepe'
#Hacemos uso del operador suma para ver su efecto
print(saludo + nombre)

#Guardamos en saludo un string 
saludo = 'Hola'
#Hacemos uso del operador producto para ver su efecto
print(saludo * 3)


################################### Listas ####################################

#Nos creamos distintas variables que almacena en millones el número de habitantes
#en ciudades
Madrid = 3.16
Barcelona = 1.6
Valencia = 0.790
Sevilla = 0.690
#Nos creamos una lista de ciudades que contiene la población de distintas ciudades
lista_ciudades = [Madrid, Barcelona, Valencia, Sevilla]
#Mostramos el contenido de la lista
print(lista_ciudades)


# Una lista puede contener distintos tipos de variables.

#Nos creamos una lista de ciudades
lista_ciudades = ['Madrid', Madrid, 'Barcelona', Barcelona, 'Valencia', Valencia, 'Sevilla', Sevilla]
#Mostramos el contenido de la lista
print(lista_ciudades)

#Accedemos al número de habitantes de la ciudad de Madrid
print(lista_ciudades[1])

#Accedemos al número de habitantes de Sevilla
print(lista_ciudades[-1])


#Accedemos a los tres primeros elementos de nuestro lista
print(lista_ciudades[0:3])
print(lista_ciudades[:3])

#Accedemos desde el tercer elemento hasta el final
print(lista_ciudades[2:])


#Cambiamos el valor del nombre de la ciudad de Barcelona
lista_ciudades[2] = 'Bcn'
#Mostramos nuestra lista
print(lista_ciudades)

#Eliminamos el nombre de Sevilla de nuestra lista
del(lista_ciudades[-2])
print(lista_ciudades)


#Insertamos la ciudad de Sevilla en la posición que se encontraba antes
lista_ciudades.insert(5, 'Sevilla')
print(lista_ciudades)

#Agregamos la ciudad Granada y su población
lista_ciudades.append('Granada')
lista_ciudades.append(0.234)
#Mostramos el contenido
print(lista_ciudades)

#Concatenamos elementos a una lista.
lista_ciudades.extend(['Oviedo', 0.22])
print(lista_ciudades)


#Invertimos el orden de la lista.
lista_ciudades.reverse()
print(lista_ciudades)


#Vemos el número de veces que aparece la ciudad de Sevilla en lista_ciudades
print(lista_ciudades.count('Sevilla'))


#Vemos en que índice de la lista_ciudades se encuentra la ciudad Granada
print(lista_ciudades.index('Granada'))

#Comprovamos si Roma se encuentra en la lista_ciudades
print('Roma' in lista_ciudades)
#Comprobamos si Madrid se encuentra en la lista_ciudades
print('Madrid' in lista_ciudades)

#Hacemos uso de pop para eleminar el último elemento de la lista
lista_ciudades.pop()
print(lista_ciudades)

#Eliminamos la ciudad oviedo
lista_ciudades.remove('Oviedo')
print(lista_ciudades)

#Nos creamos dos listas
lista1 = [1,2,3]
lista2 = [4,5]
#Concatenamos con el operador suma
lista3 = lista1 + lista2
print(lista3)

#Replicamos lista3, 5 veces
print(lista3 * 5)

