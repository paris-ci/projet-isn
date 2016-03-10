# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

# Constants #

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

import sqlite3
import time


class players:


    def init_players():
        conn = sqlite3.connect('./databases/players.db')
        c = conn.cursor()
        # Create table
        c.execute('''CREATE TABLE players
               (pseudo text, password text, datejoined text, lastconnexiondate real)''')
        # Save (commit) the changes
        conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()


    def newplayer(pseudo, plainTextPassword):
        conn = sqlite3.connect('./databases/players.db')
        c = conn.cursor()

        # Insert a row of data
        t = (pseudo, plainTextPassword, time.time(), time.time(),)
        c.execute('INSERT INTO players VALUES (?,?,?,?)', t)

        # Save (commit) the changes
        conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()

    def playerExist(pseudo):
        conn = sqlite3.connect('./databases/players.db')
        c = conn.cursor()

        t = (pseudo,)
        c.execute('''SELECT EXISTS(SELECT 1 FROM players WHERE pseudo=? LIMIT 1);''', t)
        return True

