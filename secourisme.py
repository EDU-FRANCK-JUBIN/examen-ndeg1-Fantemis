from easygui import *
msg = "Veuillez renseigner les informations"
fieldNames = ["Nom","Lieu victime","Nombre de victime","Etat de la ou les victimes"]
meschoix = multenterbox(msg, 'bonsoir', fieldNames)



signes_symptomes = ["Décrivez et localisez les symptomes","Etat des victimes de 1 à 10","Qualifiez la douleur"]
meschoix = multenterbox("Signes et symptomes", 'bonsoir', signes_symptomes)
