# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# Endroit de base dans le jeu, quand le joueur arrive pour la premiere fois.
import database.inventory
import database.players
from interface import progress

def base(d, player):
    code, tag = d.menu("Donc, que voulez-vous faire ?",
                           choices=[("(1)", "Miner"),
                                    ("(2)", "Creuser"),
                                    ("(3)", "Afficher mon inventaire"),
                                    ("(4)", "Ne rien faire")],
                           ok_label="Ok, je veux faire ca",
                           cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            d.msgbox("Vous minez dans la grotte environnante")
            progress(20, "Je mine...")
            database.inventory.addToInventory(player, "pierre", 10)
            d.msgbox("Vous trouvez 10 pierres.")
        elif tag == "(2)":
            d.msgbox("Vous allez vers le petit bois juste a coté de vous.")
            progress(10, "Je marche vers le bois...")
            d.msgbox("Vous creusez dans ce bois.")
            progress(20, "Je creuse la terre...")
            database.inventory.addToInventory(player, "brindilles", 20)
            database.inventory.addToInventory(player, "terre", 5)
            d.msgbox("Vous trouvez 5 terre et 2 brindilles.")
            progress(10, "Je rentre à la maison...")
        elif tag == "(3)":
            playerInv = database.inventory.getPlayerDict(player)
            message = "Vous avez dans votre inventaire :\n\n"
            for item in playerInv:
                if int(item["quantity"]) != 0:
                    message += item["quantity"] + "x " + item["name"] + "\n"
            d.msgbox(message)
    else:
        return "pref"
