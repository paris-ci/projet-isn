# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
import database.inventory
import database.players
from util import progress

def base(d, player):
    d.msgbox("Vous minez dans la grotte environnante")
    progress(d, 20, "Je mine...")
    database.inventory.addToInventory(player, "pierre", 10)
    d.msgbox("Vous trouvez 10 pierres.")
    database.players.changePref(player, "location", "maison")
    return True