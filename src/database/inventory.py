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

def deleteInventory(player):
    table = connectDB(player)
    table.drop()


def getPlayerDict(player):
    table = connectDB(player)
    playerDict = table.all()

    if playerDict:
        return playerDict
    else:
        return False


def setItemNumber(player, item, number, printIt=False):
    table = connectDB(player)
    if printIt:
        old = getItemNumber(player, item)
        delta = number - int(old)
        if delta < 0:
            print(str(delta) + "x " + item + " (total: " + str(getItemNumber(player, item)) + ")")
        elif delta > 0:
            print("+" + str(delta) + "x " + item + " (total: " + str(getItemNumber(player, item)) + ")")

    data = {"name": item, "quantity": number}
    table.upsert(data, ["name"])


def getItemNumber(player, item):
    table = connectDB(player)
    try:
        number = int(table.find_one(name=item)["quantity"])
        return number

    except TypeError:
        return 0


def addToInventory(player, item, number):
    if number < 0:
        if getItemNumber(player, item) < - number:
            return False
    setItemNumber(player, item, getItemNumber(player, item) + number)
    return True
