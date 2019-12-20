import turtle
import random



# Initialisation du jeu
ts = turtle.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue Ã  la course des tortues !")
ts.setup (width=1400, height=800, startx=0, starty=0)






# DÃ©clarez les 5 tortues et positionnez-les sur leurs hexagones respectifs
print(turtle.position())
michelangelo = turtle.Turtle()
michelangelo.up()
michelangelo.color("orange")
michelangelo.shape('turtle')
michelangelo.goto(-650, 300)

leonardo = turtle.Turtle()
leonardo.up()
leonardo.color("Deep Sky Blue")
leonardo.shape('turtle')
leonardo.goto(-650, 150)

raphael = turtle.Turtle()
raphael.up()
raphael.color("Red")
raphael.shape('turtle')
raphael.goto(-650, 0)

splinter = turtle.Turtle()
splinter.up()
splinter.color("Dark Slate Gray")
splinter.shape('turtle')
splinter.goto(-650, -150)

donatello = turtle.Turtle()
donatello.up()
donatello.color("purple")
donatello.shape('turtle')
donatello.goto(-650, -300)

# Demander de saisir dans la console les prÃ©dictions des joeurus 1 et 2 dans le format 1,2,3
J1_list = []
J2_list = []
prediction_J1 = -1
prediction_J2 = -1
for i in range(1, 4):
    while(prediction_J1 < 1 and prediction_J1 > 3)
        prediction_J1 = input("J1, veuillez saisir votre prédiction pour la  %i eme place" % (i))
    J1_list.append(prediction_J1)
print("Merci J1")
print(J1_list)

for i in range(1, 4):
    while(prediction_J2 < 1 and prediction_J2 > 3)
        prediction_J2 = input("J2, veuillez saisir votre prédiction pour la %i eme place" % (i))
    J2_list.append(prediction_J2)
print("Merci J2")
print(J2_list)

# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui reprÃ©sente le nombre de pixels du dÃ©placement vers la droite
michelangelo_speed = random.randint(1, 5)
leonardo_speed = random.randint(1, 5)
raphael_speed = random.randint(1, 5)
splinter_speed = random.randint(1, 5)
donatello_speed = random.randint(1, 5)

course_lancee = True
while course_lancee:

    if(michelangelo.position()[0] > 700):
        michelangelo.forward(0)
    else:
        michelangelo.forward(michelangelo_speed)

    if (leonardo.position()[0] > 700):
        leonardo.forward(0)
    else:
        leonardo.forward(leonardo_speed)

    if (raphael.position()[0] > 700):
        raphael.forward(0)
    else:
        raphael.forward(raphael_speed)

    if (splinter.position()[0] > 700):
        splinter.forward(0)
    else:
        splinter.forward(splinter_speed)

    if (donatello.position()[0] > 700):
        donatello.forward(0)
    else:
        donatello.forward((donatello_speed))

    if(donatello.position()[0] > 700 and splinter.position()[0] > 700 and raphael.position()[0] > 700 and leonardo.position()[0] > 700 and michelangelo.position()[0] > 700):
        print("La course est terminée")
        break
resultats_list = [michelangelo.position(), leonardo.position(), raphael.position(), splinter.position(), donatello.position()]
print(resultats_list)
# Comparer les rÃ©sultats de la course avec les pronostics des joueurs
# et afficher le rÃ©sultat de la course
# et le joueur gagnant avec la tortue arbitre et l'instruction turtle.Write Ã  la position 0,0
# A IMPLEMENTER



turtle_arbitre = turtle.Turtle()
turtle_arbitre.goto(0,0)
turtle_arbitre.color("Black")
turtle_arbitre.write("Le joueur 1 Ã  gagnÃ©", move=True, align="left", font=("Arial", 16, "normal"))



turtle.mainloop()