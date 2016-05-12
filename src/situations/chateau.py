# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5


import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu("Vous entrez dans le chateau il est tres grand.",
                       choices=[("(1)", "Parler aux gardes"),
                                ("(2)", "Aller à la salle du trone"),
                                ("(3)", "Revenir a la ville"),
                                ("(4)", "Afficher mon inventaire")],
                       ok_label="Ok, je veux faire ça",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            d.msgbox(
                """Les gardes vous interpellent sans vous laiser le temps de parler  "Vous ètes ici pour teter d'arretez le Sorcier? aller à la salle du trone""")
            code, tag = d.menu("Que dire ?",
                               choices=[
                                   ("(1)", "Le sorcier ?"),
                                   ("(2)", "Oui c'est exactement cela!")
                               ],
                               ok_label="Dire ça",
                               cancel_label="mettre fin à la conversation")
            if code == d.OK:
                if tag == "(1)":
                    d.msgbox("Oui le Sorcier qui est la cause de tous les problème. D'ou sortez vous? bon sang!")
                elif tag == "(2)":
                    d.msgbox("Encore un prétentieux qui va mourir.")
                else:
                    d.msgbox("Vous dites au revoir aux gardes")
                    return True
            else:
                return "pref"
        elif tag == "(2)":
            progress(d, 15, "Vous allez dans la salle du trone", player)
            database.players.changePref(player, "location", "salleDuTrone")
        elif tag == "(3)":
            database.players.changePref(player, "location", "centreVille")
            return True

        elif tag == "(4)":
            showInventory(d, player)
            return True
    else:
        return "pref"
