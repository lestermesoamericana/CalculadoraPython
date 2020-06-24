# Creacion de una calculadora en Python
from tkinter import *
import funciones_calc
import operaciones_calc

# creacion de raiz para el frame principal
raiz = Tk()
raiz.title("Calculadora")

miFrame = Frame(raiz, width = 220, height = 220)
miFrame.pack()

# ----------------------- PANTALLA-------------------------------------------
# Variable para aceptar numero en pantalla
numerosPantalla = StringVar()

pantalla = Entry(miFrame,textvariable = numerosPantalla)
# las funciones "columnspan o rowspan" sirven en el caso usemos grid en lugar
# de place para decir cuantas columnas o filas ocuparemos sin descuadrar 
'''pantalla.grid(row = 1, column=1, padx = 10, pady = 10,columnspan = 4)'''
pantalla.grid(row = 1, column=1, padx = 10, pady = 10)
pantalla.config(background = "black", fg = "white", justify = "right")
pantalla.place(x=10, y=10, height=30, width=200)
# el objeto que llamara a mi clase con los numeros en cada instancia
# y el objeto que realizara las operaciones 
objeto = funciones_calc.PresionarCalculadora()
numerosPantalla.set("0.")
objetoOperaciones = operaciones_calc.OperacionesNumericas()

#------------------------ Fila1 ---------------------------------------------
botonBorrar = Button(miFrame, text = "CE", width = 3, 
    command = lambda:funciones_calc.PresionarCalculadora.pushbuttonL(objeto,numerosPantalla))
# por si queremos usar grid
# boton7.grid(row = 5, column = 1)
botonBorrar.place(x=10, y=45, height=30, width=50) 
botonPot    = Button(miFrame, text = "C", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbuttonB(objeto,numerosPantalla))
botonPot.place(x=65, y=45, height=30, width=50) 
botonRaiz   = Button(miFrame, text = "<-", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbuttonR(objeto,numerosPantalla))
botonRaiz.place(x=120, y=45, height=30, width=50)

# division
botonDiv    = Button(miFrame, text = "➗", width = 3)
botonDiv.place(x=175, y=45, height=30, width=35)

#------------------------ Fila2 ---------------------------------------------
boton7      = Button(miFrame, text = "7", width = 3, 
    command = lambda:funciones_calc.PresionarCalculadora.pushbutton7(objeto,numerosPantalla))
boton7.place(x=10, y=80, height=30, width=50) 
boton8      = Button(miFrame, text = "8", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbutton8(objeto,numerosPantalla))
boton8.place(x=65, y=80, height=30, width=50) 
boton9      = Button(miFrame, text = "9", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbutton9(objeto,numerosPantalla))
boton9.place(x=120, y=80, height=30, width=50)

# Multiplicacion
botonProd   = Button(miFrame, text = "*", width = 3)
botonProd.place(x=175, y=80, height=30, width=35)

#------------------------ Fila3 ---------------------------------------------
boton4      = Button(miFrame, text = "4", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbutton4(objeto,numerosPantalla))
boton4.place(x=10, y=115, height=30, width=50) 
boton5      = Button(miFrame, text = "5", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbutton5(objeto,numerosPantalla))
boton5.place(x=65, y=115, height=30, width=50) 
boton6      = Button(miFrame, text = "6", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbutton6(objeto,numerosPantalla))
boton6.place(x=120, y=115, height=30, width=50)

# Resta
botonresta  = Button(miFrame, text = "-", width = 3)
botonresta.place(x=175, y=115, height=30, width=35)

#------------------------ Fila4 ---------------------------------------------
boton1      = Button(miFrame, text = "1", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbutton1(objeto,numerosPantalla))
boton1.place(x=10, y=150, height=30, width=50) 
boton2      = Button(miFrame, text = "2", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbutton2(objeto,numerosPantalla))
boton2.place(x=65, y=150, height=30, width=50) 
boton3      = Button(miFrame, text = "3", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbutton3(objeto,numerosPantalla))
boton3.place(x=120, y=150, height=30, width=50)

# suma
botonsuma   = Button(miFrame, text = "+", width = 3,
    command = lambda:operaciones_calc.OperacionesNumericas.funcion_suma(objetoOperaciones,numerosPantalla))
botonsuma.place(x=175, y=150, height=30, width=35)

#------------------------ Fila5 ---------------------------------------------
boton1      = Button(miFrame, text = "0", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbutton0(objeto,numerosPantalla))
boton1.place(x=10, y=185, height=30, width=50) 
boton2      = Button(miFrame, text = ".", width = 3,
    command = lambda:funciones_calc.PresionarCalculadora.pushbuttonP(objeto,numerosPantalla))
boton2.place(x=65, y=185, height=30, width=50) 
boton3      = Button(miFrame, text = "%", width = 3)
boton3.place(x=120, y=185, height=30, width=50)

# boton igual
botonigual  = Button(miFrame, text = "=", width = 3,
    command = lambda:operaciones_calc.OperacionesNumericas.igual(objetoOperaciones,numerosPantalla))
botonigual.place(x=175, y=185, height=30, width=35)

# Final del codigo
raiz.mainloop()