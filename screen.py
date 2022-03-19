import turtle


class Screen:

    def __init__(self):
        self.__screen = turtle.Screen()
        self.__screen.setup(400, 400)
        self.__screen.addshape("rovers/rover-bas.gif")
        self.__screen.addshape("rovers/rover-bas-droite.gif")
        self.__screen.addshape("rovers/rover-bas-gauche.gif")
        self.__screen.addshape("rovers/rover-droite.gif")
        self.__screen.addshape("rovers/rover-gauche.gif")
        self.__screen.addshape("rovers/rover-haut.gif")
        self.__screen.addshape("rovers/rover-haut-droite.gif")
        self.__screen.addshape("rovers/rover-haut-gauche.gif")

    def choix_carte(self, nom_carte):
        self.__screen.bgpic("maps/" + nom_carte)

    def mainloop(self):
        return self.__screen.mainloop()
