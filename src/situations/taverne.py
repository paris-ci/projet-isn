# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5


import database.inventory
import database.players


def base(d, player):
    code, tag = d.menu("Vous ètes dans la taverne, le propriétaire de la taverne est en train de parler d'un sorcier",
                       choices=[("(1)", "questionner au propriétaire"),
                                ("(2)", "Acheter une bière"),
                                ("(3)", "Sortir de la taverne."),
                                ("(4)", "Afficher mon inventaire.")],
                       ok_label="Ok je veux faire ça",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            d.msgbox("Le tavenier vous demande \"D'ou sortez vous pour ne pas avoir entendu parler du sorcier\".")

        elif tag == "(2)":
            if database.inventory.addToInventory(player, "or", -30):
                d.msgbox("Vous acheter une bière pour 30 or")
                return True
            else:
                d.msgbox("Vous n'avez pas assez d'or")
                return True
    else:
        return "pref"
