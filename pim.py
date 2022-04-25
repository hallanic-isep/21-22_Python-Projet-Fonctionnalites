import random

import pam
import poum


def start_game():
    print("Bienvenue dans notre \"Donjon & Dragon\"")

    try:
        model = pam.load_backup()
    except FileNotFoundError:
        model = pam.create_model()

    # Boucle de gestion des événements
    model["running"] = True
    while( model["running"] ):
        poum.print_model( model )
        pam.handle_actions(model)
        print()
        pam.process_events( model )

    poum.print_model(model) # Affichage de l'état final du jeu
    print("EXECUTION TERMINEE !!!")



def hideDagon(model):

    for i in range(32): # Abandon au bout de 32 essais => pas de possibilité
        # Il faut trouver une salle non visitée et sans le trésors
        li = random.randrange(4)
        co = random.randrange(4)
        #print("hideDagon", "li=", li, "co=",co)
        room = model["labyrinth"][li][co]
        if (not room["visited"]) and ( not (room["content"] == "T") ):
            room["content"] = "D"
            return # Sortie avec le dragon caché dans une nouvelle pièce

    return # Sortie sans trouver de pièce => le dragon est supprimé !!!
