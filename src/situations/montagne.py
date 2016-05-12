# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5


import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu("Vous ètes dans les montagnes, il y a un chateau et une caverne.",
                       choices=[("(1)", "Aller dans le chateau"),
                                ("(2)", "Aller dans la caverne."),
                                ("(3)", "Retourner dans la ville."),
                                ("(4)", "Afficher mon inventaire.")],
                       ok_label="Ok je veux faire ça",
                       cancel_label="Préférance/Quitter")
    if code == d.OK:
        if tag == "(1)":
            progress(d, 30, "Vous allez dans le chateau.", player)
            database.players.changePref(player, "location", "chateauMontagne")
            return True
        elif tag == "(2)":
            progress(d, 20, "Vous rentrez dans la grotte, mais il s'agit d'un repère de brigand", player)
            database.players.changePref(player, "location", "caverne")
            return True
        elif tag == "(3)":
            progress(d, 30, "Vous retournez dans la ville.", player)
            database.players.changePref(player, "location", "quartierSud")
            return True
        elif tag == "(4)":
            showInventory(d, player)
            return True
        else:
            return "pref"
