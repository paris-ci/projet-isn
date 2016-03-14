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
import situations.maison
import situations.mine

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"


def init():
    os.mkdir("./databases/")
    database.players.init_players()


def auth():
    d.msgbox("Bienvenue sur le TheoRPG. Pour commencer, je vais avoir besoin de savoir qui vous etes.")
    code, player = d.inputbox("Entrez votre nom")
    if database.players.playerExist(player) and code == d.OK:
        d.msgbox("Bonjour " + player + " !")
        code, password = d.passwordbox(
            "Entrez votre mot de passe. Celui ci ne s'affiche pas pour des rasions de sécurité")
        if password == database.players.playerDict(player)["password"] and code == d.OK:
            d.msgbox("Je vois que c'est bien vous :D ! Venez avec moi...")
            return player
        else:
            d.msgbox("Sale usurpateur ! Tu crois pouvoir t'en tirer avec ca ? C'est pas un mot de passe correct !")
            sys.exit(0)
    elif code != d.OK:
        d.msgbox("Ok, pas de soucis, tu ne veux pas jouer, je ne vais pas t'importuner avec ca ! A pluche :D")
        sys.exit(0)
    else:
        d.msgbox("Bonjour, je ne vous connais pas ! Ce n'est pas un probleme, présentez vous !")
        code, password = d.passwordbox("Entrez un mot de passe. Celui ci ne s'affiche pas pour des rasions de sécurité")
        if code == d.OK:
            database.players.newplayer(player, password)
            database.inventory.createInventory(player)
            database.players.changePref(player, "location", "maison")
            return player
        else:
            d.msgbox(
                "Tu me laisses moisir comme ca ? Tu ne veux pas me donner de mot de passe ? EH BAH NON ! Ca ne se passera pas comme ca !")
            sys.exit(0)


def progress(pause, text):
    d.gauge_start(text=text)
    for i in range(0, 100):
        d.gauge_update(i)
        time.sleep(pause / 100)

    d.gauge_stop()


def pref(player):
    code, tag = d.menu("Menu des préférances :",
                       choices=[("(1)", "Revenir au jeu"),
                                ("(2)", "Changer mon mot de passe"),
                                ("(3)", "Quitter")],
                       ok_label="Je choisis ca.",
                       cancel_label="Annuler")
    if tag == "(1)":
        pass
    elif tag == "(2)":
        code, newpass = d.passwordbox(
            "Entrez un mot de passe (pour des raisons de sécuritée, celui-ci ne sera pas affiché)")
        if code == d.OK:
            database.players.changePref(player, "password", newpass)
            d.msgbox("Mot de passe changé avec succés.")
        else:
            d.msgbox("Votre mot de passe n'as pas été changé.")
    elif tag == "(3)":
        d.msgbox("Au revoir :D")
        sys.exit(0)


def game(player):
    os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran
    ret = True
    while True:
        loc = database.players.playerDict(player)["location"]
        if loc == "maison":
            ret = situations.maison.base(d, player)
        if loc == "mine":
            ret = situations.mine.base(d, player)


        if ret == "pref":
            pref(player)


def main():
    player = auth()
    game(player)


# Check for first launch...
if not os.path.exists("./databases"):
    init()
    print("Le logiciel est initialisé correctement !")
    print("Lancement en cours...")
    time.sleep(1)

d = Dialog(dialog="dialog")  # , autowidgetsize=True
d.set_background_title("TheoRPG")
main()
