#Autenticar Google Earth Engine en el entorno de Python

import ee
ee.Authenticate()
ee.Initialize()

#Usar Google Earth Engine para obtener imágenes de Landsat 8:
# Seleccionar imágenes de Landsat 8
collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR') \
              .filterDate('2022-01-01', '2022-12-31') \
              .filterBounds(ee.Geometry.Point([-74.08175, 4.60971]))  # Coordenadas de Bogotá

# Seleccionar una imagen
image = collection.median()

# Descargar la imagen
url = image.getDownloadURL({
    'scale': 30,
    'crs': 'EPSG:4326'
})

print('Download URL:', url)

