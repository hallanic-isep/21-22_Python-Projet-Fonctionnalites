import random
import json
import os

import poum

def create_model():

    root = {}

    root["live_points"] = 10

    labyrinth = [] # On démarre avec une liste vide
    for line_n in range(4):
        rooms_line = []
        for room_n in range(4):
            room = {}
            room["content"] = "." # . indique que la piece est vide
            room["visited"] = False
            rooms_line.append(room)
        labyrinth.append(rooms_line)

    root["labyrinth"] = labyrinth

    #root["labyrinth"][2][1]["content"] = "J"
    #root["labyrinth"][2][1]["visited"] = True
    #root["labyrinth"][0][0]["content"] = "D"
    #root["labyrinth"][3][3]["content"] = "T"

    shuffle_li = [0, 1, 2, 3]
    shuffle_co = [0, 1, 2, 3]
    random.shuffle(shuffle_li)
    random.shuffle(shuffle_co)
    print(shuffle_li, shuffle_co)
    # Initialisation des positions
    # ATTENTION ! CETTE PARTIE EST COMPLEXE...
    root["labyrinth"][shuffle_li[0]][shuffle_co[0]]["content"] = "J"
    root["labyrinth"][shuffle_li[0]][shuffle_co[0]]["visited"] = True
    root["li"] = shuffle_li[0]
    root["co"] = shuffle_co[0]
    root["labyrinth"][shuffle_li[1]][shuffle_co[1]]["content"] = "D"
    root["labyrinth"][shuffle_li[2]][shuffle_co[2]]["content"] = "T"

    return root


def backup_game(json_data):
    json_file = open("sauvegarde.json", "w")
    json.dump(json_data, json_file, indent=2)
    json_file.close()

def load_backup():
    json_file = open("sauvegarde.json", "r")
    json_data = json.load(json_file)
    json_file.close()
    json_data["labyrinth"][ json_data["li"] ][ json_data["co"] ]["content"] = "J"
    return json_data

def clear_backup():
    try:
        os.remove("sauvegarde.json")
    except FileNotFoundError:
        pass # Pas d'erreur si le fichier n'existe pas puisqu'on voulait le supprimer

def handle_actions(model):
    # Le joueur quitte la salle qui devient vide
    model["labyrinth"][ model["li"] ][ model["co"] ]["content"] = "."
    # Fonctionnalité 4.1
    poum.handle_user_input( model )


def process_events(model):
    room = model["labyrinth"][ model["li"] ][ model["co"] ]

    # Indique que la pièce est visité
    room["visited"] = True

    # Traitement du contenu de la pièce
    if room["content"] == "T":
        poum.processTresor(model)
    elif room["content"] == "D":
        poum.processDragon(model)
    else:
        poum.processEmptyRoom(model)




