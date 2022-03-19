import turtle


class Rover:

    def __init__(self):
        self.__rover = turtle.Turtle()
        self.__rover.shape("rovers/rover-droite.gif")
        self.__rover.pencolor("red")
        self.__rover.pensize(4)
        self.__rover.speed(1)

        # Initialisation de la position du rover
        self.__rover.hideturtle()
        self.__rover.penup()
        self.__rover.goto(-165, -165)
        self.__rover.showturtle()
        self.__rover.pendown()

    def changer_position(self, horizontal, vertical):
        self.__rover.goto(horizontal, vertical)

    def avancer(self, distance):
        self.__rover.forward(distance)

    def tourner_a_droite(self, degree):
        self.__rover.right(degree)

    def tourner_a_gauche(self, degree):
        self.__rover.left(degree)

    def reculer(self, distance):
        self.__rover.backward(distance)

    def vitesse(self, vitesse):
        self.__rover.speed(vitesse)

    def changer_image(self, nom_image):
        self.__rover.shape("rovers/" + nom_image)
