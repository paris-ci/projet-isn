# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5


import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu("Les policier vous ont enfermés dans la prison, mais le geôlier vous libère.",
                       choices=[("(1)", "Parler au geôlier"),
                                ("(2)", "Tenter de libérer les prisonniers"),
                                ("(3)", "Revenir a la ville"),
                                ("(4)", "Afficher mon inventaire")],
                       ok_label="Ok, je veux faire ca",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            d.msgbox("""C'est ici que nous gardons les criminels qui ont été arrétés.""")
            code, tag = d.menu("Que dire ?",
                               choices=[
                                   ("(1)", "Les criminels?"),
                                   ("(2)", "D'accord ,donc sans vous ce serait l'anarchie.")
                               ],
                               ok_label="Dire ça",
                               cancel_label="mettre fin à la conversation")
            if code == d.OK:
                if tag == "(1)":
                    d.msgbox("Oui, cette ville regorge de fripouille en tous genre. Alors faites attention.")
                elif tag == "(2)":
                    d.msgbox("ça fais plaisir de voir que la jeune génération respecte mon travail.")
            else:
                d.msgbox("vous dites au revoir au geôlier")

        elif tag == "(2)":
            r = database.inventory.addToInventory(player, "or", -150)
            if not r:
                progress(d, 200,
                         "Votre tentative est stoppée net par le geôlier qui vous enferme. Vous n'avez pas assez d'or pour écourter votre peine.", player)
            else:
                progress(d, 120,
                         "Vous tenter de libérer les prisonniers, mais le geôlier vous en empeche et vous arrète. Vous avez une amende de 50 pièce d'or", player)
            return True

        elif tag == "(3)":
            database.players.changePref(player, "location", "centreVille")
            return True

        elif tag == "(4)":
            showInventory(d, player)
            return True
    else:
        return "pref"
