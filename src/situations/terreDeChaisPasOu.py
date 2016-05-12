# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# Endroit de base dans le jeu, quand le joueur arrive pour la premiere fois.
# Temps de voyage : TDCPO => Foret  : 25 secondes
#                   TDCPO => BoutiqueTDCPO : 3 secondes


import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu(
        "Vous etes dans une grande pleine. Un panneau indique : \"terre de chais pas où\". Le reste du panneau est effacé. Il semble y avoir une boutique un peu plus loin.",
        choices=[("(1)", "Aller dans le magasin"),
                 ("(2)", "Continuer sur le sentier"),
                 ("(3)", "Rentrer à la fôret"),
                 ("(4)", "Afficher mon inventaire")
                 ],
        ok_label="Ok, je veux faire ca",
        cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            progress(d, 3, "Vous allez vers la boutique.", player)
            database.players.changePref(player, "location", "magasinTDCPO")
            return True
        elif tag == "(2)":
            if database.inventory.getItemNumber(player, "lunettes") != 0:
                progress(d, 60, "Vous continuez sur le sentier. Il est quasiment invisible.", player)
                database.players.changePref(player, "location", "villeDeNullepart")
                return True
            else:
                d.msgbox("Impossible. Le chemin est presque indiscernable à partir d'ici !")
                return True

        elif tag == "(3)":
            progress(d, 25, "Vous rebroussez chemin vers la forèt", player)
            database.players.changePref(player, "location", "bois")
            return True

        elif tag == "(4)":
            showInventory(d, player)
            return True
    else:
        return "pref"
