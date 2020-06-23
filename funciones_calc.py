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
        self.__botonP = "."

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
    
    # ------------------------- numeros 0 y Punto --------------------------------
    def pushbutton0(self, presionarboton):
        # Primero comprueba si esta vacio el campo
        if len(presionarboton.get()) == 0:
            pass
        else:
            presionarboton.set(presionarboton.get() + self.__boton0)
    
    def pushbuttonP(self, presionarboton):
        # Primero comprueba si esta vacio el campo
        if len(presionarboton.get()) == 0:
            presionarboton.set(presionarboton.get() + "0" + self.__botonP)
        else:
            contador = 0
            texto = str()
            texto = presionarboton.get()
            for i in texto:
                if texto[i] == "." and contador == 1:
                    pass
                else:
                    presionarboton.set(presionarboton.get() + self.__botonP)
                    contador = 1
    
    #------------------------------ botones borrar -----------------------------
    def pushbuttonB(self, presionarboton):
        presionarboton.set("")
    
    # borrar caracter por caracter
    def pushbuttonR(self, presionarboton):
        if len(presionarboton.get()) == 0:
            pass
        else:
            texto1 = str()
            texto1 = presionarboton.get()
            
            texto2 = []
            texto2 = list(texto1)
            texto2.pop()

            textoS = "".join(texto2)
            
            presionarboton.set(textoS)

