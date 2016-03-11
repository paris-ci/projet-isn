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

    table.insert({"name": "or", "quantity": "0"})

def getPlayerDict(player):

    table = connectDB(player)
    playerDict = table.all()

    if playerDict:
        return playerDict
    else:
        return False

def setItemNumber(player, item, number, printIt=True):
    table = connectDB(player)
    if printIt:
        old = table.find_one(name=item)["quantity"]
        if old:
            delta = number - int(old)
            if delta < 0:
                print(str(delta) + "x " + item + " (total: " + str(getItemNumber(player, item)) + ")" )
            elif delta > 0:
                print("+" + str(delta) + "x " + item + " (total: " + str(getItemNumber(player, item)) + ")" )

    data = {"name": item, "quantity": number}
    table.upsert(data, ["name"])

def getItemNumber(player, item):
    table = connectDB(player)
    return int(table.find_one(name=item)["quantity"])