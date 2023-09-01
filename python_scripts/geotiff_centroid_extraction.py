import pandas as pd 
import rasterio
import numpy as np
from rasterio.features import shapes
import geopandas as gpd

cities = ["liege", "namur", "brussel", "charleroi", "mons"]

def get_raster_data(raster_path : str):
    """ 
    open the geotiff file
    return a rasterio object
    """
    tiff = rasterio.open(raster_path)
    return tiff


def raster_to_centroids(city : str):
    """ 
    extract the centroids of the geotiff
    return a csv file
    """
    src = get_raster_data(raster_path = f"../assets/geotiff/{city}_geotif.tif")
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
    print("centroids to csv done")
    return csv_data

def loop_cities():
    """ 
    loop through all the cities and extract the centroids
    return a csv file
    """
    all_cities = pd.DataFrame()
    for city in cities:
        csv_data = raster_to_centroids(city)
        all_cities = pd.concat([all_cities, csv_data], ignore_index=True)
    
    all_cities.to_csv("../data/centroids.csv", index=False)
    print("all cities centroids done")