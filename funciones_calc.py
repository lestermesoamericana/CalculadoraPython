# aqui se pondran las funciones del teclado y se enviaran
# a la pantalla que tenemos en el disenyo
from tkinter import *

class PresionarCalculadora():

    def __init__(self, dato):
        self.dato = dato

    def pushbutton7(self, presionarboton):
        presionarboton.set(presionarboton.get() + self.dato)


