from tkinter import*
class Fenetretk(Tk):

  def __init__(self):
    Tk.__init__(self)

    self.geometry("300x200")
    self.title("Projet Fractales Killian & Goharik")
    self.__profondeur = IntVar()
    self.__epaisseur = IntVar()
    
    lab = Label(self, text="Super fractales de la mort qui tue")
    lab.pack(side="top")

    cadre = Frame(self, width=150, height=200)
    cadre.pack(side="top")

    labprof = Label(cadre, text="Valeur de la profondeur")
    labprof.pack()

    profondeur = Entry(cadre, textvariable=self.__profondeur)
    profondeur.focus_set()
    profondeur.pack()

    labep = Label(cadre, text="Valeur de l'épaisseur")
    labep.pack()

    epaisseur = Entry(cadre, textvariable=self.__epaisseur)
    epaisseur.focus_set()
    epaisseur.pack()

    bouton = Button(self, text="Valider les valeurs", command=self.qqch)
    bouton.pack()
    
  def qqch(self):
    print(f"L'utilisateur a choisi {self.__profondeur.get()} et {self.__epaisseur.get()}")
    
fenetre = Fenetretk()
fenetre.mainloop()