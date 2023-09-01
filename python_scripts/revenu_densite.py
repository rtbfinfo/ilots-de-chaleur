import pandas as pd
import geopandas as gpd 

density_path = "../data/densite_par_secteur.xlsx"
revenu_path = "../data/revenu_par_secteur.xlsx"
secteurs_path = "../data/belgique_secteurs.geojson"

city_codes =  ["62063","52011","53053", "92094"]
bruxelles_codes = ["04000","21000","21001","21002","21003","21004","21005","21006","21007",
"21008","21009","21010","21011","21012","21013","21014","21015","21016"
"21017","21018","21019"]

# TODO: optimize opening of files (density and revenu)

def get_city_codes(secteurs_path):
    """ 
    select only the city sectors we want to keep using the nis code of the cities
    return a geodataframe 
    """
    secteurs = gpd.read_file(secteurs_path)
    secteurs.crs = "EPSG:31370"
    secteurs = secteurs.to_crs("EPSG:4326")  
    bruxelles_code = secteurs[secteurs["cd_munty_refnis"].isin(bruxelles_codes)]
    other_cities_code = secteurs[secteurs["cd_munty_refnis"].isin(city_codes)]
    all_secteurs = pd.concat([bruxelles_code, other_cities_code], ignore_index=True)
    all_secteurs.to_file("../data/cities_secteurs.geojson", driver='GeoJSON')
    return all_secteurs
 
def get_density(density_path):
    """ 
    Open the density data and change some columns names
    return a dataframe 
    """
    density = pd.read_excel(density_path)
    new_densite = density[["CD_SECTOR","TOTAL","OPPERVLAKKTE IN HM²","CD_REFNIS"]]
    new_densite = new_densite.rename(columns = {'TOTAL':'NOMBRE_HAB'})
    new_densite = new_densite.rename(columns = {'OPPERVLAKKTE IN HM²':'DENSITE_PAR_HECTARE'})
    print("got density")
    return new_densite

   
def get_revenu():
    """ 
    Open the revenu data and change some columns names
    return a dataframe
    """
    revenu = pd.read_excel("../data/revenu_par_secteur.xlsx")
    new_revenu = revenu[["CD_SECTOR","MS_AVG_TOT_NET_TAXABLE_INC","MS_MEDIAN_NET_TAXABLE_INC"]]
    new_revenu = new_revenu.rename(columns = {'MS_AVG_TOT_NET_TAXABLE_INC':'REVENU_MOYEN'})
    new_revenu = new_revenu.rename(columns = {'MS_MEDIAN_NET_TAXABLE_INC':'REVENU_MEDIAN'})
    print("got revenu")
    return new_revenu

def merge_occupation_datas():
    """ 
    Open the "occupation_du_sol" data and merge them into one dataframe 
    return a dataframe
    """
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
    """ 
    Open the "occupation_du_sol" data and compute the percentage of vegetation(high and low type)
    return a dataframe
    """
    all_cities = merge_occupation_datas()

    new_df = all_cities[["cd_sector", "tx_sector_descr_fr", "HISTO_NODATA","HISTO_1","HISTO_2", "geometry","city"]]   
    new_df["total"] = new_df["HISTO_NODATA"] + new_df["HISTO_1"] + new_df["HISTO_2"]
    new_df['perc_herbe'] = new_df["HISTO_1"] / new_df["total"] * 100
    new_df['perc_arbre'] = new_df["HISTO_2"] / new_df["total"] * 100
    new_df['perc_ver'] = new_df["perc_arbre"] + new_df['perc_herbe']
    new_df["CD_SECTOR"] = new_df["cd_sector"]
    
    final = new_df[["CD_SECTOR", "perc_herbe", "perc_arbre", "perc_ver","city"]]
    print("got verdure") 
    return final


def merge_density_revenus_verdure():
    """ 
    merge every data sources into one dataframe using the sector code as key
    return a dataframe
    """
    density = get_density(density_path)
    revenu = get_revenu()
    verdure = get_verdure_percentages()
    merged_data = revenu.merge(density, on='CD_SECTOR').drop_duplicates(subset="CD_SECTOR")
    merged_everything = merged_data.merge(verdure, on='CD_SECTOR').drop_duplicates(subset="CD_SECTOR")
    print("merged everything")
    return merged_everything


def get_density_revenus_by_sector():
    """ 
    merge the dataframe with infos with the geodataframe with the sectors
    return a geodataframe
    """
    secteurs = get_city_codes(secteurs_path)
    merged_data = merge_density_revenus_verdure()
    secteurs = secteurs.rename(columns = {'cd_sector':'CD_SECTOR'})
    everything = secteurs.merge(merged_data, on='CD_SECTOR').drop_duplicates(subset="CD_SECTOR")
    everything.to_file("../data/densite_revenus_secteurs.geojson", driver='GeoJSON')
    print("got density revenus verdure by sector")
    return everything


