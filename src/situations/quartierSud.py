# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5


import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu("Vous etes dans les quartiers pauvres de la ville.",
                       choices=[("(1)", "Aller dans les montagnes"),
                                ("(2)", "Aller dans la taverne."),
                                ("(3)", "Affronter des bandits(systeme de combat en cours de création)."),
                                ("(4)", "Retourner dans le quartier commerçant."),
                                ("(5)", "Afficher mon inventaire.")],
                       ok_label="Ok je veux faire ça",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            progress(d, 40, "Vous allez dans les montagnes.", player)
            database.players.changePref(player, "location", "montagne")
            return True
        elif tag == "(2)":
            progress(d, 15, "Vous rentrez dans la taverne.", player)
            database.players.changePref(player, "location", "taverne")
            return True
        elif tag == "(3)":
            progress(d, 20, "Vous vous aventurez dans la ville pour trouver des bandits", player)
            database.players.changePref(player, "location", "combatBandit")
            return True
        elif tag == "(4)":
            progress(d, 30, "Vous retournez dans le quartier commerçant.", player)
            database.players.changePref(player, "location", "quartierCommercant")
            return True
        elif tag == "(5)":
            showInventory(d, player)
            return True
    else:
        return "pref"
