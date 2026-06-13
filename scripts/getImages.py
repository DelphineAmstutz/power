# Vibecoded with ChatGPT Instant https://chatgpt.com/share/6a2dc36c-3e44-83eb-8422-75ad3e78ee45
import os
import urllib.request
import urllib.error
import time


def telecharge(liste_images, dossier="."):
    """
    Télécharge une liste d'images.

    Paramètres :
        liste_images : liste de listes [url, nom_fichier]
        dossier : dossier où enregistrer les fichiers

    Retour :
        liste des téléchargements ayant échoué
    """

    echecs = []

    # Création du dossier s'il n'existe pas
    os.makedirs(dossier, exist_ok=True)

    for url, nom_fichier in liste_images:
        time.sleep(2)
        chemin = os.path.join(dossier, nom_fichier)

        try:
            urllib.request.urlretrieve(url, chemin)
            print(f"? Téléchargement réussi : {nom_fichier}")

        except Exception as e:
            print(f"? Échec : {nom_fichier}")
            print(f"   URL : {url}")
            print(f"   Erreur : {e}")

            echecs.append([url, nom_fichier])

    return echecs
   
# Search/replace for Gallica links:
# https://gallica.bnf.fr/ark:/12148/(bpt[^./]*)([./].*medres)
# ["https://gallica.bnf.fr/ark:/12148/\1\2","gallica-\1.jpg"],

# Search/replace for Google Books links:
# https://books.google([^?]*)\?id=([^&]*)&(.*)
# ["https://books.google\1?id=\2&\3","gb-\2.jpg"],
 
echecs = telecharge([

["https://books.google.bj/books/content?id=DwRUAAAAcAAJ&printsec=frontcover&img=1&zoom=3&edge=curl","gb-DwRUAAAAcAAJ.jpg"],
["https://books.google.fr/books/content?id=Xm3KZ_upfVoC&hl=fr&pg=PP9&img=1&zoom=3&bul=1&sig=ACfU3U1OQ8djbZTUW9UCKCnFTRztu1A1CA&w=800","gb-Xm3KZ_upfVoC.jpg"],
["https://books.google.fr/books/content?id=Sh-E_JuIEtIC&hl=fr&pg=PP1&img=1&zoom=3&sig=ACfU3U3_kX9acO7B0d9pppmkivkODnNziA&w=800","gb-Sh-E_JuIEtIC.jpg"],
["https://books.google.fr/books/content?id=RZdXAAAAcAAJ&hl=fr&pg=PP1&img=1&zoom=3&sig=ACfU3U1mZ_epUcwSKWKMT4tVtJfnQFBJpA&w=800","gb-RZdXAAAAcAAJ.jpg"],
["https://books.google.bj/books/content?id=0PC2P2jgndMC&printsec=frontcover&img=1&zoom=3&edge=curl","gb-0PC2P2jgndMC.jpg"],
["https://books.google.bj/books/content?id=QZqn07W0b3sC&printsec=frontcover&img=1&zoom=3&edge=curl","gb-QZqn07W0b3sC.jpg"],
["https://books.google.fr/books?id=gL7LYEr3kloC&printsec=frontcover&img=1&zoom=3","gb-gL7LYEr3kloC.jpg"],
["https://books.google.fr/books?id=Vp28ljBZOSAC&printsec=frontcover&img=1&zoom=3","gb-Vp28ljBZOSAC.jpg"],
["https://books.google.fr/books/content?id=djlFAAAAcAAJ&printsec=frontcover&img=1&zoom=3","gb-djlFAAAAcAAJ.jpg"],
["https://books.google.fr/books?id=wAlLNsI02HEC&printsec=frontcover&img=1&zoom=3","gb-wAlLNsI02HEC.jpg"],
["https://books.google.fr/books?id=9CVgAAAAcAAJ&printsec=frontcover&img=1&zoom=3","gb-9CVgAAAAcAAJ.jpg"],
["https://books.google.fr/books/content?id=2Vk0tBOL48QC&hl=fr&pg=PP1&img=1&zoom=3&sig=ACfU3U2RkPGPig11XQTN2m1yxekgJoZCnw&w=800","gb-2Vk0tBOL48QC.jpg"],
["https://books.google.fr/books?id=goZMAAAAcAAJ&printsec=frontcover&img=1&zoom=3","gb-goZMAAAAcAAJ.jpg"],
["https://books.google.fr/books?id=ibD4-rSKBC8C&printsec=frontcover&img=1&zoom=3","gb-ibD4-rSKBC8C.jpg"],
["https://books.google.bj/books/content?id=gG9oAAAAcAAJ&printsec=frontcover&img=1&zoom=3&edge=curl","gb-gG9oAAAAcAAJ.jpg"],
["https://books.google.bj/books/content?id=0TefLygkdBcC&printsec=frontcover&img=1&zoom=3&edge=curl","gb-0TefLygkdBcC.jpg"],
["https://books.google.bj/books/content?id=TH4bk5r-uSYC&printsec=frontcover&img=1&zoom=3&edge=curl","gb-TH4bk5r-uSYC.jpg"],
["https://books.google.fr/books/content?id=MfrcK8aov68C&hl=fr&pg=PP5&img=1&zoom=3&bul=1&sig=ACfU3U2N1Hmp-dzCLbQED-E8oQZSDi1Isg&w=800","gb-MfrcK8aov68C.jpg"],
["https://books.google.fr/books/content?id=BW8-AAAAcAAJ&printsec=frontcover&img=1&zoom=3","gb-BW8-AAAAcAAJ.jpg"],
["https://books.google.bj/books/content?id=Sc9KYyizldgC&printsec=frontcover&img=1&zoom=3&edge=curl","gb-Sc9KYyizldgC.jpg"],
["https://books.google.bj/books/content?id=kR-B6aKGAGEC&printsec=frontcover&img=1&zoom=3&edge=curl","gb-kR-B6aKGAGEC.jpg"],
["https://books.google.bj/books/content?id=RBRbAAAAQAAJ&printsec=frontcover&img=1&zoom=3&edge=curl","gb-RBRbAAAAQAAJ.jpg"],
["https://books.google.bj/books/content?id=hEYiqfGkAiwC&printsec=frontcover&img=1&zoom=3&edge=curl","gb-hEYiqfGkAiwC.jpg"],
["https://books.google.bj/books/content?id=DTbuLzr6XAYC&printsec=frontcover&img=1&zoom=3&edge=curl","gb-DTbuLzr6XAYC.jpg"],
["https://books.google.fr/books/content?id=qWkFRBAHMs4C&hl=fr&pg=PP5&img=1&zoom=3&bul=1&sig=ACfU3U2PkhFBIrQVeaCw0mdzEEXcwl2bVQ&w=800","gb-qWkFRBAHMs4C.jpg"],
["https://books.google.bj/books/content?id=zJtEAAAAcAAJ&printsec=frontcover&img=1&zoom=3&edge=curl","gb-zJtEAAAAcAAJ.jpg"],
["https://books.google.bj/books/content?id=V_OdwAEACAAJ&printsec=frontcover&img=1&zoom=3&edge=curl","gb-V_OdwAEACAAJ.jpg"],
["https://books.google.bj/books/content?id=mudICV56XKAC&printsec=frontcover&img=1&zoom=3&edge=curl","gb-mudICV56XKAC.jpg"],
["https://books.google.bj/books/content?id=-dhYAAAAcAAJ&printsec=frontcover&img=1&zoom=3&edge=curl","gb--dhYAAAAcAAJ.jpg"],
["https://books.google.fr/books/content?id=fVxLAAAAcAAJ&printsec=frontcover&img=1&zoom=3","gb-fVxLAAAAcAAJ.jpg"],
["https://books.google.bj/books/content?id=v57G4isp_50C&printsec=frontcover&img=1&zoom=3&edge=curl","gb-v57G4isp_50C.jpg"],
["https://books.google.bj/books/content?id=n3mgcVQKEfQC&printsec=frontcover&img=1&zoom=3&edge=curl","gb-n3mgcVQKEfQC.jpg"],
["https://books.google.bj/books/content?id=Ci9eAAAAcAAJ&printsec=frontcover&img=1&zoom=3&edge=curl","gb-Ci9eAAAAcAAJ.jpg"],
])

print(echecs)