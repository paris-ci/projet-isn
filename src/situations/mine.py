# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# Mine de pierre.
# Temps de voyage : maison => mine : 20 secondes
import database.inventory
import database.players
from util import progress, showInventory

def base(d, player):

    code, tag = d.menu("Vous êtes à la mine. Que voulez-vous faire ?",
                       choices=[("(1)", "Miner dans la mine de pierre"),
                                ("(2)", "Rentrer à la maison"),
                                ("(3)", "Afficher mon inventaire")],
                       ok_label="Ok, je veux faire ca",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            d.msgbox("Vous minez dans la grotte environnante")
            progress(d, 20, "Vous minez...")
            database.inventory.addToInventory(player, "pierre", 10)
            d.msgbox("Vous trouvez 10 pierres.")
            return True
        elif tag == "(2)":
            progress(d, 20, "Vous rentrez de la mine")
            database.players.changePref(player, "location", "maison")
            return True
        elif tag == "(3)":
            showInventory(d, player)
            return True
    else:
        return "pref"