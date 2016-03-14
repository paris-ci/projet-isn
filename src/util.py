# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

# Constants #

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

import time

import database.inventory


def progress(d, pause, text):
    d.gauge_start(text=text)
    for i in range(0, 100):
        d.gauge_update(i)
        time.sleep(pause / 100)

    d.gauge_stop()


def showInventory(d, player):
    playerInv = database.inventory.getPlayerDict(player)
    message = "Vous avez dans votre inventaire :\n\n"
    for item in playerInv:
        if int(item["quantity"]) != 0:
            message += item["quantity"] + "x " + item["name"] + "\n"
    d.msgbox(message)
