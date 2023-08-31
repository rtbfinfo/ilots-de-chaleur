# from geotiff_centroid_extraction import raster_to_centroids
# from revenu_densite import get_density_revenus_by_sector
import geopandas as gdp
import pandas as pd


def merge_LST_revenus():
    lst = pd.read_csv("centroids.csv")
    gdf = gdp.GeoDataFrame(lst, geometry=gdp.points_from_xy(lst.centroid_lon, lst.centroid_lat), crs="EPSG:4326")
    geo_data = gdp.read_file('../data/belgique_secteurs.geojson')
    geo_data = geo_data.to_crs("EPSG:4326")
    merged = gdp.sjoin(geo_data,gdf, predicate="within")
    print(merged.head())

merge_LST_revenus()

# TODO moyenne par secteur 