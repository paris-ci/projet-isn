# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
import database.inventory
import database.players
from util import progress, showInventory


# Temps de voyage : BoutiqueTDCPO => TDCPO : 3 secondes


def base(d, player):
    code, tag = d.menu("Vous etes devant le magasin. Un homme vous propose :",
                       choices=[("(1)", "Vendre 5 terre contre 3 or"),
                                ("(2)", "Vendre 10 pierres contre 4 or"),
                                ("(3)", "Acheter 5 terre contre 3 or"),
                                ("(4)", "Acheter 10 pierres contre 4 or"),
                                ("(5)", "Parler à l'Homme."),
                                ("(6)", "Repartir dans la plaine"),
                                ("(7)", "Afficher mon inventaire")
                                ],
                       ok_label="Ok, je veux faire ca",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            if database.inventory.addToInventory(player, "terre", -5):
                database.inventory.addToInventory(player, "or", 3)
                d.msgbox(
                    "Vous échangez 5x terre contre 3x or. Le marchand dit : \"merci pour votre achat, cher voyageur.\"")
                return True
            else:
                d.msgbox("Vous n'avez pas asser de terre.")
                return True

        elif tag == "(2)":
            if database.inventory.addToInventory(player, "pierre", -10):
                database.inventory.addToInventory(player, "or", 4)
                d.msgbox(
                    "Vous échangez 10x pierres contre 4x or. Le marchand dit : \"merci pour votre achat, cher voyageur.\"")
                return True
            else:
                d.msgbox("Vous n'avez pas asser de pierres.")
                return True
        elif tag == "(3)":
            if database.inventory.addToInventory(player, "or", -3):
                database.inventory.addToInventory(player, "terre", 5)
                d.msgbox(
                    "Vous échangez 3x or contre 5x terre. Le marchand dit : \"merci pour votre achat, cher voyageur.\"")
                return True
            else:
                d.msgbox("Vous n'avez pas assez d'or.")

        elif tag == "(4)":
            if database.inventory.addToInventory(player, "or", -4):
                database.inventory.addToInventory(player, "pierre", 10)
                d.msgbox(
                    "Vous échangez 4x or contre 10x terre. Le marchand dit : \"merci pour votre achat, cher voyageur.\"")

        elif tag == "(5)":
            if database.inventory.getItemNumber(player, "lunettes") <= 0:
                d.msgbox("""Que faites vous dans ce coin perdu ? Vous ne voulez pas rejoindre la ville ?
Comment ca quelle ville ? Mais la ville de NullePart pardi. Tu n'as pas vu le panneau ?
Prendss mes lunettes et vas-y !""")
                database.inventory.addToInventory(player, "lunettes", 1)
            else:
                d.msgbox("As-tu pu visiter la ville ?")

        elif tag == "(6)":
            progress(d, 3, "Vous rebroussez chemain vers la plaine")
            database.players.changePref(player, "location", "terreDeChaisPasOu")
            return True

        elif tag == "(7)":
            showInventory(d, player)
            return True
    else:
        return "pref"
