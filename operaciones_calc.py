# aqui pondremos nuestras distintas operaciones numericas

from tkinter import *

class OperacionesNumericas():
    
    def __init__(self):
        self.resultado  = 0.0
        self.operador   = ""
        # propiedades
        self.contador   = 0
        self.valorsuma  = False
        self.valorresta = False
        self.valorprod  = False
        self.valordivi  = False
        return

    # ---------------------------------- Suma ----------------------------------
    def funcion_suma(self, pantalla):
        if pantalla.get() == "0." and self.operador == "":
            pass
        elif len(pantalla.get()) == 0:
            pass
        elif self.operador == "":
            self.resultado = float(pantalla.get())
            pantalla.set("")
            self.operador   = "+"
            self.valorsuma  = True
            self.valorresta = False
            self.valorprod  = False
            self.valordivi  = False
        elif self.operador != "":
            self.resultado += float(pantalla.get())
            pantalla.set("")
            self.operador   = "+"
            self.valorsuma  = True
            self.valorresta = False
            self.valorprod  = False
            self.valordivi  = False
        return
    
    # --------------------------------- Resta ----------------------------------
    
    def funcion_resta(self, pantalla):
        if pantalla.get() == "0.":
            pass
        elif len(pantalla.get()) == 0:
            pass
        else:
            if self.contador == 0:
                self.resultado = float(pantalla.get())
                pantalla.set("")
                self.contador = 1
            else:
                self.resultado -= float(pantalla.get())
                pantalla.set("")
            self.operador   = "-"
            self.valorsuma  = False
            self.valorresta = True
            self.valorprod  = False
            self.valordivi  = False
            return
    
    # -------------------------------- Producto --------------------------------
    def funcion_prod(self, pantalla):
        if pantalla.get() == "0.":
            pass
        elif len(pantalla.get()) == 0:
            pass
        else:
            if self.contador == 0:
                self.resultado = float(pantalla.get())
                pantalla.set("")
                self.contador = 1
            else:
                self.resultado *= float(pantalla.get())
                pantalla.set("")
            self.valorsuma  = False
            self.valorresta = False
            self.valorprod  = True
            self.valordivi  = False
        return

    # -------------------------------- Division --------------------------------

    def funcion_division(self, pantalla):
        if pantalla.get() == "0.":
            pass
        elif len(pantalla.get()) == 0:
            pass
        elif pantalla.get() == "0" and self.contador == 1:
            pantalla.set("Error")
        else:
            self.resultado = float(pantalla.get())
            pantalla.set("")
            self.valorsuma  = False
            self.valorresta = False
            self.valorprod  = False
            self.valordivi  = True
        return
           
    
    # --------------------------------- Igual ---------------------------------
    def igual(self, pantalla):
        
        __variableDiv = 0.0
        __VariableTemp = 0.0

        if len(pantalla.get()) == 0:
            pass
        
        if self.valorsuma:
            self.resultado += float(pantalla.get())
            pantalla.set(self.resultado)
            self.contador   = 0
            self.resultado  = 0.0
            self.valorsuma  = False
            self.operador   = "" 
        
        if self.valorresta:
            self.resultado -= float(pantalla.get())
            pantalla.set(self.resultado)
            self.contador = True
            self.resultado = 0.0
            self.valorsuma = False

        if self.valorprod:
            self.resultado *= float(pantalla.get())
            pantalla.set(self.resultado)
            self.contador = True
            self.resultado = 0.0
            self.valorprod = False
        
        if self.valordivi:
            if pantalla.get() == "0":
                pantalla.set("Error")
            else:
                __variableDiv = float(pantalla.get())
                __VariableTemp = self.resultado
                pantalla.set(str(__VariableTemp/__variableDiv))
                self.contador = 0
                self.valordivi = False
        return
    
    # -------------------------------- Borrar --------------------------------
    def funcion_limpiar(self, valor, pantalla):
        if valor:
            self.resultado = 0.0
        return
    # metodo
    def funcion_reestablecer(self):
        self.operador = ""
        return
    
    # ------------------------------- devolver -------------------------------
    def getOperador(self):
        return self.operador

    