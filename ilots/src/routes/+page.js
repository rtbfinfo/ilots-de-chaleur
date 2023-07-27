

export const load = async ({fetch}) => {
    
        const fetchSecteur = async () => {
            const secteurRes = await fetch("https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/liege_revenu_densite%2520(1).json")
            const secteurData = await secteurRes.json()
            return secteurData
        }

        const fetchTemp = async () => {
            const tempRes = await fetch("https://gist.githubusercontent.com/Yheloww/4feb324e218221eccf5a9b0e57431c30/raw/819fc593992b9df0b4a43f1f48988048b60996f2/liege_sel_centroid.json")
            const tempData = await tempRes.json()
            return tempData
        }

        return {
            secteur : fetchSecteur(),
            temp : fetchTemp(),
        }
}



let cities_object = [
    {
      name : "Liege",
      secteur : "https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/liege_revenu_densite%2520(1).json",
      lst : "https://gist.githubusercontent.com/Yheloww/4feb324e218221eccf5a9b0e57431c30/raw/819fc593992b9df0b4a43f1f48988048b60996f2/liege_sel_centroid.json"
    },
    {
      name : "Charleroi",
      secteur : "https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/charleroi_revenu_densite%2520(1).json",
      lst : "https://gist.githubusercontent.com/Yheloww/4feb324e218221eccf5a9b0e57431c30/raw/819fc593992b9df0b4a43f1f48988048b60996f2/charleroi_centroid.json"
    },
    {
      name : "Namur",
      secteur : "https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/namur_revenu_densite%2520(1).json",
      lst :"https://gist.githubusercontent.com/Yheloww/4feb324e218221eccf5a9b0e57431c30/raw/819fc593992b9df0b4a43f1f48988048b60996f2/namur_sel_centroid.json"
    },
    {
      name : "Mons",
      secteur : "https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/mons_revenu_densite%2520(1).json",
      lst : "https://gist.githubusercontent.com/Yheloww/4feb324e218221eccf5a9b0e57431c30/raw/819fc593992b9df0b4a43f1f48988048b60996f2/mons_sel_centroid.json"

    },
    {
      name : "Tournai",
      secteur : "https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/tournai_revenu_densite%2520(1).json",
      lst : "https://gist.githubusercontent.com/Yheloww/4feb324e218221eccf5a9b0e57431c30/raw/819fc593992b9df0b4a43f1f48988048b60996f2/tournai_sel_centroid.json"

    }
  ]