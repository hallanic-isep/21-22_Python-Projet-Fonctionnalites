import random

import pam
import pim

def print_model( data ):
    print("POINTS DE VIE =", data["live_points"])

    for line in data["labyrinth"]:
        for room in line:
            if room["visited"]:
                print(room["content"],end="")
            else:
                print("#",end="")
        print()

    print("joueur en ligne", data["li"], "colonne", data["co"])


def handle_user_input(model):
    print("n,s,e,o = direction | fin = sauve et quitte | raz = abandon")
    action = input("commande: ")
    if action == "n":
        if model["li"] == 0:
            print("Impossible d'aller au nord...")
        else:
            model["li"] -= 1
    elif action == "s":
        if model["li"] == 3:
            print("Impossible d'aller au sud...")
        else:
            model["li"] += 1
    elif action == "o":
        if model["co"] == 0:
            print("Impossible d'aller à l'ouest...")
        else:
            model["co"] -= 1
    elif action == "e":
        if model["co"] == 3:
            print("Impossible d'aller à l'est...")
        else:
            model["co"] += 1
    elif action == "fin":
        print("Partie sauvegardée...")
        pam.backup_game(model)
        model["running"] = False
    elif action == "raz":
        print("Partie annulée...")
        pam.clear_backup()
        model["running"] = False
    else:
        print("Commande inconnue...")

def processEmptyRoom(model):
    print("Cette pièce est vide...")
    model["labyrinth"][ model["li"] ][ model["co"] ]["content"] = "J"

def processTresor(model):
    print("BRAVO, vous avez trouvé le trésor, vous êtes riche !!!")
    model["running"] = False # Fin du jeu
    pam.clear_backup()  # Supprime la partie sauvegardée

def processDragon(model):
    print("ATTENTION, vous êtes attaqué par le dragon...")
    lost_points = random.randint(1,10)
    model["live_points"] -= lost_points
    if model["live_points"] <= 0:
        print("Le dragon vous a terrassé, vous avez perdu...")
        model["running"] = False  # Fin du jeu
        pam.clear_backup() # Supprime la partie sauvegardée
    else:
        print("Vous avez battu le dragon !!!")
        print("Le dragon vous a quand même blessé avant de s'enfuir.")
        print("Vous avez perdu", lost_points, "points de vie...")
        # Le joueur prend la place du dragon
        model["labyrinth"][model["li"]][model["co"]]["content"] = "J"
        # Fonctionnalité 2.3.1 : Le dragon change de salle
        pim.hideDagon( model )
