

export const load = async ({fetch}) => {
    
        const fetchSecteur = async () => {
            const secteurRes = await fetch("https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/liege_revenu_densite%2520(1).json")
            const secteurData = await secteurRes.json()
            return secteurData
        }

        const fetchTemp = async () => {
            const tempRes = await fetch("https://gist.githubusercontent.com/Yheloww/8b84130f5e9bc0a5b51b9f4fb5b5f230/raw/cc1cf3c1f71ba17332190405c4d2f1ba0076dc6a/every_city.json")
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
      lst : "https://gist.githubusercontent.com/Yheloww/bba8f6cd07949116b34cdb6d94d07ac2/raw/fb5205b70519a670eec42fe7c5ccda5d96a5d3c0/liege_sel_centroid.json"
    },
    {
      name : "Charleroi",
      secteur : "https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/charleroi_revenu_densite%2520(1).json",
      lst : "https://gist.githubusercontent.com/Yheloww/bba8f6cd07949116b34cdb6d94d07ac2/raw/fb5205b70519a670eec42fe7c5ccda5d96a5d3c0/charleroi_sel_centroid.json"
    },
    {
      name : "Namur",
      secteur : "https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/namur_revenu_densite%2520(1).json",
      lst :"https://gist.githubusercontent.com/Yheloww/bba8f6cd07949116b34cdb6d94d07ac2/raw/fb5205b70519a670eec42fe7c5ccda5d96a5d3c0/namur_sel_centroid.json"
    },
    {
      name : "Mons",
      secteur : "https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/mons_revenu_densite%2520(1).json",
      lst : "https://gist.githubusercontent.com/Yheloww/bba8f6cd07949116b34cdb6d94d07ac2/raw/fb5205b70519a670eec42fe7c5ccda5d96a5d3c0/mons_sel_centroid.json"

    },
    {
      name : "Tournai",
      secteur : "https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/tournai_revenu_densite%2520(1).json",
      lst : "https://gist.githubusercontent.com/Yheloww/bba8f6cd07949116b34cdb6d94d07ac2/raw/fb5205b70519a670eec42fe7c5ccda5d96a5d3c0/tournai_sel_centroid.json"

    }
  ]