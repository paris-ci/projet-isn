# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5


import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu("CET ENDROIT N'EXISTE PAS ENCORE !?",
                       choices=[("(1)", "---"),
                                ("(2)", "Revenir a la ville"),
                                ("(3)", "Afficher mon inventaire")],
                       ok_label="Ok, je veux faire ca",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            return True
        elif tag == "(2)":
            database.players.changePref(player, "location", "centreVille")
            return True

        elif tag == "(3)":
            showInventory(d, player)
            return True
    else:
        return "pref"
