# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5


import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu("Vous êtes dans le quartier commerçant il énormément de gens.",
                       choices=[("(1)", "Aller chez le marchand de matériaux"),
                                ("(2)", "Aller chez le pharmacien"),
                                ("(3)", "Aller dans les quartier du sud"),
                                ("(4)", "Aller chez le marchand d'armes"),
                                ("(5)", "parler aux gens"),
                                ("(6)", "Revenir a la ville"),
                                ("(7)", "Afficher mon inventaire")],
                       ok_label="Ok, je veux faire ca",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            progress(d, 15, "Vous entrez dans le marchand de matériaux", player)
            database.players.changePref(player, "location", "marchandMateriaux")
            return True
        elif tag == "(2)":
            progress(d, 15, "Vous entrez dans la Pharmacie", player)
            database.players.changePref(player, "location", "pharmacie")
            return True
        elif tag == "(3)":
            if database.inventory.getItemNumber(player, "gourdin") != 0:
                progress(d, 30, "Vous allez dans les quartiers du sud", player)
                database.players.changePref(player, "location", "quartierSud")
            else:
                d.msgbox("Des citadins vous empechent de passer.")
                return True
        elif tag == "(4)":
            progress(d, 15, "Vous allez chez le marchand d'armes", player)
            database.players.changePref(player, "location", "marchandArme")
            return True
        elif tag == "(5)":
            d.msgbox(
                """Vous tentez de parler à un citadin dans une charrette mais il semble trop occupé a hurler "P***** avance!".""")
            return True
        elif tag == "(6)":
            database.players.changePref(player, "location", "centreVille")
            return True

        elif tag == "(7)":
            showInventory(d, player)
            return True
    else:
        return "pref"
