import pandas as pd 
import geopandas as gpd


def merge_occupation_datas():
    list_cities = ["liege","bxl","namur","charleroi","mons"]
    all_cities = gpd.GeoDataFrame()
    for city in list_cities:
        df = gpd.read_file(f"../assets/occupation du sol/{city}_perc.geojson")
        if city == "bxl":
            df = df.rename(columns= {'HISTO_0' : 'HISTO_NODATA'})
        df["city"] = city
        all_cities = pd.concat([all_cities,df])
    return all_cities

def get_verdure_percentages():
    all_cities = merge_occupation_datas()

    new_df = all_cities[["cd_sector", "tx_sector_descr_fr", "HISTO_NODATA","HISTO_1","HISTO_2", "geometry","city"]]   
    new_df["total"] = new_df["HISTO_NODATA"] + new_df["HISTO_1"] + new_df["HISTO_2"]
    new_df['perc_herbe'] = new_df["HISTO_1"] / new_df["total"] * 100
    new_df['perc_arbre'] = new_df["HISTO_2"] / new_df["total"] * 100
    new_df['perc_ver'] = new_df["perc_arbre"] + new_df['perc_herbe']
    new_df["CD_SECTOR"] = new_df["cd_sector"]
    
    final = new_df[["CD_SECTOR", "perc_herbe", "perc_arbre", "perc_ver","city"]]
    return final

get_verdure_percentages()