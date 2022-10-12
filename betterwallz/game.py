import tkinter
from PIL import Image
from gen_board import generate_board
from pynput.keyboard import Key, Listener

class ClassAttributeError(Exception):
	pass

class WoullaCestPasNet(Exception):
	pass

class Player():
	"""docstring for Player
	Class used two times, one time per player"""
	def __init__(self, other, posx, posy, playerpng):
		super(Player, self).__init__()
		self.x = posx
		self.y = posy
		#x et y en pixel, pas en position matrice
		self.png = playerpng
		self.ID = self
		self.MATx = self.x / 31
		self.MATy = self.y / 31
		self.game = other


	def spawn(self, other):
	
		self.id_png = other.canvas_display_calque1.create_image(self.x, self.y, image=self.png, anchor="nw")
		other.canvas_display_calque1.pack(fill="both", expand=False)


	def center_display(self):
		pass


	def move(self, direction: tuple):
		self.FLIP()


	def move_up(useless_arg_but_bind, self):
		print("Player moved up")
		pass

	def move_down(useless_arg_but_bind, self):
		print("Player moved down")
		pass

	def move_left(useless_arg_but_bind, self):
		print("Player moved left")		
		Game.FLIP()

	def move_right(useless_arg_but_bind, self):
		print("Player moved right")
		pass


class Case():


	def __init__(self, state, other):

		self._game_other_ = other
		self.player_on = None
		if state not in [0, 1, 2, 3]:
			raise ClassAttributeError(f"Case.__init__ -> L'état de la case a l'init est incorrect: {state}")
		else:
			self.state = state

	def __str__(self):
		return self.state

	def libre(self):
		return self.state == 1

	def depart(self):
		self.state = 1

	def arrivee(self, player):
		self.player_on = player
		if self.player_on == self._game_other_.PLAYER1_class_id:
			self.state = 2
		elif self.player_on == semf._game_other_.PLAYER2_class_id:
			self.state = 3
		else:
			raise WoullaCestPasNet("Ni le J1 ni le J2 arrive sur la case.")



class Game():

	def __init__(self):
		pass


	def FLIP(self):
		

		self.canvas_display_calque1.delete(PLAYER1.id_png)
		PLAYER1.id_png = self.canvas_display_calque1.create_image(PLAYER1.x, PLAYER1.y, image=PLAYER1.png, anchor="nw")
		
		self.canvas_display_calque1.delete(PLAYER2.id_png)
		PLAYER2.id_png = self.canvas_display_calque1.create_image(PLAYER2.x, PLAYER2.y, image=PLAYER2.png, anchor="nw")



	def create(self, size):
		self.data = generate_board(size)
		self.matrice = self.data[5]
		self.board = []

		for ligne in self.matrice:
			board_line = []

			for char in ligne:

				board_line.append(Case(char, self))

			self.board.append(board_line)

		print(self.board)

		self.SETUP_CREATE()


	def SETUP_CREATE(self):


		self.gameframe = tkinter.Toplevel()
		self.gameframe.title("Wallz - Game running")
		self.gameframe.geometry("527x527")
		#fenêtre réduite, a utiliser pour le vrai jeu (affichage test ci dessous)
		#self.gameframe.geometry("1457x1457")
		
		self.gameframe.resizable(0, 0)

		self.bgimage = tkinter.PhotoImage(file = "board.png")
		self.player1png = tkinter.PhotoImage(file = r"./assets/player1.png")
		self.player2png = tkinter.PhotoImage(file = r"./assets/player2.png")

		#prépa de la surface du jeu calque 1 (canvas_display_calque1)

		self.canvas_display_calque1 = tkinter.Canvas(self.gameframe, width=1457, height=1457)
		self.canvas_display_calque1.pack(fill="both", expand=False)
		self.canvas_display_calque1.configure(bg="black")

		self.boarddisplay = self.canvas_display_calque1.create_image(0, 0, image=self.bgimage, anchor="nw")


		self.PLAYER1 = Player(self, self.data[1], self.data[2], self.player1png)
		self.PLAYER2 = Player(self, self.data[3], self.data[4], self.player2png)

		self.PLAYER1_class_id = self.PLAYER1
		self.PLAYER2_class_id = self.PLAYER2

		print(self.PLAYER1_class_id, self.PLAYER2_class_id)

		self.PLAYER1.spawn(self)
		self.PLAYER2.spawn(self)

		self.RUN()

		self.gameframe.mainloop()


	def RUN(self):




		TURN = self.PLAYER1_class_id

		self.TURN = self.PLAYER1_class_id

		self.gameframe.bind('<Up>', 
			lambda event, content = self:
				Player.move_up("bind", content))

		self.gameframe.bind('<Down>', 
			lambda event, content = self:
				Player.move_down("bind", content))

		self.gameframe.bind('<Left>',
			lambda event, content = self:
				Player.move_left("bind", content))
		
		self.gameframe.bind('<Right>',
			lambda event, content = self:
				Player.move_right("bind", content))