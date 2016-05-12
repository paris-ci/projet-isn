# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5


import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu("Vous etes chez le marchand de matÃ©riaux. Les prix sont anormalement élevées.",
                       choices=[("(1)", "Demandez au marchand pourquoi les prix sont il si élevés."),
                                ("(2)", "Vendre 10 pierre pour 30 or"),
                                ("(3)", "Vendre 5 terre pour 15 or"),
                                ("(4)", "Vendre 2 brindilles pour 10 or"),
                                ("(5)", "Acheter 10 pierre pour 30 or"),
                                ("(6)", "Acheter 5 terre pour 15 or"),
                                ("(7)", "Acheter 2 brindilles pour 10 or"),
                                ("(8)", "Revenir dans le quartier."),
                                ("(9)", "Afficher mon inventaire")
                                ],
                       ok_label="Ok, je veux faire ca",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            d.msgbox(
                """Le marchand vous répond que la banque "Street Money" à racheté le fournisseur du magasin et qu'il rachète a prix d'or les matériaux.  """)
            return True
        elif tag == "(2)":
            if database.inventory.addToInventory(player, "pierre", -10):
                database.inventory.addToInventory(player, "or", 30)
                d.msgbox(
                    "Vous échangez 10 pierre contre 30 or. Le marchand dit : \"merci pour votre achat, cher voyageur.\"")
                return True
            else:
                d.msgbox("Vous n'avez pas assez de pierre")
        elif tag == "(3)":
            if database.inventory.addToInventory(player, "terre", -5):
                database.inventory.addToInventory(player, "or", 15)
                d.msgbox(
                    "Vous échangez 5 terre contre 15 or. Le marchand dit : \"merci pour votre achat, cher voyageur.\"")
                return True
            else:
                d.msgbox("Vous n'avez pas assez de terre")
        elif tag == "(4)":
            if database.inventory.addToInventory(player, "brindille", -2):
                database.inventory.addToInventory(player, "or", 10)
                d.msgbox(
                    "Vous échangez 2 brindilles contre 10 or. Le marchand dit : \"merci pour votre achat, cher voyageur.\"")
                return True
            else:
                d.msgbox("Vous n'avez pas assez de terre")
                return True
        elif tag == "(5)":
            if database.inventory.addToInventory(player, "pierre", 10):
                database.inventory.addToInventory(player, "or", -30)
                d.msgbox(
                    "Vous échangez 10 pierre contre 30 or. Le marchand dit : \"merci pour votre achat, cher voyageur.\"")
                return True
            else:
                d.msgbox("Vous n'avez pas assez d'or")
        elif tag == "(6)":
            if database.inventory.addToInventory(player, "terre", 5):
                database.inventory.addToInventory(player, "or", -15)
                d.msgbox(
                    "Vous échangez 5 terre contre 15 or. Le marchand dit : \"merci pour votre achat, cher voyageur.\"")
                return True
            else:
                d.msgbox("Vous n'avez pas assez d'or")
            return True
        elif tag == "(7)":
            if database.inventory.addToInventory(player, "terre", 5):
                database.inventory.addToInventory(player, "or", -10)
                d.msgbox(
                    "Vous échangez 2 brindilles contre 10 or. Le marchand dit : \"merci pour votre achat, cher voyageur.\"")
                return True
            else:
                d.msgbox("Vous n'avez pas assez d'or")
        elif tag == "(8)":
            progress(d, 15, "Vous retourner dans le quartier commerçant", player)
            database.players.changePref(player, "location", "quartierCommercant")
            return True

        elif tag == "(9)":
            showInventory(d, player)
            return True
    else:
        return "pref"
