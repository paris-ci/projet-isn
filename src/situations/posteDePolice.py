# Créé par tflecheux, le 17/03/2016 en Python 3.2
import database.inventory
import database.players
from util import progress, showInventory


def base(d, player):
    code, tag = d.menu("Vous rentrez dans le poste de police, vous êtes entouré par des policiers qui travaillent.",
                       choices=[("(1)", "Parler à un policier"),
                                ("(2)", "Rentrer dans la prison"),
                                ("(3)", "Sortir du poste de police"),
                                ("(4)", "Afficher l'inventaire")
                                ],
                       ok_label="OK, je veux faire ca",
                       cancel_label="Préférances/Quitter")
    if code == d.OK:
        if tag == "(1)":
            if database.inventory.getItemNumber(player, "gourdin") <= 0:
                d.msgbox("""Faites attention dans les quartiers malfamés de la ville.""")
                code, tag = d.menu("Que dire ?",
                                   choices=[
                                       ("(1)", "Quels quartiers?"),
                                       ("(2)", "D'accord")
                                   ],
                                   ok_label="Dire ca",
                                   cancel_label="Partir en courant")
                if code == d.OK:

                    if tag == "(1)":
                        d.msgbox(
                            "Vous, vous êtes pas d'ici non?\nPrenez ça pour vous défendre mais ne l'utilisez qu'en cas de défence, c'est clair ?")
                        database.inventory.addToInventory(player, "gourdin", 1)
                    elif tag == "(2)":
                        d.msgbox("Sur ce, bonne journée et ne causez pas de troubles")
                else:
                    d.msgbox("Le policier vous ratrappe, vous trouve suspect et vous envoie en prison")
                    database.players.changePref(player, "location", "posteDePolice")


            else:
                d.msgbox("Faites attention dans les quartiers du sud, Mais ne faites pas l'idiot avec ce gourdin")

        elif tag == "(2)":
            progress(d, 5, "Vous là! Vous essayez de libérer des prisonniers,\nça tombe bien vous allez les rejoindre",
                     player)
            database.players.changePref(player, "location", "prison")
            return True

        elif tag == "(3)":
            progress(d, 15, "Vous sortez du poste de police", player)
            database.players.changePref(player, "location", "centreVille")
            return True

        elif tag == "(4)":
            showInventory(d, player)
            return True

    else:
        return "pref"
