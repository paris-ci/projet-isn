# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5


import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu("Vous etes chez le marchand de bombes.",
                       choices=[("(1)", "Achetez un bombes"),
                                ("(2)", "Sortir du magasin"),
                                ("(3)", "Afficher mon inventaire")],
                       ok_label="Ok, je veux faire ca",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            if database.inventory.addToInventory(player, "bombe", 3):
                database.inventory.addToInventory(player, "or", -40)
                d.msgbox("Vous achetez 3 bombe, faites attention avec")
                return True
            else:
                d.msgbox("Vous n'avez pas assez d'or")
                return True
        elif tag == "(2)":
            progress(d, 15, "Vous sortez du magasin.", player)
            database.players.changePref(player, "location", "quartierCommercant")
            return True
        elif tag == "(3)":
            showInventory(d, player)
            return True

    else:
        return "pref"
