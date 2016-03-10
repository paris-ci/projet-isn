# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
projet-isn -- interface
MODULE DESC 
"""
# Constants #

import os

import sys

import database.players
import database.inventory
import config
import objets

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"


def init():
    os.mkdir("./databases/")
    database.players.init_players()


def auth():
    print("Bienvenue sur le TheoRPG. Pour commencer, je vais avoir besoin de savoir qui vous etes.")
    player = input("Entrez votre nom >")
    if database.players.playerExist(player):
        print("Bonjour " + player +" ! \n Entrez ici votre mot de passe afin que je vous reconnaisse.")
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



def main():
    player = auth()
    database.inventory.setItemNumber(player, "or", 3)




# Check for first launch...
if not os.path.exists("./databases"):
    init()
    print("Le logiciel est initialisé correctement !")
    print("Lancement en cours...")

main()