# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

# Constants #

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

import time
import dataset


def connectDB():
    return dataset.connect('sqlite:///databases/players.db')["players"]

def init_players():
    connectDB()

def newplayer(pseudo, plainTextPassword):
    table = connectDB()

    table.insert({"pseudo": pseudo, "password":plainTextPassword, "timeJoined": int(time.time()), "lastConnect": time.time()})

def playerExist(pseudo):

    table = connectDB()

    if table.find_one(pseudo=pseudo):
        return True
    else:
        return False

def playerDict(pseudo):

    table = connectDB()
    player = table.find_one(pseudo=pseudo)

    if player:
        return player
    else:
        return False
