# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# Endroit de base dans le jeu, quand le joueur arrive pour la premiere fois.
# Temps de voyage : Maison => Mine  : 20 secondes
#                   Maison => Foret : 10 secondes

import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu("Donc, que voulez-vous faire ?",
                       choices=[("(1)", "Prendre la route a droite de la porte vers la mine"),
                                ("(2)", "Prendre le sentier vers la foret"),
                                ("(3)", "Afficher mon inventaire")],
                       ok_label="Ok, je veux faire ca",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            progress(d, 20, "Vous allez vers la mine", player)
            database.players.changePref(player, "location", "mine")
            return True
        elif tag == "(2)":
            progress(d, 10, "Vous marchez vers le bois...", player)
            database.players.changePref(player, "location", "bois")
            return True

        elif tag == "(3)":
            showInventory(d, player)
            return True
    else:
        return "pref"
