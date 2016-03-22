# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# Le bois prés de la maison, pour trouver des brindilles et de la terre
import database.players
from util import progress


def base(d, player):
    code, tag = d.menu("Vous etes au milieu du centre ville. il y a beaucoup de monde",
                       choices=[("(1)", "S'asseoir par terre"),
                                ("(2)", "Aller dans le quartier commerçant"),
                                ("(3)", "Aller au poste de police"),
                                ("(4)", "Aller au chateau"),
                                ("(5)", "Retourner à l'entrée de la ville")
                                ],
                       ok_label="OK, je veux faire ca",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            progress(d, 60, "Un policier vous prend pour un mendiant et vous envoie en prison", player)
            database.players.changePref(player, "location", "posteDePolice")
        elif tag == "(2)":
            progress(d, 15, "Vous allez au quartier commerçant", player)
            database.players.changePref(player, "location", "quartierCommercant")
            return True
        elif tag == "(3)":
            progress(d, 15, "Vous allez au poste de police", player)
            database.players.changePref(player, "location", "posteDePolice")
            return True
        elif tag == "(4)":
            progress(d, 15, "Vous allez au chateau", player)
            database.players.changePref(player, "location", "chateau")
            return True
        elif tag == "(5)":
            progress(d, 15, "Vous allez à l'entrée de la ville", player)
            database.players.changePref(player, "location", "villeDeNullepart")
            return True

    else:
        return "pref"
