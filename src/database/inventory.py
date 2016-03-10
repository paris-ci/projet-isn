# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

# Constants #

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

import dataset


def connectDB(player):
    return dataset.connect('sqlite:///databases/inventory.db')[player]


def createInventory(player):
    table = connectDB(player)

    table.insert({"or": 0, "exp":0})

def playerDict(player):

    table = connectDB(player)
    playerDict = table.all()

    if playerDict:
        return playerDict
    else:
        return False

def setItemNumber(player, item, number):
    table = connectDB(player)
    data = {item: number}
    table.upsert(data, [item])
