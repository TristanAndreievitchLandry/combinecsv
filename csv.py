import os
import glob # le module qu'on a déjà vu qui permet de sélectionner plusieurs fichiers selon leur extension, ici .csv.
import pandas as pd #un module permettant la manipulation et l'analyse des données
os.chdir('C:/Users/Tristan/Desktop/Afrika')
extension = 'csv'
tous_les_csv = [i for i in glob.glob('*.{}'.format(extension))]
#on a donc sélectionné tous les fichiers .csv, maintenant on va les combiner:
combined_csv = pd.concat([pd.read_csv(f) for f in tous_les_csv ])
#et on exporte enfin vers un nouveau fichier csv, en lui donnant un nom et en spécifiant l'encodage (utf-8) pour éviter les problèmes avec les langues qui, comme le français, ont des accents:
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
