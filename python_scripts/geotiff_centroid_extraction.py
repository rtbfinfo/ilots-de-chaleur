import pandas as pd 
import rasterio
import numpy as np
from rasterio.features import shapes
import geopandas as gpd

raster_path = "../assets/geotiff/liege_geotif.tif"

# TODO loop through all geotiffs and merge them into one csv file

def get_raster_data(raster_path):
    tiff = rasterio.open(raster_path)
    return tiff


def raster_to_centroids():
    src = get_raster_data(raster_path)
    # Convert the first band to float32
    image = src.read(1).astype(np.float32)
    # Extract shapes and values
    results = (
        {'properties': {'raster_value': v}, 'geometry': s}
        for i, (s, v) in enumerate(shapes(image, transform=src.transform))
    )
    gdf = gpd.GeoDataFrame.from_features(results)
    # Explicitly set the CRS of the GeoDataFrame to the original CRS
    gdf.crs = "EPSG:3857"
    # Convert the GeoDataFrame to latitude/longitude
    gdf = gdf.to_crs("EPSG:4326")
    # Compute the centroids of the polygons
    centroids = gdf.geometry.centroid
    # Add the centroids as new columns in the GeoDataFrame
    gdf['centroid_lon'] = centroids.x
    gdf['centroid_lat'] = centroids.y
    # Select the columns to include in the CSV
    csv_data = gdf[['centroid_lon', 'centroid_lat', 'raster_value']]
    # Save the data to a CSV file
    csv_data.to_csv('centroids.csv', index=False)
    return csv_data


raster_to_centroids()