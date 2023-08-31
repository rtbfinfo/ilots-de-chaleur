import pandas as pd
import geopandas as gpd 

density_path = "../data/densite_par_secteur.xlsx"
revenu_path = "../data/revenu_par_secteur.xlsx"
secteurs_path = "../data/belgique_secteurs.geojson"

city_codes =  ["62063","52011","53053", "92094"]
bruxelles_codes = ["04000","21000","21001","21002","21003","21004","21005","21006","21007",
"21008","21009","21010","21011","21012","21013","21014","21015","21016"
"21017","21018","21019"]
    
def get_city_codes(secteurs_path):
    secteurs = gpd.read_file(secteurs_path)
    secteurs.crs = "EPSG:31370"
    secteurs = secteurs.to_crs("EPSG:4326")  
    bruxelles_code = secteurs[secteurs["cd_munty_refnis"].isin(bruxelles_codes)]
    other_cities_code = secteurs[secteurs["cd_munty_refnis"].isin(city_codes)]
    all_secteurs = pd.concat([bruxelles_code, other_cities_code], ignore_index=True)
    return all_secteurs
 
def get_density(density_path):
    density = pd.read_excel(density_path)
    new_densite = density[["CD_SECTOR","TOTAL","OPPERVLAKKTE IN HM²","CD_REFNIS"]]
    new_densite = new_densite.rename(columns = {'TOTAL':'NOMBRE_HAB'})
    new_densite = new_densite.rename(columns = {'OPPERVLAKKTE IN HM²':'DENSITE_PAR_HECTARE'})
    return new_densite
    
def get_revenu(revenu_path):
    revenu = pd.read_excel("../data/revenu_par_secteur.xlsx")
    new_revenu = revenu[["CD_SECTOR","MS_AVG_TOT_NET_TAXABLE_INC","MS_MEDIAN_NET_TAXABLE_INC"]]
    new_revenu = new_revenu.rename(columns = {'MS_AVG_TOT_NET_TAXABLE_INC':'REVENU_MOYEN'})
    new_revenu = new_revenu.rename(columns = {'MS_MEDIAN_NET_TAXABLE_INC':'REVENU_MEDIAN'})
    return new_revenu

def merge_density_revenus():
    density = get_density(density_path)
    revenu = get_revenu(revenu_path)
    merged_data = revenu.merge(density, on='CD_SECTOR').drop_duplicates(subset="CD_SECTOR")
    return merged_data

def get_density_revenus_by_sector():
    secteurs = get_city_codes(secteurs_path)
    merged_data = merge_density_revenus()
    secteurs = secteurs.rename(columns = {'cd_sector':'CD_SECTOR'})
    everything = secteurs.merge(merged_data, on='CD_SECTOR').drop_duplicates(subset="CD_SECTOR")
    print(everything.shape)
    print(everything.head())
    everything.to_file("../data/densite_revenus_secteurs.geojson", driver='GeoJSON')
    return everything
get_density_revenus_by_sector()