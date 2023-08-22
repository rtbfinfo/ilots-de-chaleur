import * as d3 from "d3"

export const load = async ({fetch}) => {
    
        const fetchAnnot = async () => {
            const secteurRes = await fetch("https://gist.githubusercontent.com/Yheloww/a1de676bc3d2b9546505cfcce034ea43/raw/3eb77b84f5cdc9f19d9937ca79dd6cbd32695638/annotations.json")
            const secteurData = await secteurRes.json()
            return secteurData
        }

        const fetchProv = async () => {
          const secteurRes = await fetch("https://gist.githubusercontent.com/Yheloww/27646b49316b9191e18d1c3f51b5b296/raw/5d71834c6f4d5dc3dd0652d8a6bfd48467a89fe4/belgium-with-regions_.json")
          const secteurData = await secteurRes.json()
          return secteurData
      }

        const fetchSecteurAll = async () => {
          const secteurRes = await fetch("https://gist.githubusercontent.com/Yheloww/805d8a72fd2ccb58bea81506d26d9851/raw/ffdf83bcb6d97fe3ad69340d80d5c44df4368e1c/secteur_every_city.json")
          const secteurData = await secteurRes.json()
          return secteurData
    }


        const fetchTemp = async () => {
            const tempRes = await fetch("https://gist.githubusercontent.com/Yheloww/ebcf7632eaa0d227cca089042a83ff86/raw/940803c2c67dd468ee82b19c3bc81d40ca99eb9f/every_city_infos.json")
            const tempData = await tempRes.json()
            return tempData
        }

        const fecthMar = async () => {
          const marRes = await d3.csv("https://gist.githubusercontent.com/Yheloww/51d8d8cceebdc6ac09a186e595f02add/raw/c0116bb68e9d3cc5428f25ab7cad8fb1d4bdbb71/mar_clean.csv")
          const marData = await marRes
          return marData
        }

        return {
            annot : fetchAnnot(),
            temp : fetchTemp(),
            mar : fecthMar(),
            provinces : fetchProv(),
            secteur_all : fetchSecteurAll()
        }
}