
# coding: utf-8

# # Matplotlib

#El primer paso para utlizar la librería es importarla.

#Importamos pyplot de matplotlib y numpy 
import matplotlib.pyplot as plt
import numpy as np

# Como toda librería de visualización el gráfico más básico que podemos mostrar es el gráfico de tipo línea.

#Nos creamos dos listas numéricas que representan año y población mundial en billones
#de habitantes
year = [1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,
 1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,
 1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,
 1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,
 2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,
 2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,
 2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,
 2041,2042,2043,2044,2045,2046,2047,2048,2049,2050,2051,2052,2053,
 2054,2055,2056,2057,2058,2059,2060,2061,2062,2063,2064,2065,2066,
 2067,2068,2069,2070,2071,2072,2073,2074,2075,2076,2077,2078,2079,
 2080,2081,2082,2083,2084,2085,2086,2087,2088,2089,2090,2091,2092,
 2093,2094,2095,2096,2097,2098,2099,2100]
    
poblacion = [2.53,2.57,2.62,2.67,2.71,2.76,2.81,2.86,2.92,2.97,
 3.03,3.08,3.14,3.2,3.26,3.33,3.4,3.47,3.54,3.62,3.69,3.77,3.84,
 3.92,4.0,4.07,4.15,4.22,4.3,4.37,4.45,4.53,4.61,4.69,4.78,4.86,
 4.95,5.05,5.14,5.23,5.32,5.41,5.49,5.58,5.66,5.74,5.82,5.9,5.98,
 6.05,6.13,6.2,6.28,6.36,6.44,6.51,6.59,6.67,6.75,6.83,6.92,7.0,
 7.08,7.16,7.24,7.32,7.4,7.48,7.56,7.64,7.72,7.79,7.87,7.94,8.01,
 8.08,8.15,8.22,8.29,8.36,8.42,8.49,8.56,8.62,8.68,8.74,8.8,8.86,
 8.92,8.98,9.04,9.09,9.15,9.2,9.26,9.31,9.36,9.41,9.46,9.5,9.55,
 9.6,9.64,9.68,9.73,9.77,9.81,9.85,9.88,9.92,9.96,9.99,10.03,
 10.06,10.09,10.13,10.16,10.19,10.22,10.25,10.28,10.31,10.33,
 10.36,10.38,10.41,10.43,10.46,10.48,10.5,10.52,10.55,10.57,
 10.59,10.61,10.63,10.65,10.66,10.68,10.7,10.72,10.73,10.75,
 10.77,10.78,10.79,10.81,10.82,10.83,10.84,10.85]

#Realizamos una representación gráfica de los datos
plt.plot(year, poblacion)
plt.show()


# A continuación vamos a trabajar con el fichero de datos gapminder.csv.

#Cargamos el dataset
import pandas as pd
gap_minder = pd.read_csv('gapminder.csv')
#Nos quedamos con las columnas life_exp y gdp_cap
esperanza_vida = gap_minder['life_exp']
renta = gap_minder['gdp_cap']
#Nos creamos un plot 
plt.plot(renta, esperanza_vida)
plt.show()

#Nos creamos nuestra primera visualización de tipo scatter
plt.scatter(renta, esperanza_vida)
plt.show()

#Nos quedamos con la población de las personas
poblacion = gap_minder['population']
#Nos creamos nuestro scatter
plt.scatter(poblacion, esperanza_vida)
plt.show()

#Filtramos y obtenemos la esperanza de vida de los países para el año 2007
gap_minder2007 = gap_minder[gap_minder.year == 2007]
gap_minder2007_lexp = gap_minder2007['life_exp']
#Representamos mediante un histograma la esperanza de vida en el año 2007
plt.hist(gap_minder2007_lexp)
plt.show()

#Mostramos la esperanza de vida en el año 2007 con 10 bins
plt.hist(gap_minder2007_lexp)
plt.show()
#Hacemos un cleaning
plt.clf()
#Mostramos la esperanza de vida con 20 bins
plt.hist(gap_minder2007_lexp, bins = 20)
plt.show()
#Hacemos un cleaning
plt.clf()

# Una de las utilidades de los histogramas es comparar, por ejemplo podemos comparar la distrbución de la esperanza de vida entre los años 2007 y 1950.

#Nos creamos una lista con la esperanza de vida para el año 1950
gap_minder1950_lexp = [28.8,55.23,43.08,30.02,62.48,69.12,66.8,50.94,
 37.48,68.0,38.22,40.41,53.82,47.62,50.92,59.6,
 31.98,39.03,39.42,38.52,68.75,35.46,38.09,54.74,
 44.0,50.64,40.72,39.14,42.11,57.21,40.48,61.21,
 59.42,66.87,70.78,34.81,45.93,48.36,41.89,45.26,
 34.48,35.93,34.08,66.55,67.41,37.0,30.0,67.5,43.15,
 65.86,42.02,33.61,32.5,37.58,41.91,60.96,64.03,72.49,
 37.37,37.47,44.87,45.32,66.91,65.39,65.94,58.53,63.03,
 43.16,42.27,50.06,47.45,55.56,55.93,42.14,38.48,42.72,
 36.68,36.26,48.46,33.68,40.54,50.99,50.79,42.24,59.16,
 42.87,31.29,36.32,41.72,36.16,72.13,69.39,42.31,37.44,
 36.32,72.67,37.58,43.44,55.19,62.65,43.9,47.75,61.31,
 59.82,64.28,52.72,61.05,40.0,46.47,39.88,37.28,58.0,
 30.33,60.4,64.36,65.57,32.98,45.01,64.94,57.59,38.64,
 41.41,71.86,69.62,45.88,58.5,41.22,50.85,38.6,59.1,
 44.6,43.58,39.98,69.18,68.44,66.07,55.09,40.41,43.16,
 32.55,42.04,48.45]
#Mostramos la esperanza de vida en 2007
plt.hist(gap_minder2007_lexp, bins = 15)
plt.show()
#Hacemos un cleaning
plt.clf()
#Mostramos la esperanza de vida en 1950
plt.hist(gap_minder1950_lexp, bins = 15)
plt.show()
#Hacemos un cleaning
plt.clf()

################### Añadimos nombre a los ejes y titulo ###############################
#Realizamos un gráfico de tipo scatter entre la renta per capita y la esperanza de vida
plt.scatter(renta, esperanza_vida)
#Le añadimos nombre al ejex, ejey y le ponemos un título
plt.xlabel('Renta')
plt.ylabel('Esperanza de vida')
plt.title('Renta vs Esperanza de vida')
plt.show()


################### Modificamos los valores de los ejes ############################
#Realizamos un gráfico de tipo scatter entre la renta per capita y la esperanza de vida y
plt.scatter(renta, esperanza_vida)
#Le añadimos nombre al ejex, ejey y le ponemos un título
plt.xlabel('Renta')
plt.ylabel('Esperanza de vida')
plt.title('Renta vs Esperanza de vida')
#Añadimos ticks a nuestro grafo
tick_val = [10000,20000, 30000, 40000, 50000]
tick_lab = ['10k', '20k', '30k', '40k', '50k']
plt.xticks(tick_val, tick_lab)
plt.show()

##################### Variamos la dimensión ###############################
#Nos creamos un array con el valor de la población para poder normalizar
poblacion_np = np.array(poblacion)
poblacion_np = poblacion_np / 1000000
#Realizamos un gráfico de tipo scatter entre la renta per capita y la esperanza de vida
#y tamaño en función de la población.
plt.scatter(renta, esperanza_vida, s = poblacion_np)
#Le añadimos nombre al ejex, ejey y le ponemos un título
plt.xlabel('Renta')
plt.ylabel('Esperanza de vida')
plt.title('Renta vs Esperanza de vida')
#Añadimos ticks a nuestro grafo
tick_val = [10000,20000, 30000, 40000, 50000]
tick_lab = ['10k', '20k', '30k', '40k', '50k']
plt.xticks(tick_val, tick_lab)
plt.show()

#################### Añadimos color #############################
#Nos creamos el diccionario para asignarle un color a cada continente
dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}

#Obtenemos las columna cont de gp
cont = gap_minder['cont']
#Ahora reemplazamos cada continente por su color mapeando la columna cont con nuestro diccionario dict
cont_color = cont.replace(dict)
#Nos creamos un array con el valor de la población para poder normalizar
poblacion_np = np.array(poblacion)
poblacion_np = poblacion_np / 1000000
#Realizamos un gráfico de tipo scatter entre la renta per capita y la esperanza de vida
#variando el tamañoo, color y transparencia
plt.scatter(renta, esperanza_vida, s = poblacion_np, c = cont_color, alpha = 0.8)
#Le añadimos nombre al ejex, ejey y le ponemos un título
plt.xlabel('Renta')
plt.ylabel('Esperanza de vida')
plt.title('Renta vs Esperanza de vida')
#Añadimos ticks a nuestro grafo
tick_val = [10000,20000, 30000, 40000, 50000]
tick_lab = ['10k', '20k', '30k', '40k', '50k']
plt.xticks(tick_val, tick_lab)
plt.show()


################ Añadimos texto ############################3
#Nos creamos el diccionario para asignarle un color a cada continente
dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}

#Obtenemos las columna cont de gp
cont = gap_minder['cont']
#Ahora reemplazamos cada continente por su color mapeando la columna cont con nuestro diccionario dict
cont_color = cont.replace(dict)
#Nos creamos un array con el valor de la población para poder normalizar
poblacion_np = np.array(poblacion)
poblacion_np = poblacion_np / 1000000
#Realizamos un gráfico de tipo scatter entre la renta per capita y la esperanza de vida
plt.scatter(renta, esperanza_vida, s = poblacion_np, c = cont_color, alpha = 0.8)
#Le añadimos nombre al ejex, ejey y le ponemos un título
plt.xlabel('Renta')
plt.ylabel('Esperanza de vida')
plt.title('Renta vs Esperanza de vida')
#Añadimos ticks a nuestro grafo
tick_val = [10000,20000, 30000, 40000, 50000]
tick_lab = ['10k', '20k', '30k', '40k', '50k']
plt.xticks(tick_val, tick_lab)
#Añadimos los nombres a determinados países
plt.text(1550, 71, 'India')
plt.text(28800, 80, 'Spain')
plt.show()

