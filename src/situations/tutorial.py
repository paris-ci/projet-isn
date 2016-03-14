# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
# Endroit invisible qui sert de tutorial.

import database.players

def base(d, player):
    d.msgbox("""Bienvenue sur ce RPG, """ + player + """.
Je suis le MJ. Je vais t'apprendre les bases du jeu, afin que tu puisse t'en sortir une fois laché dans la nature.
Ce jeu est composé de choix à faire au travers d'un menu. Selectionnez les à l'aide du clavier, ou de la souris afin de les executer.
Votre but est de devenir le plus riche joueur dans ce jeu.
Il y à aussi quelques secrets, mais je te fais confience pour les trouver...
Je vais te déposer à ta maison, d'ou tu pourra débuter ton aventure.
Bon jeu!""")
    database.players.changePref(player, "location", "maison")
    return True

