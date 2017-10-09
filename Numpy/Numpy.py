
# coding: utf-8

##################################### Numpy ###################################

#Importamos Numpy
import numpy as np 
#Nos creamos dos listas
lista_productos = ['Boligrafo', 'Libreta', 'Agenda', 'Grapadora']
lista_precios = [1.90, 2.45, 3.89, 10.90]
lista_ventas = [10, 15, 20, 5]
#Convertimos las listas a objetos de tipo array
np_lista_precios = np.array(lista_precios)
np_lista_ventas = np.array(lista_ventas)
np_lista_productos = np.array(lista_productos)

#Nos creamos la array np_ganancias
np_ganancias = np_lista_precios * np_lista_ventas
print(np_ganancias)

# Al igual que en las listas podemos hacer uso de expresiones regulares para filtrar y quedarnos con lo que nos interesa. Por ejemplo supongamos que estamos interesados en quedarnos con los productos cuyas ganancias fueron superiores a 40.
productos  = np_lista_productos[np_ganancias > 40]
print(productos)

#Nos creamos dos arrays
array1 = np.array([1,2,3])
array2 = np.array([3,4,5])
#Sumamos las dos arrays
array_sum = array1 + array2
print(array_sum)

#Restamos ambas arrays
array_dif = 2*array1 - array2
print(array_dif)

#Dividimos ambas arrays
array_div = array2/array1
print(array_div)

#Nos creamos un array
paises = np.array(['USA', 'España', 'Croacia', 'Tailandia'])
#Accedemos al primer elemento
print(paises[0])

#Accedemos al último elemento
print(paises[-1])

#Accedemos al segundo y el tercer elemento
print(paises[1:3])

#Nos creamos nuestra primer array bidimensional
array_champions = np.array([['Manchester United', 3], ['Milan', 7], ['Barcelona', 5], ['Real Madrid', 12]])
print(array_champions)

#El atributo shape nos permite conocer la dimensión de un array
print(array_champions.shape)

#Accedemos al número de champions league ganadas por el milan
print(array_champions[1,1])

#Seleccionamos la segunda columna completa
print(array_champions[:,1])

#Seleccionamos la segunda fila completa
print(array_champions[1,:])

#Seleccinamos la segunda y la tercera columna
print(array_champions[1:3,:])

#También podemos sumar, restar,dividir y multiplicar los elementos de un array
array_numerica = np.array([[1,2], [3,4]])
#Sumamos uno a cada uno de los elementos
print(array_numerica + 1)

#Multiplicamos por dos todos los elementos 
print(array_numerica * 2)
