# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5


import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu("Vous entrez dans la salle du trone.",
                       choices=[("(1)", "Parler au roi"),
                                ("(2)", "quitter la salle du trone"),
                                ("(3)", "afficher mon inventaire")],
                       ok_label="Ok,je veux faire ça",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            d.msgbox("Vous vous avancez pour parler au roi, celui ci vous demande  ce que vous faites ici.")
            code, tag = d.menu("Que dire ?",
                               choices=[
                                   ("(1)", "je suis venu ici pour vaincre le sorcier."),
                                   ("(2)", "je ne fais que visiter.")
                               ],
                               ok_label="Dire ça",
                               cancel_label="mettre fin à la conversation")
            if code == d.OK:
                if tag == "(1)":
                    d.msgbox("J'espere que vous serez à la hauteur.")
                elif tag == "(2)":
                    d.msgbox("Eh bien bien bonne journée.")
                else:
                    d.msgbox("vous dites au revoir au roi")
                    return True
            else:
                return "pref"
        elif tag == "(2)":
            progress(d, 15, "Vous quittez la salle du trone", player)
            database.players.changePref(player, "location", "chateau")
            return True

        elif tag == "(3)":
            showInventory(d, player)
            return True
    else:
        return "pref"
