# aqui se pondran las funciones del teclado y se enviaran
# a la pantalla que tenemos en el disenyo
from tkinter import *
from operaciones_calc import *

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
        self.contador = 0

    # -------------------- numeros 1, 2 y 3 ---------------------------------------
    # Numero 1
    def pushbutton1(self, presionarboton):
        objetoOp = OperacionesNumericas()

        if presionarboton.get() == "0." and self.contador == 1:
            presionarboton.set(presionarboton.get() + self.__boton1)
        elif presionarboton.get() == "0." and self.contador == 0:
            presionarboton.set(self.__boton1)
        else:
            presionarboton.set(presionarboton.get() + self.__boton1)

    
    # Numero 2
    def pushbutton2(self, presionarboton):
        if presionarboton.get() == "0." and self.contador == 1:
            presionarboton.set(presionarboton.get() + self.__boton2)
        elif presionarboton.get() == "0." and self.contador == 0:
            presionarboton.set(self.__boton2)
        else:
            presionarboton.set(presionarboton.get() + self.__boton2)
  
    # Numero 3
    def pushbutton3(self, presionarboton):
        if presionarboton.get() == "0." and self.contador == 1:
            presionarboton.set(presionarboton.get() + self.__boton3)
        elif presionarboton.get() == "0." and self.contador == 0:
            presionarboton.set(self.__boton3)
        else:
            presionarboton.set(presionarboton.get() + self.__boton3)

    # -------------------- numeros 4, 5 y 6 ---------------------------------------
    # Numero 4
    def pushbutton4(self, presionarboton):
        if presionarboton.get() == "0." and self.contador == 1:
            presionarboton.set(presionarboton.get() + self.__boton4)
        elif presionarboton.get() == "0." and self.contador == 0:
            presionarboton.set(self.__boton4)
        else:
            presionarboton.set(presionarboton.get() + self.__boton4) 
    
    # Numero 5
    def pushbutton5(self, presionarboton):
        if presionarboton.get() == "0." and self.contador == 1:
            presionarboton.set(presionarboton.get() + self.__boton5)
        elif presionarboton.get() == "0." and self.contador == 0:
            presionarboton.set(self.__boton5)
        else:
            presionarboton.set(presionarboton.get() + self.__boton5) 
    
    # Numero 6
    def pushbutton6(self, presionarboton):
        if presionarboton.get() == "0." and self.contador == 1:
            presionarboton.set(presionarboton.get() + self.__boton6)
        elif presionarboton.get() == "0." and self.contador == 0:
            presionarboton.set(self.__boton6)
        else:
            presionarboton.set(presionarboton.get() + self.__boton6)

    # -------------------- numeros 7, 8 y 9 ---------------------------------------
    # Numero 7
    def pushbutton7(self, presionarboton):
        if presionarboton.get() == "0." and self.contador == 1:
            presionarboton.set(presionarboton.get() + self.__boton7)
        elif presionarboton.get() == "0." and self.contador == 0:
            presionarboton.set(self.__boton7)
        else:
            presionarboton.set(presionarboton.get() + self.__boton7)
    
    # Numero 8
    def pushbutton8(self, presionarboton):
        if presionarboton.get() == "0." and self.contador == 1:
            presionarboton.set(presionarboton.get() + self.__boton8)
        elif presionarboton.get() == "0." and self.contador == 0:
            presionarboton.set(self.__boton8)
        else:
            presionarboton.set(presionarboton.get() + self.__boton8)
    
    # Numero 0
    def pushbutton9(self, presionarboton):
        if presionarboton.get() == "0." and self.contador == 1:
            presionarboton.set(presionarboton.get() + self.__boton9)
        elif presionarboton.get() == "0." and self.contador == 0:
            presionarboton.set(self.__boton9)
        else:
            presionarboton.set(presionarboton.get() + self.__boton9)
    
    # ------------------------- numeros 0 y Punto --------------------------------
    # numero 0
    def pushbutton0(self, presionarboton):
        if presionarboton.get() == "0." and self.contador == 0:
            pass
        elif presionarboton.get() == "0." and self.contador == 1:
            presionarboton.set(presionarboton.get() + self.__boton0)
        else:
            presionarboton.set(presionarboton.get() + self.__boton0)
    
    def pushbuttonP(self, presionarboton):
        # Primero comprueba si esta vacio el campo
        if presionarboton.get() == "0." and self.contador == 0:
            self.contador = 1
        elif presionarboton.get() == "0." and self.contador == 1:
            pass
        elif presionarboton.get() != "0." and self.contador == 1:
            pass
        elif presionarboton.get() != "0." and self.contador == 0:
            presionarboton.set(presionarboton.get() + self.__botonP)
            self.contador = 1

    #------------------------------ botones borrar -----------------------------
    # Borrar pantalla y memoria
    def pushbuttonB(self, presionarboton):
        objOp = OperacionesNumericas()
        valor = True

        objOp.funcion_limpiar(valor,presionarboton)
        presionarboton.set("0.")
    
    # Borrar pantalla
    def pushbuttonL(self, presionarboton):
        presionarboton.set("0.")
    
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
    

