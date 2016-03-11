# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
projet-isn -- interface
MODULE DESC 
"""
# Constants #

import os
import sys

import time
from dialog import Dialog

import database.inventory
import database.players

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"


def init():
    os.mkdir("./databases/")
    database.players.init_players()


def auth():
    d.msgbox("Bienvenue sur le TheoRPG. Pour commencer, je vais avoir besoin de savoir qui vous etes.")
    code, player = d.inputbox("Entrez votre nom")
    if database.players.playerExist(player):
        d.msgbox("Bonjour " + player + " !")
        code, password = d.passwordbox("Entrez votre mot de passe. Celui ci ne s'affiche pas pour des rasions de sécurité")
        if password == database.players.playerDict(player)["password"] and code == d.OK:
            d.msgbox("Je vois que c'est bien vous :D ! Venez avec moi...")
            return player
        else:
            d.msgbox("Sale usurpateur ! Tu crois pouvoir t'en tirer avec ca ? C'est pas un mot de passe correct !")
            sys.exit(0)
    else:
        d.msgbox("Bonjour, je ne vous connais pas ! Ce n'est pas un probleme, présentez vous !")
        code, password = d.passwordbox("Entrez un mot de passe. Celui ci ne s'affiche pas pour des rasions de sécurité")
        if code == d.OK:
            database.players.newplayer(player, password)
            database.inventory.createInventory(player)
            return player
        else:
            d.msgbox("Tu me laisses moisir comme ca ? Tu ne veux pas me donner de mot de passe ? EH BAH NON ! Ca ne se passera pas comme ca !")
            sys.exit(0)


def progress(pause, text):
    d.gauge_start(text=text)
    for i in range(0,100):
        d.gauge_update(i)
        time.sleep(pause/100)

    d.gauge_stop()


def game(player):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran

        code, tag = d.menu("Donc, que voulez-vous faire ?",
                           choices=[("(1)", "Miner"),
                                    ("(2)", "Creuser"),
                                    ("(3)", "Ne rien faire")],
                           ok_label="Ok, je veux faire ca",
                           cancel_label="Préférances/Quitter")
        if code == d.OK:
            if tag == "(1)":
                d.msgbox("Vous minez dans la grotte environnante")
                progress(20, "Je mine...")
                database.inventory.addToInventory(player, "pierre", 10)
                d.msgbox("Vous trouvez 10 pierres.")
            elif tag == "(2)":
                d.msgbox("Vous allez vers le petit bois juste a coté de vous.")
                progress(10, "Je marche vers le bois...")
                d.msgbox("Vous creusez dans ce bois.")
                progress(20, "Je creuse la terre...")
                database.inventory.addToInventory(player, "brindilles", 20)
                database.inventory.addToInventory(player, "terre", 5)
                d.msgbox("Vous trouvez 5 terre et 2 brindilles.")

        else:
            code, tag = d.menu("Menu des préférances :",
                               choices=[("(1)", "Revenir au jeu"),
                                        ("(2)", "Changer mon mot de passe"),
                                        ("(3)", "Quitter")],
                               ok_label="Ok, je veux faire ca",
                               cancel_label="Annuler")
            if tag == "(1)":
                pass
            elif tag == "(2)":
                code, newpass = d.passwordbox("Entrez un mot de passe (pour des raisons de sécuritée, celui-ci ne sera pas affiché)")
                if code == d.OK:
                    database.players.changePref(player, "password", newpass)
                    d.msgbox("Mot de passe changé avec succés.")
                else:
                    d.msgbox("Votre mot de passe n'as pas été changé.")
            elif tag == "(3)":
                d.msgbox("Au revoir :D")
                sys.exit(0)


def main():
    player = auth()
    game(player)


# Check for first launch...
if not os.path.exists("./databases"):
    init()
    print("Le logiciel est initialisé correctement !")
    print("Lancement en cours...")
    time.sleep(1)

d = Dialog(dialog="dialog") #, autowidgetsize=True
d.set_background_title("TheoRPG")
main()
