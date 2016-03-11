# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
projet-isn -- interface
MODULE DESC 
"""
# Constants #

import os
import sys

from dialog import Dialog

import database.inventory
import database.players

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"


def init():
    os.mkdir("./databases/")
    database.players.init_players()


def auth():
    print("Bienvenue sur le TheoRPG. Pour commencer, je vais avoir besoin de savoir qui vous etes.")
    player = input("Entrez votre nom >")
    if database.players.playerExist(player):
        print("Bonjour " + player + " ! \n Entrez ici votre mot de passe afin que je vous reconnaisse.")
        password = input("Entrez votre mot de passe >")
        if password == database.players.playerDict(player)["password"]:
            print("Je vois que c'est bien vous :D ! Venez avec moi...")
            return player
        else:
            print("Sale usurpateur ! Tu crois pouvoir t'en tirer avec ca ? C'est pas un mot de passe correct !")
            sys.exit(0)
    else:
        print("Bonjour, je ne vous connais pas ! Ce n'est pas un probleme, présentez vous !")
        password = input("Entrez un mot de passe >")
        database.players.newplayer(player, password)
        database.inventory.createInventory(player)
        return player


def game(player):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran
        d = Dialog(dialog="dialog", autowidgetsize=True)
        d.set_background_title("TheoRPG")
        code, tag = d.menu("Donc, que voulez-vous faire ?",
                           choices=[("(1)", "Miner"),
                                    ("(2)", "Creuser"),
                                    ("(3)", "Ne rien faire")])
        if code == d.OK:
            if tag == "(1)":
                d.msgbox("Vous minez dans la grotte environnante")
                database.inventory.addToInventory(player, "pierre", 10)
                d.msgbox("Vous trouvez 10 pierres.")
        else:
            print("Au revoir :D")
            sys.exit(0)


def main():
    player = auth()
    game(player)


# Check for first launch...
if not os.path.exists("./databases"):
    init()
    print("Le logiciel est initialisé correctement !")
    print("Lancement en cours...")

main()
