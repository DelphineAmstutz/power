import requests
from bs4 import BeautifulSoup
import time

"""
Script généré le 09/06/2025 par ChatGPT 4o à partir des prompts suivants :
Peux-tu écrire un script Python contenant une fonction chercheBNF qui prend en entrée une liste de chaines de caractères contenant des cotes d'ouvrages conservés à la BnF, et à chaque seconde, cherche la cote dans le catalogue général de la BnF, en récupérant l'identifiant ARK des 5 premiers résultats de cette recherche ?
[puis]
La récupération des identifiants des ouvrages ne fonctionne pas mais voici un exemple de page de résultat de recherche pour t'aider à la corriger.
[puis]
Ce script est erroné : ce qu’on doit extraire, ce sont les valeurs dans les attributs href des balises a situées dans les balises div ayant la classe notice-synthese. Peux-tu corriger le script ?
"""

def chercheBNF(cotes):
    base_url = "https://catalogue.bnf.fr/rechercher.do?motRecherche={}&critereRecherche=0"
    resultats = {}

    for cote in cotes:
        print(f"Recherche de la cote : {cote}")
        url = base_url.format(requests.utils.quote("\""+cote+"\""))
        print(url)
        response = requests.get(url)
        ark_ids = []

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            id = soup.find("p", {"id": "arkNot"})
            if id:
               print("id")
               print(id)
               # Nettoyage éventuel de paramètres dans l'URL
               ark = str(id).split("ark:/12148/")[1].split("<")[0]
               print(ark)
               ark_ids.append(f"ark:/12148/{ark}")
            else:
              notices = soup.find_all("div", class_="notice-synthese")

              for notice in notices[:5]:  # Limiter aux 5 premiers résultats
                lien = notice.find("a", href=True)
                if lien and "ark:/12148/" in lien['href']:
                    href = lien['href']
                    # Nettoyage éventuel de paramètres dans l'URL
                    ark = href.split("ark:/12148/")[1].split("?")[0]
                    ark_ids.append(f"ark:/12148/{ark}")
        else:
            print(f"Erreur HTTP pour la cote {cote} : {response.status_code}")

        resultats[cote] = ark_ids
        time.sleep(1)

    return resultats

# Exemple d'utilisation
if __name__ == "__main__":
    cotes = ["*E 194","Rés. *E 329 (5)","*E 2892","E 770"]
    """
    cotes = ["*E 808","Lf3 11","Ld39 110","Rés. R 1245","O2N-235","J 3628","Lb34 329 B","Rés. Lb36 32","Rés. L37 17","Lj22 2","Lb36 3752","*E3027","*E 3089(1)","Ye 1311","Lb36 1483","Rés. Ld6 8(2)","Lb36 3757","*E 3390","Rés. E 2676","IL 17342-17344","Rés. Lb36 2860","Rés. D 21280","Rés. L35 104-105","*E 942 (1)","M 14599","M 14600-14601","*E 2870","V 21807","4-LD10-11","Rés. 4° Le4 14","8 Le4 16","8° La4 12","Rés. Ld6 8","Rés. L35 80","Fol L35 84","Rés. Ld10 7","8° Lb36 700","Ye 5625","E 267","8<> Z 19713","*Ez 158","8° Ld4 160","Rés. Lb36 22a","R 1971","Rés. Oc 59 (1)","*E 4609-4610","Rés. Lb36 3492","Lb36 3246","Rés. Lb36 3246","4° Le4 38","Rés. J 1580","Le37 13","19046-19047","*E 194, *E 195","8° Ln27 20522","8° Lb36 1018","Fol Lm3 986","Rés. *E 244","8° Lb36 1424","*E 826","*E 2944","*E 3226","L ei7 40","*E 1019","Lb36 2709","L35 89","R 24401-24402","Rés. E 547","E 623-624"]
        
    cotes = ["Lb36 342",
"Lb36 3474",
"*E 808",
"R 24435",
"*E 805",
"Lf3 11",
"Lb36 2992",
"R 32958",
"Lb37 1395",
"Ln27 17410",
"Lb37 3556",
"Ld39 110",
"R 19908",
"Rés. R 1245",
"R 24461",
"*E 3766",
"R 6337",
"L45 20",
"On2 235A",
"Lb29 7",
"H 3269",
"J 11804",
"J 3628",
"D 21266",
"Lb34 329 B",
"Rés. Lb36 32",
"*E 611",
"Rés. L37 17",
"Lj22 2",
"Rés. Le4 19",
"Lb36 3752",
"*E 3884",
"*E3027",
"*E 3089(1)",
"Lb36 37",
"Ye 1086",
"Ye 1311",
"Lb36 1483",
"*E 3368",
"*E 3369",
"Rés. Ld6 8(2)",
"Lb36 3757",
"*E 3390",
"Rés. E 2676",
"IL 17342",
"Lb36 51 A",
"Z 16728",
"R 22150",
"Rés. Lb36 2860",
"Rés. D 21280",
"Rés. L35 104-105",
"L37 18",
"L37 19",
"*E 942 (1)",
"Lb36 3149",
"M 14599",
"M 14600-14601",
"*E 916",
"*E 2870 et J 13713.",
"*E 2870",
"V 21807",
"Lb36 2262",
"*E 693",
"Lf19 1",
"Lb35 666",
"La11 19A",
"D 5961",
"Rés. 4° Le4 14",
"8o Le4 16",
"X 3459",
"La4 12",
"Rés. Ld6 8",
"Rés. L35 80.",
"Fol. L35 83",
"Fol L35 84",
"Ld10 12",
"Rés. Ld10 7",
"Lf3 9",
"Lb36 2144",
"Lb36 700",
"*E 2671",
"Ye 1365",
"Ye 5625",
"E 267",
"Z 19713",
"*Ez 158",
"Ld4 160",
"Rés. Lb36 22a fol.",
"H 10947",
"*E 3255",
"Lb36 2864",
"R 1971",
"*E 1565",
"F 24331",
"Oc 407",
"Lb36 3660",
"Ye 1134",
"*E 926",
"*E 2928",
"*E 896",
"X 18784",
"Rés. Oc 59 (1)",
"*E 4609-4610",
"Rés. Lb36 3492",
"Lb36 3246",
"Rés. Lb36 3246",
"4° Le4 38",
"*E 2477",
"Rés. J 1580",
"J 21755",
"*E 142.",
"Ye 1107",
"E 3613",
"Le37 13",
"Lf3 10. A",
"*E 3570",
"R 24043",
"19046",
"Le4 40",
"Le3 8",
"Lf3 16",
"Lb36 31",
"E 2907",
"F 16141",
"*E 4759",
"*E 2089",
"Ln27 13551",
"*E 194, *E 195",
"Lb35 863",
"Fol Lb27 5",
"Ln27 20522",
"Lb36 1018",
"Fol Lm3 986",
"E 2890",
"Lb36 70.",
"Rés. *E 244",
"Lb36 3408",
"D2 107",
"*E 2922",
"*E 929",
"Lb36 1424",
"Q 3469",
"Q 3470",
"*E 826",
"Lb27 6",
"*E 2944",
"D 9014",
"*E 3371",
"Z 14338",
"Z 32368",
"*E 3226",
"Lb35 875",
"Lb35 860",
"G 3150",
"*E 3439",
"*E 3349",
"*E 1183",
"D 9607",
"E 5900",
"4° Lb36 27",
"G 32384",
"R 6447",
"Le4 32",
"L ei7 40",
"*E 1019",
"*E 960",
"G 32776",
"Lb36 2709",
"Lb36 2830",
"Lb36 2835",
"Lb36 2881",
"Lb36 2993",
"Ld4 154",
"Z 32984",
"L35 89",
"R 24401",
"E 703",
"L35 77",
"Rés. E 547",
"4° Lb36 3328",
"*E 3391",
"E 623-624"]
    """
    resultats = chercheBNF(cotes)
    print(resultats)
    """
    for cote, arks in resultats.items():
        print(f"{cote} : {arks}")
    """