# coding: utf8
# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

# Constants #

import os
import sys
import time

from raven import Client

from dialog import Dialog

import database.inventory
import database.players
import situations.bois
import situations.centreVille
import situations.chateau
import situations.magasinTDCPO
import situations.maison
import situations.marchandArme
import situations.marchandMateriaux
import situations.mine
import situations.monstreTaverne
import situations.montagne
import situations.pharmacie
import situations.posteDePolice
import situations.prison
import situations.quartierCommercant
import situations.quartierSud
import situations.salleDuTrone
import situations.taverne
import situations.terreDeChaisPasOu
import situations.tutorial
import situations.villeDeNullepart



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
                str("Entrez votre mot de passe."), insecure=True)
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
                                ("(4)", "Quitter"),
                                ("(5)", "Entrer un code")],
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
        code = d.yesno("Etes vous sur de vouloir supprimer votre compte ? /!\ IL NE POURRA PAS ETRE RESTAURE. /!\ ",
                yes_label="Oui, je suis sur de vouloir supprimer ce compte",
                no_label="Je te supplie, j'ai changé d'avis, je ne veux rien supprimer",
                width=200,
                height=7)
        if code == d.OK:
            database.players.deletePlayer(player)
            code = d.yesno("Regrettez-vous cela ?",
                           yes_label="Non",
                           no_label="Oui") # Attention : boutons oui non inversés.
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
    elif tag == "(5)":
        code, text = d.inputbox("Entrez le code qui vous à été fourni ici :")

        # Liste des codes de triche :
        #
        # - streetmoney >> Donne 1000 or.
        # - homesweethome >> Téléportation instantanée à la maison
        # - unmarsetca >> Multiplie par 10 la quantitée de chaque objet possédé
        # - bugseverywhere >> Fait planter le jeu.
        # - GlaDOS >> Donne une PATATE.

        if code == d.OK:
            if text == "streetmoney":
                database.inventory.addToInventory(player, "or", 1000)
            elif text == "homesweethome":
                database.players.changePref(player, "location", "maison")
            elif text == "unmarsetca":
                playerInv = database.inventory.getPlayerDict(player)
                for item in playerInv:
                    if int(item["quantity"]) != 0:
                        newqtity = int(item["quantity"]) * 10 - int(item["quantity"])
                        database.inventory.addToInventory(player, item["name"], newqtity)
            elif text == "bugseverywhere":
                raise Exception
            elif text == "GlaDOS":
                database.inventory.addToInventory(player, "patate", 1)
            elif text == "iwanttogonullepart":
                database.players.changePref(player, "location", "villeDeNullepart")
            elif text == "putainavance":
                database.inventory.addToInventory(player, "anneau de transport", 1)
            else:
                d.msgbox("Le MJ : Je ne comprends pas votre demande.")

        else:
            d.msgbox("Rien ne se passe.")

def game(player):
    os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran
    while True:
        loc = database.players.playerDict(player)["location"]
        if loc == "bois":
            ret = situations.bois.base(d, player)
        elif loc == "centreVille":
            ret = situations.centreVille.base(d, player)
        elif loc == "chateau":
            ret = situations.chateau.base(d, player)
        elif loc == "magasinTDCPO":
            ret = situations.magasinTDCPO.base(d, player)
        elif loc == "maison":
            ret = situations.maison.base(d, player)
        elif loc == "marchandArme":
            ret = situations.marchandArme.base(d, player)
        elif loc == "marchandMateriaux":
            ret = situations.marchandMateriaux.base(d, player)
        elif loc == "mine":
            ret = situations.mine.base(d, player)
        elif loc == "monstreTaverne":
            ret = situations.monstreTaverne.base(d, player)
        elif loc == "montagne":
            ret = situations.montagne.base(d, player)
        elif loc == "pharmacie":
            ret = situations.pharmacie.base(d, player)
        elif loc == "posteDePolice":
            ret = situations.posteDePolice.base(d, player)
        elif loc == "prison":
            ret = situations.prison.base(d, player)
        elif loc == "quartierCommercant":
            ret = situations.quartierCommercant.base(d, player)
        elif loc == "quartierSud":
            ret = situations.quartierSud.base(d, player)
        elif loc == "salleDuTrone":
            ret = situations.salleDuTrone.base(d, player)
        elif loc == "taverne":
            ret = situations.taverne.base(d, player)
        elif loc == "terreDeChaisPasOu":
            ret = situations.terreDeChaisPasOu.base(d, player)
        elif loc == "tutorial":
            ret = situations.tutorial.base(d, player)
        elif loc == "villeDeNullepart":
            ret = situations.villeDeNullepart.base(d, player)


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
    client = Client('https://49aa914786e14bd693802f876db91c13:5ce6654ffc3c409c8ff900efcbbe1c60@app.getsentry.com/70494')

    try:
        main()
    except Exception as e:
        client.captureException()
        os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran

        print("Malheureusement, une erreur est survenue (" + str(e) + "). Nous nous en excusons. Veuillez envoyer le rapport d'erreur suivant ainsi qu'un bref résumé des vos actions sur GitHub en suivant le lien suivant : https://github.com/paris-ci/projet-isn/issues")
        #client.user_context({
        #    'last_steps': input("Que venez vous de faire juste avant l'erreur ? >")
        #})
        time.sleep(20)
        print("=== DEBUT RAPPORT ERREUR ENVOYE AUTOMATIQUEMENT===")
        #client.captureException()
        raise

