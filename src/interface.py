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

from raven import Client

from dialog import Dialog

import database.inventory
import database.players
import situations.bois
import situations.maison
import situations.mine
import situations.tutorial

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"


def init():
    os.mkdir("./databases/")
    database.players.init_players()


def auth():
    d.msgbox("Bienvenue sur le TheoRPG. Pour commencer, je vais avoir besoin de savoir qui vous etes.")
    code, player = d.inputbox("Entrez votre nom")
    if player == "":
        d.msgbox("Entre un nom d'utilisateur correct. Et pas juste un truc blanc tout moche.")
        sys.exit(1)
    if database.players.playerExist(player) and code == d.OK:
        d.msgbox("Bonjour " + player + " !")
        code, password = d.passwordbox(
                "Entrez votre mot de passe. Celui ci ne s'affiche pas pour des rasions de sécurité")
        if password == database.players.playerDict(player)["password"] and code == d.OK:
            d.msgbox("Je vois que c'est bien vous :D ! Venez avec moi...")
            return player
        else:
            d.msgbox("Sale usurpateur ! Tu crois pouvoir t'en tirer avec ca ? C'est pas un mot de passe correct !")
            sys.exit(1)
    elif code != d.OK:
        d.msgbox("Ok, pas de soucis, tu ne veux pas jouer, je ne vais pas t'importuner avec ca ! A pluche :D")
        sys.exit(0)
    else:
        d.msgbox("Bonjour, je ne vous connais pas ! Ce n'est pas un probleme, présentez vous !")
        code, password = d.passwordbox("Entrez un mot de passe. Celui ci ne s'affiche pas pour des rasions de sécurité")
        if code == d.OK:
            database.players.newplayer(player, password)
            database.inventory.createInventory(player)
            database.players.changePref(player, "location", "tutorial")
            return player
        else:
            d.msgbox(
                    "Tu me laisses moisir comme ca ? Tu ne veux pas me donner de mot de passe ? EH BAH NON ! Ca ne se passera pas comme ca !")
            sys.exit(0)


def pref(player):
    code, tag = d.menu("Menu des préférances :",
                       choices=[("(1)", "Revenir au jeu"),
                                ("(2)", "Changer mon mot de passe"),
                                ("(3)", "Supprimer mon compte"),
                                ("(4)", "Quitter")],
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
        code = d.yesno("Etes vous sur de voulor supprimer votre compte. IL NE POURRA ETRE RESTAURE.",
                yes_label="Oui, je suis sur de vouloir supprimer ce compte",
                no_label="Je te supplie, j'ai changé d'avis, je ne veux rien supprimer",
                width=200)
        if code == d.OK:
            database.players.deletePlayer(player)
            code = d.yesno("Regrettez-vous cela ?",
                           yes_label="Non",
                           no_label="Oui")
            if code == d.OK:
                d.msgbox("Le compte " + player + " à bien été supprimé. Le jeu va maintenent se fermer.")
                sys.exit(0)
            else:
                d.msgbox("Nous aussi.")
                sys.exit(0)
        else:
            d.msgbox("C'est bien, tu fais le bon choix. Ton compte n'est pas supprimé.")

    elif tag == "(4)":
        d.msgbox("Au revoir :D")
        sys.exit(0)


def game(player):
    os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran
    while True:
        loc = database.players.playerDict(player)["location"]
        if loc == "maison":
            ret = situations.maison.base(d, player)
        elif loc == "mine":
            ret = situations.mine.base(d, player)
        elif loc == "bois":
            ret = situations.bois.base(d, player)
        elif loc == "tutorial":
            ret = situations.tutorial.base(d, player)
        else:
            raise FileNotFoundError

        if ret == "pref":
            pref(player)


def main():
    player = auth()
    game(player)


if __name__ == '__main__':

    # Check for first launch...
    if not os.path.exists("./databases"):
        init()
        print("Le logiciel est initialisé correctement !")
        print("Lancement en cours...")
        time.sleep(1)

    d = Dialog(dialog="dialog", autowidgetsize=True)  # , autowidgetsize=True
    d.set_background_title("TheoRPG")
    try:
        main()
    except Exception as e:
        client = Client('https://49aa914786e14bd693802f876db91c13:5ce6654ffc3c409c8ff900efcbbe1c60@app.getsentry.com/70494')
        client.captureException()
        os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran
        print("Malheureusement, une erreur est survenue (" + str(e) + "). Nous nous en excusons. Veuillez envoyer le rapport d'erreur suivant ainsi qu'un bref résumé des vos actions sur GitHub en suivant le lien suivant : https://github.com/paris-ci/projet-isn/issues")
        print("=== DEBUT RAPPORT ERREUR ENVOYE AUTOMATIQUEMENT===")
        raise

