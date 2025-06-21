import requests
from bs4 import BeautifulSoup
from typing import List, Dict

"""
Script généré le 08/06/2025 par ChatGPT 4o à partir des prompts suivants :
Peux-tu écrire un script en Python avec une fonction scrapingBNF qui prend en entrée une liste d'identifiants d'ouvrages dans le catalogue général de la bibliothèque générale de France et qui récupère, dans le catalogue, les informations de titre, nom et identifiant BNF de l'auteur, nom de l'éditeur, lieu et année d'édition, et lien Gallica des ouvrages, pour renvoyer un tableau d'objets contenant toutes ces informations ?
[puis, le 09/06/2025, en réponse à Souhaitez-vous que je rende le script plus robuste (ex. : gestion d’exceptions, parsing plus précis de la date ou éditeur) ?]
Oui, pourrais-tu corriger l'extraction des informations, en utilisant le fichier ci-joint d'exemple de fiche du catalogue de la Bibliothèque nationale de France ? [fichier : https://catalogue.bnf.fr/ark:/12148/cb36119402j]
[puis]
Peux-tu améliorer le script pour récupérer le nom d'auteur et son identifiant Gallica depuis le lien contenu dans la balise p qui a pour identifiant auteur ?
"""

def scrapingBNF(identifiants: List[str]) -> List[Dict[str, str]]:
    base_url = "https://catalogue.bnf.fr/ark:/12148/"
    results = []

    for ident in identifiants:
        url = base_url + ident
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Erreur d'accès pour l'identifiant {ident}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extraction des balises meta
        meta = {m.get("name"): m.get("content") for m in soup.find_all("meta") if m.get("name") and m.get("content")}

        titre = meta.get("DC.title", "")
        contributeur = meta.get("DC.contributor", "")

        # Extraction de l'auteur et de son identifiant via la balise <p id="auteur">
        auteur_nom = ""
        auteur_id = ""
        auteur_tag = soup.find("p", id="auteur")
        if auteur_tag:
            a_tag = auteur_tag.find("a")
            if a_tag and a_tag.get("href"):
                auteur_nom = a_tag.text.strip()
                href = a_tag.get("href")
                if "/ark:/12148/" in href:
                    auteur_id = href.split("/ark:/12148/")[-1]

        publication_info = meta.get("DC.publisher", "")
        lieu = editeur = ""
        if publication_info:
            if "." in publication_info:
                parts = publication_info.split(".", 1)
                lieu = parts[0].strip()
                editeur = parts[1].strip()

        annee = meta.get("DC.date", "")

        # Recherche du lien Gallica
        lien_gallica = ""
        gallica_link_tag = soup.find("a", string=lambda text: text and "Gallica" in text)
        if gallica_link_tag:
            lien_gallica = gallica_link_tag.get("href", "")

        results.append({
            "identifiant": ident,
            "titre": titre,
            "auteur_nom": auteur_nom,
            "auteur_id": auteur_id,
            "contributeur": contributeur,
            "editeur": editeur,
            "lieu": lieu,
            "annee": annee,
            "lien_gallica": lien_gallica
        })
        print(auteur_nom)
        print(titre)

    return results

data = scrapingBNF(["cb300161996","cb37301332j","cb300410907","cb30051554z","cb300667240","cb314273066","cb35946245d","cb300903273","cb30103632j","cb30103626m","cb30104673c","cb301120127","cb30116976x","cb30121725g","cb30123119c","cb36343334d","cb301526012","cb30153200v","cb301825273","cb393098684","cb30202978m","cb302081258","cb30212560n","cb30221861s","cb30232445w","cb301463448","cb30260140g","cb30260144v","cb30268438p","cb30349750c","cb30361205n","cb303689596","cb303702048","cb30380290w","cb303802870","cb31118270j","cb304802290","cb30529285k","cb30544760t","cb33993284b","cb305448080","cb305668542","cb30583364p","cb30608184g","cb30736731v","cb314278711","cb30745634k","cb30745658k","cb30745658k","cb307622794","cb31427308w","cb44132214j","cb40256242s","cb308893906","cb30908224d","cb314537942","cb309554515","cb30968775x","cb31005702b","cb31005679n","cb31005714b","cb30853412m","cb363492902","cb31340315q","cb31367008q","cb313855368","cb31453594h","cb315497876","cb315426637"])
print(data)