
# coding: utf-8

################################## Tuplas ######################################

#Nos creamos nuestra primera tupla
mitupla = ('Madrid', 'Getafe', 'Alcorcón')
print(mitupla)

#Nos creamos tupla sin hacer uso de los paréntesis
mitupla2 = 'Madrid', 'Getafe', 'Alcorcón'
print(mitupla2)

#Accedemos al primer elemento de la tupla
print(mitupla[0])

#Convertimos una tupla en lista
lista_CM = list(mitupla)
print(lista_CM)

#Convertimos una lista en tupla
tupla_CM = tuple(lista_CM)
print(tupla_CM)

#Vemos si el barrio de Vayecas está en nuestra lista
print('Vayecas' in tupla_CM)

#Vemos el número de veces que aparece la ciudad de Madrid en nuestra tupla
print(tupla_CM.count('Madrid'))

# El método len() nos permite averiguar la longitud de una tupla.
print(len(tupla_CM))

#Nos creamos una tupla unitaria haciendo uso de los paréntesis
tupla_unitaria = ('Madrid',)
print(len(tupla_unitaria))
#Nos creamos una tupla unitaria sin hacer uso de los paréntesis
tupla_unitaria = 'Madrid',
print(len(tupla_unitaria))

#Desempaquetamos nuestras tuplas
tupla_capitales = ('Roma', 'París', 'Amsterdam')
Italia, Francia, Holanda = tupla_capitales
print(Italia)
print(Francia)
print(Holanda)


################################# Diccionarios #################################

#Nos creamos un diccionario 
paises_dic = {'España' : 'madrid', 'Francia': 'París', 'Italia': 'Roma'}
print(paises_dic)

#Nos creamos dos listas
list_paises = ['España', 'Francia', 'Italia']
list_capitales = ['Madrid', 'París', 'Roma']

#Accedemos a la capita de Francia
print(list_capitales[list_paises.index('Francia')])

#Accedemos al elemento que corresponde a la clave Francia
print(paises_dic['Francia'])

#Agregamos un nuevo elemento al diccionario
paises_dic['Portugal'] = 'Lisboa'
print(paises_dic)

#Sobreescribimos el nombre de la capital de España
paises_dic['España'] = 'Madrid'
print(paises_dic)

#Eliminamos la información respecto a Italia
del(paises_dic['Italia'])
print(paises_dic)

#Nos creamos un diccionario donde ahora las claves son numéricas
DreamTeam_USA = {9: 'Michael Jordan', 8: 'Scottie Pippen', 7: 'Larry Bird', 15: 'Magic Johnson', 11: 'Karl Malone'}
print(DreamTeam_USA)

#Almacenamos dentro de un diccionario una tupla
MichaelJordan_dic = {'Nombre': 'Michael', 'Equipo': 'Chicago', 'anillos': (1991, 1992, 1993, 1996,1997,1988)}
print(MichaelJordan_dic)

#Almacenamos dentro de un diccionario otro diccionario
MichaelJordan_dic = {'Nombre': 'Michael', 'Equipo': 'Chicago', 'anillos': {'Temporadas':                                                                            (1991, 1992, 1993, 1996,1997,1988)}}
print(MichaelJordan_dic)

#Accedemos a temporadas 
print(MichaelJordan_dic['anillos']['Temporadas'])

#Mostramos las claves
print(MichaelJordan_dic.keys())

#Mostramos los valores
print(MichaelJordan_dic.values())

# El método len nos permite obtener la longitud de un diccionario.
print(len(MichaelJordan_dic))

#Comprobamos si la clave nombre se encuentra en nuestro diccionario
print('Nombre' in MichaelJordan_dic)

