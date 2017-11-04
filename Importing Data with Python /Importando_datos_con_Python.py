# coding: utf-8

################################################### Explorando nuestro directorio ###################################################

#Python cuenta con el comando !ls, que nos muestra todos los ficheros que tenemos en nuestro espacio de trabajo.
!ls


################################################# Importando ficheros de texto ########################################################

# Nos creamos una conexión al fichero
file = open('moby_dick.txt', mode = 'r')
#Vemos el contenido del fichero
print(file.read())

#Cerramos el fichero
file.close()

#Comprobamos que la conexión ha sido cerrada
print(file.closed)


#Nos creamos la conexión al fichero y imprimimos las 4 primeras líneas
with open('moby_dick.txt', mode = 'r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())


########################################################### Importando datos con Numpy ###############################################################

#Importamos la librería Numpy y matplotlib
import numpy as np
import matplotlib.pyplot as plt
#Cargamos nuestro fichero 
file = np.loadtxt('mnist_kaggle_some_rows.csv', delimiter = ',')
#Mostramos el tipo de dato que es file
print(type(file))

#Seleccionamos y reescalamos ciertas filas y columnas
im = file[21,1:]
im_sq = np.reshape(im, (28,28))
#Mostramos el resultado 
plt.imshow(im_sq, cmap = 'Greys', interpolation = 'nearest')
plt.show()


#Cargamos nuestro conjunto de datos haciendo uso de dtype
file = np.loadtxt('seaslug.txt', delimiter = '\t', dtype = 'str')
#Imprimimos la segunda fila
print(file[1])

#Cargamos nuestros datos como float
file = np.loadtxt('seaslug.txt', delimiter = '\t', dtype = 'float', skiprows = 1)
print(file[1:3])

#Cargamos nuestro fichero mixto
file = np.genfromtxt('titanic_sub.csv', delimiter = ',', names = True,
                    dtype = None)
print(file[0:3])



#Cargamos nuestro fichero con la función recfromcsv()
file = np.recfromcsv('titanic_sub.csv')
print(file[0:3])


###################################################### Importando datos con Pandas ####################################################################

#Importamos Pandas
import pandas as pd
#Cargamos nuestro conjunto de datos 
df = pd.read_csv('titanic_sub.csv')
#Mostramos las 5 primeras filas
print(df.head())

#Importamos como DataFrame haciendo uso de pandas 
df = pd.read_csv('mnist_kaggle_some_rows.csv', header = None, nrows = 5)
print(df.head())

#Ahora convertimos a numpyarray
df_np = df.values
print(df_np)


############################################ Introducción a la librería os ###########################################################

#Importamos la librería os
import os
#Accedemos a nuestro espacio trabajo
wd = os.getcwd()
#Vemos los ficheros en nuestro espacion de trabajo
os.listdir(wd)


########################################## Guardando y Cargando Ficheros pickled #########################################################################

#Importamos la librería pickle 
import pickle 
#Escribimos un diccionario a un archivo pkl
mydict = {'a': 1, 'b': 2, 'c': 3}
output = open('myfile.pkl', 'wb')
pickle.dump(mydict, output)
output.close()
#Realizamos ahora la lectura de nuestro archivo pickle
with open('myfile.pkl', 'rb') as file:
    d = pickle.load(file)

print(d)


################################################# Importando ficheros excel ####################################################################

#Importamos pandas
import pandas as pd
#Cargamos nuestro hoja de cálculo
xl = pd.ExcelFile('battledeath.xlsx')
#Mostramos las hojas que tiene
print(xl.sheet_names)

#Cargamos la hoja 2002
df1 = xl.parse('2002')
#Mostramos las 5 primeras filas
print(df1.head())


#Accedemos a la primera hoja (2002)
df2 = xl.parse(0)
#Mostramos las 5 primeras filas
print(df2.head())


#Importamos la hoja 2002
df1 = xl.parse(0,names = ['Country', 'AAM due to war (2002)'], skiprows = 0)
#Mostramos las 5 primeras filas
print(df1.head())


#Importamos la hoja 2002 haciendo uso de parámetros adicionales
df1 = xl.parse('2002', names = ['Country'], skiprows = 0, parse_cols = [0])
print(df1.head())


#################################################################### Importando ficheros SAS ##################################################################

#Importamos el paquete
from sas7bdat import SAS7BDAT
#Almacenamos el contenido de nuestro fichero en un DataFrame
with SAS7BDAT('sales.sas7bdat') as file: 
    df_sas = file.to_data_frame()
print(df_sas.head())


#################################################################### Importando ficheros dta ##################################################################

#Importamos pandas
import pandas as pd
#Importamos los datos 
df_disarea = pd.read_stata('disarea.dta')
print(df_disarea.head())


#################################################################### Importando ficheros HDF5 #################################################################

#Importamos las librerías necesarias
import numpy as np
import h5py
#Cargamos el fichero en modo lectura
file = h5py.File('L-L1_LOSC_4_V1-1126259446-32.hdf5', 'r')
print(type(file))

#Imprimimos las claves
for key in file.keys():
    print(key)


#Accedemos a la información de la clave strain
group = file['strain']
type(group)

#Imprimimos las claves de group
for key in group.keys():
    print(key)

#Accedemos al valor de los datos
strain = file['strain']['Strain'].value
print(type(strain))
np.shape(strain)

#Visualizamos la información del fichero

#Importamos las librería matplotlib
import matplotlib.pyplot as plt
#Realizamos el gráfico
num_muestras = 1000
time = np.arange(0,1,1/num_muestras)
#Seleccionamos las 1000 primeras muestras de strain
plt.plot(time, strain[:num_muestras])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()


###################################################################### Importando ficheros Matlab #######################################################################

#Importamos el paquete scipy.io
import scipy.io
#Leemos el fichero
file = scipy.io.loadmat('ja_data2.mat')
print(type(file))

#Mostramos las claves del fichero
print(file.keys())

#Vemos el tipo de una de las claves
print(type(file['CYratioCyt']))
print(np.shape(file['CYratioCyt']))

