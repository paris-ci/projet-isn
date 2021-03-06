# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu("Vous etes arrivé a la ville de NullePart. La ville est grande. Il y a quelques passants. ",
                       choices=[("(1)", "Aller au centre ville"),
                                ("(2)", "Prendre le bus jusqu'à la maison (2x or)"),
                                ("(3)", "Rentrer vers la pleine"),
                                ("(4)", "Afficher mon inventaire")
                                ],
                       ok_label="Ok, je veux faire ca",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            progress(d, 15, "Vous marchez jusqu'au centre ville.", player)
            database.players.changePref(player, "location", "centreVille")
            return True
        elif tag == "(2)":
            if database.inventory.addToInventory(player, "or", -2):
                progress(d, 10, "Le bus vous ramene chez vous.", player)
                database.players.changePref(player, "location", "maison")
                return True
            else:
                d.msgbox("Impossible. Vous n'avez pas asser d'argent !")
                return True

        elif tag == "(3)":
            progress(d, 60, "Vous rebroussez chemain vers la plaine", player)
            database.players.changePref(player, "location", "terreDeChaisPasOu")
            return True

        elif tag == "(4)":
            showInventory(d, player)
            return True
    else:
        return "pref"
