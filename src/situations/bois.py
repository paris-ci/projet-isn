# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# Le bois prés de la maison, pour trouver des brindilles et de la terre
# Temps de voyage : maison => bois : 10 secondes
import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu("Vous êtes dans le petit bois. Que voulez-vous faire ?",
                       choices=[("(1)", "Fouiller la terre"),
                                ("(2)", "Continuer sur ce sentier"),
                                ("(3)", "Rentrer à la maison"),
                                ("(4)", "Afficher mon inventaire")],
                       ok_label="Ok, je veux faire ca",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            d.msgbox("Vous creusez dans ce bois.")
            progress(d, 20, "Vous creusez la terre...", player)
            database.inventory.addToInventory(player, "brindilles", 20)
            database.inventory.addToInventory(player, "terre", 5)
            d.msgbox("Vous trouvez 5 terre et 2 brindilles.")
            return True
        elif tag == "(2)":
            progress(d, 25, "Vous continuez sur le sentier... Il semble en bien plus mauvais état !", player)
            database.players.changePref(player, "location", "terreDeChaisPasOu")
            return True
        elif tag == "(3)":
            progress(d, 10, "Vous rentrez à la maison...", player)
            database.players.changePref(player, "location", "maison")
            return True
        elif tag == "(4)":
            showInventory(d, player)
            return True
    else:
        return "pref"
