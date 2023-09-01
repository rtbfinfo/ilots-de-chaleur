import geopandas as gdp
import pandas as pd

#TODO refactor function to make it do less things
def select_centroid():
    lst = pd.read_csv("../data/centroids.csv")
    gdf = gdp.GeoDataFrame(lst, geometry=gdp.points_from_xy(lst.centroid_lon, lst.centroid_lat), crs="EPSG:4326")
    geo_data = gdp.read_file('../data/densite_revenus_secteurs.geojson')
    # geo_data.crs = "EPSG:31370"
    geo_data = geo_data.to_crs("EPSG:4326")
    merged = gdp.sjoin(gdf,geo_data, predicate="within")
    print("spatial join done")
    final = merged[["city", "raster_value",
                "tx_sector_descr_fr", "REVENU_MOYEN", "REVENU_MEDIAN",
                    "NOMBRE_HAB","geometry","DENSITE_PAR_HECTARE",
                    "ms_area_ha","CD_SECTOR"]]
    finall = final.fillna(0).drop_duplicates()
    print("nan dropped")
    df2 = finall.groupby("tx_sector_descr_fr")["raster_value"].mean()
    print("temperaure mean done")
    everything = pd.merge(finall, df2, on='tx_sector_descr_fr')
    everything.to_file("../data/final_file.geojson", driver="GeoJSON")
    print("all done !")


