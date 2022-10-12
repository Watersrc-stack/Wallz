import tkinter
from game import Game

"""
Corridors and walls : jeu à deux joueurs / en ligne / TpT
But : Trouver et eliminer l'autre avant de perdre toutes ses vies
Déroulement :
Income fixe à chaque tour, plusieurs items a acheter (torches, pièges, potions...)
Loot random sur la map

Labyrinthe gruyère 10%, map triple calque (walls/loot/fog)
"""

app = tkinter.Tk()
app.title("Wallz")
app.geometry("400x500")


def scale_size(value):
	pass


def create_game():
	game = Game()
	game.create(int( (slider.get() -1) / 2) )

slider = tkinter.Scale(app, from_=47, to=11, orient=tkinter.VERTICAL, length=100, tickinterval=12, resolution=2, command=scale_size)
slider.set(61)
slider.pack()

size_label = tkinter.Label(app, text="Laby size")
size_label.pack(padx=20, pady=0)

try:
	button_create = tkinter.Button(app, text="Create game", command=create_game)
	button_create.pack(pady=50)
except ClassAttributeError as cae:
	print(cae)
except WoullaCestPasNet as wcpn:
	print(wcpn)


app.mainloop()