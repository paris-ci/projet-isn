# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# Mine de pierre.
# Temps de voyage : maison => mine : 20 secondes
import database.inventory
import database.players
from util import progress

def base(d, player):
    d.msgbox("Vous minez dans la grotte environnante")
    progress(d, 20, "Vous minez...")
    database.inventory.addToInventory(player, "pierre", 10)
    d.msgbox("Vous trouvez 10 pierres.")
    progress(d, 20, "Vous rentrez de la mine")
    database.players.changePref(player, "location", "maison")
    return True