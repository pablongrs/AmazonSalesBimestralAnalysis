## Descripción
Este proyecto tiene como objetivo realizar un proceso de Extracción, Transformación y Carga (ETL) y un Análisis Exploratorio de Datos (EDA) sobre un conjunto de datos de Amazon. El dataset incluye información sobre los ingresos de las diferentes categorías de venta de Amazon correspondientes al segundo trimestre de 2022. 
Este análisis se lleva a cabo utilizando herramientas de Python y SQL.
A través de este proyecto, se busca demostrar competencias en la gestión de datos, abarcando desde su procesamiento y transformación hasta su carga en una base de datos.


## Diccionario de datos

- ID de pedido (Order id): Identificador único de cada pedido
- Fecha (Date): Fecha en la que se realizó el pedido
- Estado del envío  (shipping_status)
- Cumplimiento (fulfilment)
- Canal de ventas (Sales Channel): Canal por el cual se realizó la venta
- Nivel de servicio del envio (ship_service_level)
- Estilo (Style)
- SKU: Número de referencia del producto
- Categoria (category): Categoría a la que pertenece el producto
- Tamaño (Size): Tamaño del producto
- Asin (Amazon Standard Identification Number)
- Cantidad (Quantity): Cantidad de productos en el pedido
- Importe (Amount)
- Ciudad del envio (Ship-city): Ciudad de destino del envío
- Estado del envio (Ship-state)
- País del envio (ship-country): País de destino del envío

Se comenzo realizando un Analisis preliminar de la calidad de los datos para comprenderlos y evaluar si son adecuados para un analisis mas profundo

Se comenzó con un análisis preliminar de la calidad de los datos para obtener una comprensión general de su estructura y características. Esta etapa permitió identificar posibles problemas, como datos faltantes o inconsistencias, y determinar si el conjunto de datos era adecuado para un análisis más profundo