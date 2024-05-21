import rasterio
import numpy as np

# Cargar imágenes
band_files = [
    "Analisis_Satelital\Data\LC09_L2SP_008057_20240410_20240411_02_T1_SR_B1.TIF",
    "Analisis_Satelital\Data\LC09_L2SP_008057_20240410_20240411_02_T1_SR_B2.TIF",
    "Analisis_Satelital\Data\LC09_L2SP_008057_20240410_20240411_02_T1_SR_B3.TIF",
    "Analisis_Satelital\Data\LC09_L2SP_008057_20240410_20240411_02_T1_SR_B4.TIF",
    "Analisis_Satelital\Data\LC09_L2SP_008057_20240410_20240411_02_T1_SR_B5.TIF",
    "Analisis_Satelital\Data\LC09_L2SP_008057_20240410_20240411_02_T1_SR_B6.TIF",
    "Analisis_Satelital\Data\LC09_L2SP_008057_20240410_20240411_02_T1_SR_B7.TIF",
    "Analisis_Satelital\Data\LC09_L2SP_008057_20240410_20240411_02_T1_ST_B10.TIF",
]


# Lectura de bandas
bands_data = []
for band_file in band_files:
    with rasterio.open(band_file) as src:
        bands_data.append(src.read(1))

# Calcular NDVI (ejemplo de índice)
red_band = bands_data[3]  # Ajusta el índice de la banda según tus datos
nir_band = bands_data[4]  # Ajusta el índice de la banda según tus datos
ndvi = (nir_band - red_band) / (nir_band + red_band)

# Segmentación y clasificación (ejemplo)
urban_areas = np.where(ndvi > 0.7, 1, 0)  # Ajusta el umbral según tus datos

# Guardar resultados
with rasterio.open("urban_areas.tif", "w", **src.profile) as dst:
    dst.write(urban_areas.astype(rasterio.uint8), 1)
