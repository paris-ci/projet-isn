# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5


import database.inventory
import database.players
from util import progress


def base(d, player):
    code, tag = d.menu("Vous etes dans la pharmacie",
                       choices=[("(1)", "Acheter une potion de soin (15 or)"),
                                ("(2)", "Acheter du chocolay noir (10 or)"),
                                ("(3)", "Regarder les affiches de publicités"),
                                ("(4)", "Retourner dans le quartier"),
                                ("(5)", "Afficher mon inventaire")
                                ],
                       ok_label="Ok, je veux faire ca",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            if database.inventory.addToInventory(player, "or", -15):
                database.inventory.addToInventory(player, "potion", 1)
                d.msgbox("Vous avez acheté une potion de soin")
                return True
            else:
                d.msgbox("Vous n'avez pas assez d'or.")
        elif tag == "(2)":
            if database.inventory.addToInventory(player, "or", -15):
                database.inventory.addToInventory(player, "chocolat", 1)
                d.msgbox("Vous avez acheté du chocolat,")
                return True
            else:
                d.msgbox("Vous n'avez pas assez d'or.")
        elif tag == "(3)":
            code, tag = d.menu("Vous regardez les affiches",
                               choices=[("(1)", "Regarder l'affiche de droite"),
                                        ("(2)", "Regarder l'affiche de gauche")
                                        ],
                               ok_label="Regarder",
                               cancel_label="Ne pas regarder les affiches")
            if code == d.OK:
                if tag == "(1)":
                    d.msgbox("L'affiche est un publicité pour insectiside, le slogan est  \"bugs everywhere\".")
                elif tag == "(2)":
                    d.msgbox(
                        "L'affiche est celle d'unje société appelée Arperture Science Il y a un grand robot sur l'affiche qui s'appelle GlaDos")
            else:
                d.msgbox("Vous arrétez de regarder les affiches.")

        elif tag == "(4)":
            progress(d, 15, "Vous sortez du magasin", player)
            database.players.changePref(player, "location", "quartierCommercant")
            return True

        else:
            return "pref"
