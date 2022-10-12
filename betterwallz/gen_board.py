from PIL import Image
from random import randint
from assets import AlgorithmeDePrim


def generate_board(size=23):
	"""Préparation du tableau - map | génération aléatoire d'un labyrinthe en matrice 
	 puis traitement image pour un visuel sur la map durant la partie """

	labyrinthe = AlgorithmeDePrim.generate_labyrinthe(size, size)
	black = Image.open(r"./assets/board/black.png")
	white = Image.open(r"./assets/board/white.png")
	blue = Image.open(r"./assets/board/blue.png")
	red = Image.open(r"./assets/board/red.png")

	# Pour un moi futur : oui, il est nécéssaire de le faire en deux fois (actualiser la matrice)

	iX = 0
	for X in labyrinthe:
		iY = 0
		for Y in X:

			#ajout de passages avant traitement image (10%)
			#conditions pour pas faire de trous dans le contour (46, rappel de l'algo laby X*2+1)
			if Y == 0 and not iX == 0 and not iX == 46 and not iY == 0 and not iY == 46:
				hole_choice = randint(0,10)
				if hole_choice == 0:
					labyrinthe[iX][iY] = 1

			iY += 1
		iX += 1


	iX = 0
	for X in labyrinthe:
		iY = 0
		for Y in X:

			#traitement image
			if Y == 0:
				Image.Image.paste(white, black, (iY*31, iX*31))
			if Y == 2:
				Image.Image.paste(white, blue, (iY*31, iX*31))
				spawn_xp1 = iX*31
				spawn_yp1 = iY*31
			if Y == 3:
				Image.Image.paste(white, red, (iY*31, iX*31))
				spawn_xp2 = iX*31
				spawn_yp2 = iY*31

			iY += 1
		iX += 1

	white = white.save("board.png")

	return "Completed", spawn_yp1, spawn_xp1, spawn_yp2, spawn_xp2, labyrinthe
# pour un moi futur : c'est tt inversé dans ce code mais ca marche
#donc pas touche
#	return "Completed", spawn_xp1, spawn_yp1, spawn_xp2, spawn_yp2, labyrinthe