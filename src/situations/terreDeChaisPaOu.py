# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# Endroit de base dans le jeu, quand le joueur arrive pour la premiere fois.
# Temps de voyage : TDCPO => Foret  : 25 secondes
#                   TDCPO => BoutiqueTDCPO : 3 secondes


import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu("Vous etes dans une grande pleine. Un panneau indique : \"terre de chais pas où\". Il semble y avoir une boutique un peu plus loin.",
                       choices=[("(1)", "Aller dans le magasin"),
                                ("(2)", "Rentrer à la fôret"),
                                ("(3)", "Afficher mon inventaire")
                                ],
                       ok_label="Ok, je veux faire ca",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            progress(d, 3, "Vous allez vers la boutique.")
            database.players.changePref(player, "location", "magasinTDCPO")
            return True
        elif tag == "(2)":
            progress(d, 25, "Vous rebroussez chemain vers la forèt")
            database.players.changePref(player, "location", "bois")
            return True

        elif tag == "(3)":
            showInventory(d, player)
            return True
    else:
        return "pref"

