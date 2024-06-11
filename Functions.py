import pandas as pd

#Devuelve un dataframe con tipos de datos y nulos del dataset completo
def data_characteristics(dataframe):
    lista =[]
    
    for columna in dataframe.columns:
        cant_nulos = dataframe[columna].isnull().sum()
        lista.append({'column':columna,
                      'type data':dataframe[columna].dtypes,
                      'total nulls':cant_nulos,
                      'percentage':f'{round((cant_nulos/len(dataframe))*100,2)}%' })
        
    caracteristicas = pd.DataFrame(lista)    
    return caracteristicas


def informe_data(df):
    print(f'--Dimensiones del DataFrame--\nFilas: {df.shape[0]}\nColumnas: {df.shape[1]}')
    print(f'Cantidad de datos: {df[df.isna() == False].count().sum()}\n')
 
 
     
#-------------------   funciones para analisis preliminar de datos  -----------------------
def info_basica(data):
     print(f'- Cantidad de datos no nulos: {data.notnull().sum()}')
     print(f'- Numero de datos nulos: {data.isna().sum()}')  
     print(f'- Cantidad de valores únicos: {data.nunique()}\n')
     
def distribucion_de_frecuencia(data):
    print(f'  DISTRIBUCION DE FRECUENCIAS (TOP 3) {data.value_counts().nlargest(3)}\n')
    
     
#Devuelve las caracteristicas de los datos de la columna especificada
def informe_columna(df: None|pd.DataFrame, columna: None|str) -> None:
    data = df[columna]
    print(f'INFORME PRELIMINAR SOBRE LA COLUMNA: {columna}\n')
       
    if data.dtype == 'object':
        info_basica(data)# muestra la cantidad de nuelos y unicos de la columna
         
        if len(data.unique()) > 5:
            print(f'VALORES UNICOS EN LA COLUMNA (TOP 5)  \n{data.unique()[0:5]}\n')
        else:
            print(f'--Valores únicos en la columna--\n{data.unique()}\n')

        print(f'FRECUENCIAS DE LA COLUMNA   \n- Valor modal: {data.mode().iloc[0]}\n- Frecuencia acumulada: {data.value_counts().max()}\n')
        #Esta funcion imprime los 3 valores con mas frecuencia de la columna
        distribucion_de_frecuencia(data)
#----------------------------------------------------------------------------------------------------------------------------------------------  
#----------------------------------------------------------------------------------------------------------------------------------------------     
    elif data.dtype == 'datetime64[ns]':
        info_basica(data)# muestra la cantidad de nuelos y unicos de la columna
        
        print(f'  VALORES UNICOS EN LA COLUMNA  \nEjemplo: {data.dt.strftime("%Y-%m-%d").unique()[0:3]}  -----> Desde {list(data.dt.strftime("%Y-%m-%d").unique())[0]}  Hasta {list(data.dt.strftime("%Y-%m-%d").unique())[-1]}\n')
        print(f'  FRECUENCIAS DE LA COLUMNA   \nValor modal: {data.mode()[0]}\nFrecuencia acumulada: {data.value_counts().max()}\n')
        #Esta funcion imprime los 3 valores con mas frecuencia de la columna
        distribucion_de_frecuencia(data)
#----------------------------------------------------------------------------------------------------------------------------------------------  
#----------------------------------------------------------------------------------------------------------------------------------------------         
    else:
        print(f'- Numero de datos nulos: {data.isna().sum()}\n')
        if data.dtype in ['int64', 'float64', 'int32']:
           if not data.isna().any():
             print(f'cantidad de datos no nulos: {data.notnull().sum()}')
             print(f'  ESTADISTICOS PRINCIPALES  \nMedia: {round(data.mean(),2)}\nDesviacion Estandar: {round(data.std(),2)}\nPrimer cuartil: {data.quantile(0.25)}\nMediana: {data.median()}\nTercer cuartil: {data.quantile(0.75)}\n')
             print(f'--Valores extremos--\nValor máximo: {data.max()}\nValor mínimo: {data.min()}\n')
             distribucion_de_frecuencia(data)
           else:
              print('No se pueden calcular estadísticas principales para esta columna debido a valores nulos o no numéricos')
    print('-'*120)
    print('-'*120)
    
    

    