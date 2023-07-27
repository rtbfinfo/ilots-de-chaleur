

export const load = async ({fetch}) => {
    
        const fetchSecteur = async () => {
            const secteurRes = await fetch("https://gist.githubusercontent.com/Yheloww/c9d7a4fa9b5903ce80f6f1f51f6d738e/raw/db0542e118ed6f00b2d5017134c3048ce45876e6/liege_revenu_densite%2520(1).json")
            const secteurData = await secteurRes.json()
            return secteurData
        }

        return {
            secteur : fetchSecteur()
        }
}