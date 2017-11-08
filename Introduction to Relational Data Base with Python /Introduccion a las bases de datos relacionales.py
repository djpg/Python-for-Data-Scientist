#-*-coding: utf-8 -*-

################################ Creando un motor de bases de datos en Python ######################################

#Importamos create_engine
from sqlalchemy import create_engine
#Creamos la conexión
engine = create_engine('sqlite:///Chinook.sqlite')

#Mostramos las diferentes tablas que componen nuestra base de datos
tables = engine.table_names()
print(tables)


########################################## Primera consulta SQL ####################################################

#Importamos paquetes
from sqlalchemy import create_engine
import pandas as pd
#Creamos el motor de conexión 
engine = create_engine('sqlite:///Chinook.sqlite')
#Conectamos con la base de datos
con = engine.connect()
#Realizamos nuestra primera consulta
rs = engine.execute('SELECT * FROM Album')
#Salvamos los resulados como un DataFrame
df = pd.DataFrame(rs.fetchall())
#Cerramos la conexión a nuestra base de datos
con.close()
#Mostramos las 5 primeras filas de nuestra consulta
print(df.head())


with engine.connect() as con:
    rs = engine.execute('SELECT Lastname, Title FROM Employee')
    df = pd.DataFrame(rs.fetchmany(size = 3))
    df.columns = rs.keys()

print(len(df))
print(df.head())


###################################################### WHERE ###################################################################

with engine.connect() as con:
    rs = engine.execute('SELECT * FROM Employee WHERE EmployeeId >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

print(df.shape)    
print(df.head())


###################################################### ORDER BY ################################################################

with engine.connect() as con:
    rs = engine.execute('SELECT * FROM Employee ORDER BY BirthDate')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

print(df.head())


########################################## Realizando consultas SQL directamente con Pandas ########################################

#Importamos pandas
from sqlalchemy import create_engine
import pandas as pd
#Nos creamos el motor de consulta
engine = create_engine('sqlite:///Chinook.sqlite')
#Realizamos la consulta a través de pandas
df = pd.read_sql_query('SELECT * FROM Album', engine)
print(df.head())


# A continuación vamos a proceder a realizar una consulta un poco más compleja haciendo uso de pandas.

#Importamos las librerías necesarias
from sqlalchemy import create_engine
import pandas as pd
#Nos creamos el motor 
engine = create_engine('sqlite:///Chinook.sqlite')
#Realizamos la consulta SQL
df = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY Birthdate', engine)
print(df.head())


########################################################## INNER JOIN ####################################################################
#Importamos las librerías
import pandas as pd
from sqlalchemy import create_engine
#Creamos el motor
engine = create_engine('sqlite:///Chinook.sqlite')
#Mostramos las tablas
print(engine.table_names())
#Hacemos el InnerJoin
df = pd.read_sql_query('SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistId == Artist.ArtistID', engine)
print(df.head())
