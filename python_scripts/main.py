from geotiff_centroid_extraction import loop_cities
from revenu_densite import get_density_revenus_by_sector
from merge import select_centroid

# ! before running you need a /data folder with the following files:
# ! data_par_secteur.xlsx
# ! revenu_par_secteur.xlsx
# ! belgique_secteurs.geojson 
# ! links to download in the README.md

# TODO fix user warning with projections

def main():
    # extract centroid from geotiff
    loop_cities()
    # merge revenu, densite and verdure into one geodataframe
    get_density_revenus_by_sector()
    # select the centroid that are in the sectors
    # then merge them with density, revenu and verdure
    select_centroid()
    print("data saved to data/final_file.geojson")
    print("sectors saved to data/city_sectors.geojson")

if __name__ == "__main__":
    main()