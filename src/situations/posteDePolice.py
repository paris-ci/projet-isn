# Créé par tflecheux, le 17/03/2016 en Python 3.2
import database.inventory
import database.players
from util import progress, showInventory

def base(d, player):
    code, tag = d.menu("Vous dans le poste de police, vous  etes entourés par des policiers qui travaille.",
                        choices=[("(1)", "Parler à un policier"),
                        ("(2)", "Rentrer dans la prison"),
                        ("(3)", "Sortir du poste de police"),
                        ("(4)", "Afficher l'inventaire")
                        ],
                ok_label="OK, je veux faire ca",
                cancel_label="en fait non je veux plus")
    if code == d.OK:
        if tag == "(1)":
            if database.inventory.getItemNumber(player, "gourdin") <= 0:
                d.msgbox("""Faites attention dans les quartiers malfamés de la ville.Comment ça les quartiers malfamés?
                  Oui les quartiers du sud ils regorgent de malfrats,alors faites attention si vous y aller.
                  D'accord merci. Prenez ça pour vous défendre """)
                  database.inventory.addToInventory(player, "gourdin", 1)
            else:
                d.msgbox("Faites attention dans les quartiers du sud, Mais ne faites pas l'idiot avec ce gourdin")

            elif tag == "(2)":
                progress(d,5, "Vous rentrez dans la prison")
                database.players.changePref(player, "location", "prison")
                return True

            elif tag == "(3)":
                progress(d,15, "Vous sortez du poste de police")
                database.players.changePref(player, "location", "centreVille")
                return True

            elif tag == "(4)":
                showInventory(d, player)
                return True
    else:
        return "pref"
