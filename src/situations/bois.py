# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# Le bois prés de la maison, pour trouver des brindilles et de la terre
# Temps de voyage : maison => bois : 10 secondes
import database.inventory
import database.players
from util import progress

def base(d, player):
    d.msgbox("Vous creusez dans ce bois.")
    progress(d, 20, "Vous creusez la terre...")
    database.inventory.addToInventory(player, "brindilles", 20)
    database.inventory.addToInventory(player, "terre", 5)
    d.msgbox("Vous trouvez 5 terre et 2 brindilles.")
    progress(d, 10, "Vous rentrez à la maison...")
    database.players.changePref(player, "location", "bois")
    return True