# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# Endroit de base dans le jeu, quand le joueur arrive pour la premiere fois.
import database.inventory
import database.players
from util import progress

def base(d, player):
    code, tag = d.menu("Donc, que voulez-vous faire ?",
                           choices=[("(1)", "Miner"),
                                    ("(2)", "Creuser"),
                                    ("(3)", "Afficher mon inventaire")],
                           ok_label="Ok, je veux faire ca",
                           cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            progress(d, 20, "Vous allez vers la mine")
            database.players.changePref(player, "location", "mine")
            return True
        elif tag == "(2)":
            d.msgbox("Vous allez vers le petit bois juste a coté de vous.")
            progress(d, 10, "Je marche vers le bois...")
            database.players.changePref(player, "location", "mine")
            return True

        elif tag == "(3)":
            playerInv = database.inventory.getPlayerDict(player)
            message = "Vous avez dans votre inventaire :\n\n"
            for item in playerInv:
                if int(item["quantity"]) != 0:
                    message += item["quantity"] + "x " + item["name"] + "\n"
            d.msgbox(message)
    else:
        return "pref"
