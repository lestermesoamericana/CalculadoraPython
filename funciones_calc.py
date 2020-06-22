# aqui se pondran las funciones del teclado y se enviaran
# a la pantalla que tenemos en el disenyo
from tkinter import *

class PresionarCalculadora():

    def __init__(self):
        self.__boton1 = "1"
        self.__boton2 = "2"
        self.__boton3 = "3"
        self.__boton4 = "4"
        self.__boton5 = "5"
        self.__boton6 = "6"
        self.__boton7 = "7"
        self.__boton8 = "8"
        self.__boton9 = "9"
        self.__boton0 = "0"

    # -------------------- numeros 1, 2 y 3 ---------------------------------------
    def pushbutton1(self, presionarboton):
        presionarboton.set(presionarboton.get() + self.__boton1)
    
    def pushbutton2(self, presionarboton):
        presionarboton.set(presionarboton.get() + self.__boton2)
    
    def pushbutton3(self, presionarboton):
        presionarboton.set(presionarboton.get() + self.__boton3)

    # -------------------- numeros 4, 5 y 6 ---------------------------------------
    def pushbutton4(self, presionarboton):
        presionarboton.set(presionarboton.get() + self.__boton4)
    
    def pushbutton5(self, presionarboton):
        presionarboton.set(presionarboton.get() + self.__boton5)
    
    def pushbutton6(self, presionarboton):
        presionarboton.set(presionarboton.get() + self.__boton6)

    # -------------------- numeros 7, 8 y 9 ---------------------------------------
    def pushbutton7(self, presionarboton):
        presionarboton.set(presionarboton.get() + self.__boton7)
    
    def pushbutton8(self, presionarboton):
        presionarboton.set(presionarboton.get() + self.__boton8)
    
    def pushbutton9(self, presionarboton):
        presionarboton.set(presionarboton.get() + self.__boton9)
    
    # ------------------------- numeros 0 ----------------------------------------
    def pushbutton0(self, presionarboton):
        presionarboton.set(presionarboton.get() + self.__boton0)


