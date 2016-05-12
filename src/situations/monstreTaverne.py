# Créé par tflecheux, le 04/05/2016 en Python 3.2
# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5



import random

import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    vie_joueur = database.inventory.getItemNumber(player, "vie")
    vie_adversaire = 15
    code, tag = d.menu("Vous etes entrain de combattre un bandit, il vous reste " + str(vie_joueur) + "point de santé",
                       choices=[("(1)", "Combattre"),
                                ("(2)", "Utiliser un objet"),
                                ("(3)", "Fuire"),
                                ("(4)", "Afficher mon inventaire")],
                       ok_label="Ok je veux faire ça",
                       cancel_label="Préférences/Quitter")

    if code == d.OK:

        if vie_joueur <= 0:
            d.msgbox("Vous avez perdu :'(")
            database.players.changePref(player, "location", "maison")
        if vie_adversaire <= 0:
            d.msgbox("Vous avez gagné :)")
            database.players.changePref(player, "location", "")
        if tag == "(1)":
            chance = random.randrange(1, 100)
            if chance < 6:
                vie_adversaire = vie_adversaire - 3
                d.msgbox("Vous ifliger de gros dégat a votre énnemi.")
                return True
            elif 5 < chance < 51:
                vie_adversaire = vie_adversaire - 1
                d.msgbox("Vous arrivez à blesser votre énnemi.")
                return True
            elif 94 < chance:
                database.inventory.addToInventory(player, "vie", -3)
                d.msgbox("Vous vous cassez la jambe. ")
                return True
            else:
                database.inventory.addToInventory(player, "vie", -1)
                d.msgbox("Votre énnemi vous blesse.")

                return True

        elif tag == "(2)":
            code, tag = d.menu("Quel objet voulez vous utiliser?",
                               choices=[("(1)", "Bombe"),
                                        ("(2)", "Potion"),
                                        ("(3)", "Afficher mon inventaire.")],
                               ok_label="Ok je veux utiliser ça",
                               cancel_label="Préférances/Quitter")
            if tag == "(1)":
                if database.inventory.getItemNumber(player, "bombe") >= 1:
                    database.inventory.addToInventory(player, "bombe", -1)
                    vie_adversaire = -3
                    d.msgbox("Vous utiliser une bombe.")
                    return True
                else:
                    d.msgbox("Vous n'avez pas assez de bombes.")
                    return True

            elif tag == "(2)":
                if database.inventory.addToInventory(player, "potion", -1):
                    database.inventory.addToInventory(player, "vie", 2)
                    d.msgbox("Vous utilisez une potion")
                    return True
                else:
                    d.msgbox("Vous n'avez pas assez de potions.")
                    return True
            elif tag == "(3)":
                progress(d, 10, "Vous prenez la fuite.", player)
                database.players.changePref(player, "location", "maison")
                return True
            elif tag == "(4)":
                showInventory(d, player)
                return True
        else:
            return "pref"
