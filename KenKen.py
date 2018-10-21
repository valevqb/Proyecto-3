"""
__________________________________________________________________
Autora: Tania María Sánchez Irola y Valeria Quesada Benavides
Carné: 2018138723 y 2018085308
Curso: Taller de programación
Profesor: William Mata Rodriguez
Grupo: 2
___________________________________________________________________
"""

from tkinter import *

from tkinter import messagebox

import tkinter

import sys

import random

import threading

import time

import os

import ast

global crono
crono=1

global sexo
sexo=0

global nivel
nivel = "F"

global sonido
sonido = True

global cuadro
cuadro = 3

"""__________________________________________________________________________________________________________________________________________________________________"""
"""__________________________________________________________________________________________________________________________________________________________________"""

"""CREACIÓN DE ETIQUETAS, TEXTOS Y BOTONES"""
def crearEtiqueta(self, nombre, texto, posX, posY):
    """ Creamos una etiqueta con los valores recibidos"""
    etiqueta = Label(self, name=nombre, text= texto, fg =  "#4285f4", font = ("Serif", 14))
    etiqueta.place(x=posX, y=posY)
    return etiqueta

def crearTexto(self, nombre, posX, posY, ancho):
    """ Creamos un cuadro de texto con los valores recibidos"""
    texto = Entry(self, name=nombre, width=ancho, font = ("Serif", 13))
    texto.place(x=posX, y=posY)
    return texto

def crearBoton(self, nombre, texto, posX, posY, ancho, comando):
    """ Creamos un boton con los valores recibidos"""
    boton = Button(self, name=nombre, text=texto, width=ancho, activebackground="gray85",command= comando, fg = "white", bg = "gray85", font = ("Serif", 13))
    boton.place(x=posX, y=posY)
    return boton

cronometro=0

"""__________________________________________________________________________________________________________________________________________________________________"""

"""__________________________________________________________________________________________________________________________________________________________________"""

class menu_principal (tkinter.Tk):
    def __init__(menu):
        #_____________________VENTANA___________________________#
        
        """Esta es la primer ventana"""
        tkinter.Tk.__init__(menu);

        """Titulo"""
        menu.title("Menú principal");

        """Tamaño"""
        menu.geometry("330x60");

        """Indica que la ventana no se puede ampliar"""
        menu.resizable(width=False, height=False)

        #Barra del menú

        """Agregar etiquetas"""
        menubar = Menu(menu)
        menubar.add_command(label="Acerca De",            command=menu.acercaDe)
        menubar.add_command(label="Ayuda",                   command=menu.ayuda)
        menubar.add_command(label="Salir",                 command=menu.destroy)

        #Desplegar el menú
        menu.config(menu = menubar)

        #______________________BOTONES__________________________#
        menu.jugar = crearBoton(menu, "jugar", "Jugar", 10, 10, 15, lambda: menu.juego());
        menu.jugar.configure         (bg = "mediumpurple")
        menu.configurar = crearBoton(menu, "configurar", "Configurar", 170, 10, 15, lambda: menu.configura());
        menu.configurar.configure    (bg = "cornflowerblue")
        
        documentos = ["kenken_juegos.txt","kenken_juegos2.txt","kenken_juegos3.txt", "kenken_juegos4.txt","kenken_juegos5.txt"]   
        #print(random.choice(documentos))
        global horasOrig
        global minutosOrig
        global segundosOrig
        segundosOrig = 0
        minutosOrig = 0
        horasOrig = 0        
        global diccionarios
        global documento
        diccionarios = open(str(random.choice(documentos)), "r")
        documento    = diccionarios.read()
        #print(documento)
    def juego (menu):
        """Destruir esta ventana"""
        menu.destroy()

        """Crear la nueva ventana"""
        name().mainloop()

    def configura (menu):
        """Destruir esta ventana"""
        menu.destroy()

        """Crear la nueva ventana"""
        configuracion().mainloop()

    def acercaDe(menu):
        messagebox.showinfo("Acerca De", "Autores: Tania María Sánchez Irola\n                Valeria Quesada Benavides \nFecha: 15 de octubre del 2018 \nVersión: 9.2 \nPrograma: Kenken")

    """DESPLEGA LA AYUDA"""
    def ayuda(menu):
        os.startfile("Manual.pdf")
        #open("MANUAL DE USUARIO2.pdf")
       

class configuracion (tkinter.Tk):
    def __init__(menu):
        #_____________________VENTANA___________________________#

        """Esta es la primer ventana"""
        tkinter.Tk.__init__(menu);

        """Titulo"""
        menu.title("Elije la configuracion de tu juego");

        """Tamaño"""
        menu.geometry("450x570");

        """Indica que la ventana no se puede ampliar"""
        menu.resizable(width=False, height=False)

        #_______________________BOTONES____________________________# se cambiaron
        """Botones de nivel"""
        menu.values = tkinter.IntVar(menu)
        menu.values.set(3)
        menu.nivel1 = tkinter.Radiobutton(menu, text="Fácil",   variable=menu.values, value=3, command=menu.level1)
        menu.nivel2 = tkinter.Radiobutton(menu, text="Regular", variable=menu.values, value=2, command=menu.level2)
        menu.nivel3 = tkinter.Radiobutton(menu, text="Difícil", variable=menu.values, value=1, command=menu.level3)
        menu.nivel1.place(x=20,y=25)
        menu.nivel2.place(x=20,y=45)
        menu.nivel3.place(x=20,y=65)

        """Botones de reloj"""
        menu.valor = tkinter.IntVar(menu)
        menu.valor.set(3)

        menu.si    = tkinter.Radiobutton(menu, text="Sí",    variable=menu.valor, value=3, command=menu.tiemposi)
        menu.no    = tkinter.Radiobutton(menu, text="No",    variable=menu.valor, value=2, command=menu.tiempono)
        menu.timer = tkinter.Radiobutton(menu, text="Timer", variable=menu.valor, value=1, command=menu.timer)
        menu.si.place   (x=20,y=125)
        menu.no.place   (x=20,y=145)
        menu.timer.place(x=20,y=165)

        """Botones sonido"""
        menu.valores = tkinter.IntVar()
        menu.valores.set(2)

        menu.sonido1 = tkinter.Radiobutton(menu, text="Sí", variable=menu.valores, value=2, command=menu.sonidosi)
        menu.sonido2 = tkinter.Radiobutton(menu, text="No", variable=menu.valores, value=1, command=menu.sonidono)
        menu.sonido1.place(x=20,y=225)
        menu.sonido2.place(x=20,y=245)

        """Botones sexo"""
        menu.value = tkinter.IntVar(menu)
        menu.value.set(3)

        menu.mujer  = tkinter.Radiobutton(menu, text="Femenino",  variable=menu.value, value=2, command=menu.mujer)
        menu.hombre = tkinter.Radiobutton(menu, text="Masculino", variable=menu.value, value=1, command=menu.hombre)
        menu.otro   = tkinter.Radiobutton(menu, text="Otro",      variable=menu.value, value=3, command=menu.otro)
        menu.mujer.place (x=20,y=307)
        menu.hombre.place(x=20,y=327)
        menu.otro.place  (x=20,y=347)

        """Botones juego cuadricula"""
        menu.cuadricula = tkinter.IntVar(menu)
        menu.cuadricula.set(8)

        menu.cuadricula_3  = tkinter.Radiobutton(menu, text="3 x 3",  variable=menu.cuadricula, value=8, command=menu.cuadricula_3)
        menu.cuadricula_4  = tkinter.Radiobutton(menu, text="4 x 4",  variable=menu.cuadricula, value=2, command=menu.cuadricula_4)
        menu.cuadricula_5 = tkinter.Radiobutton(menu, text="5 x 5", variable=menu.cuadricula, value=3, command=menu.cuadricula_5)
        menu.cuadricula_6   = tkinter.Radiobutton(menu, text="6 x 6",      variable=menu.cuadricula, value=4, command=menu.cuadricula_6)
        menu.cuadricula_7  = tkinter.Radiobutton(menu, text="7 x 7",  variable=menu.cuadricula, value=5, command=menu.cuadricula_7)
        menu.cuadricula_8 = tkinter.Radiobutton(menu, text="8 x 8", variable=menu.cuadricula, value=6, command=menu.cuadricula_8)
        menu.cuadricula_9   = tkinter.Radiobutton(menu, text="9 x 9",      variable=menu.cuadricula, value=7, command=menu.cuadricula_9)
        menu.multi   = tkinter.Radiobutton(menu, text="Multitamaño",      variable=menu.cuadricula, value=1, command=menu.multi)
        menu.cuadricula_3.place (x=20,y=407)
        menu.cuadricula_4.place(x=20,y=427)
        menu.cuadricula_5.place  (x=20,y=447)
        menu.cuadricula_6.place (x=20,y=467)
        menu.cuadricula_7.place(x=150,y=407)
        menu.cuadricula_8.place  (x=150,y=427)
        menu.cuadricula_9.place(x=150,y=447)
        menu.multi.place  (x=150,y=467)


        """Regresar"""
        menu.regreso = crearBoton(menu, "botoninicio", "Regresar al menú", 260, 515, 17, menu.regresar)
        menu.regreso.configure(bg = "lightblue")

        menu.jugar = crearBoton(menu, "jugar", "Jugar", 150, 515, 10, lambda: menu.juego());
        menu.jugar.configure         (bg = "mediumpurple")

        #____________________GLOBAL________________________________#

        global crono
        crono=1
        
        #_______________________ETIQUETAS__________________________# se cambiaron
        menu.niveles=Label(menu, text="Nivel",fg="black",                     font=("Arial",12)) #para anadir texto
        menu.niveles.place(x=20,y=5)
        menu.reloj  =Label(menu, text="Reloj",fg="black",                     font=("Arial",12)) #para anadir texto
        menu.reloj.place  (x=20,y=105)
        menu.sonido =Label(menu, text="Sonido al terminar el juego con éxito",fg="black",font=("Arial",12)) #para anadir texto
        menu.sonido.place (x=20,y=205)
        menu.sonido =Label(menu, text="Seleccione su sexo",                   fg="black",font=("Arial",12)) #para anadir texto
        menu.sonido.place (x=20,y=287)
        menu.cuadricula =Label(menu, text="Defina una posible cuadricula",                   fg="black",font=("Arial",12)) #para anadir texto
        menu.cuadricula.place (x=20,y=385)

        #_______________________FUNCIONES___________________________#

        #Barra del menú

        """Agregar etiquetas"""
        menubar = Menu(menu)
        menubar.add_command(label="Acerca De",            command=menu.acercaDe)
        menubar.add_command(label="Ayuda",                   command=menu.ayuda)
        menubar.add_command(label="Salir",                 command=menu.destroy)


        #Desplegar el menú
        menu.config(menu = menubar)

    def juego (menu):
        """Destruir esta ventana"""
        menu.destroy()

        """Crear la nueva ventana"""
        name().mainloop()

    def acercaDe(menu):
        messagebox.showinfo("Acerca De", "Autores: Tania María Sánchez Irola\n                Valeria Quesada Benavides \nFecha: 15 de octubre del 2018 \nVersión: 9.2 \nPrograma: Kenken")

    """DESPLEGA LA AYUDA"""
    def ayuda(menu):
        os.startfile("Manual.pdf")
        #open("MANUAL DE USUARIO2.pdf")

    def level1(menu):
        global nivel
        nivel = "F"

    def level2(menu):
        global nivel
        nivel = "I"
    
    def level3(menu):
        global nivel
        nivel = "D"

    def tiemposi(menu):
        global crono
        crono=1
        #print(cronometro)

    def tiempono(menu):
        global crono
        crono=0
        #print(cronometro)

    def timer(menu):
        global crono
        crono=2
        """Destruir esta ventana"""
        menu.destroy()

        #"""Crear la nueva ventana"""
        timer().mainloop()

    def sonidono(menu):
        global sonido
        sonido = False

    def sonidosi(menu):
        global sonido
        sonido = True

    def mujer(menu):
        global sexo
        sexo=1

    def hombre(menu):
        global sexo
        sexo=2

    def regresar(menu):
        """Destruir esta ventana"""
        menu.destroy()

        #"""Crear la nueva ventana"""
        menu_principal().mainloop()

    def otro(menu):
        global sexo
        sexo=0

    """Cuadriculas"""

    def cuadricula_3(menu):
        global cuadro
        cuadro = 3

    def cuadricula_4(menu):
        global cuadro
        cuadro = 4

    def cuadricula_5(menu):
        global cuadro
        cuadro = 5

    def cuadricula_6(menu):
        global cuadro
        cuadro = 6

    def cuadricula_7(menu):
        global cuadro
        cuadro = 7

    def cuadricula_8(menu):
        global cuadro
        cuadro = 8

    def cuadricula_9(menu):
        global cuadro
        cuadro = 9

    def multi(menu):
        global cuadro
        cuadro = 10

class timer (tkinter.Tk):
    def __init__(self):

        #_______________________GLOBALES_______________________________#

        global crono
        global horas
        global minutos
        global segundos
        global horasOrig
        global minutosOrig
        global segundosOrig
        segundosOrig = 0
        minutosOrig = 0
        horasOrig = 0
        crono=2
        
        #_____________________VENTANA___________________________#
        """Esta es la primer ventana"""
        tkinter.Tk.__init__(self);

        """Titulo"""
        self.title("Por favor inserta el tiempo a durar");

        """Tamaño"""
        self.geometry("312x450");

        """Indica que la ventana no se puede ampliar"""
        self.resizable(width=False, height=False)

        #____________________ETIQUETAS___________________________#

        self.textoHoras=Label(self, text="Horas",fg="black",font=("Arial",15)) #para anadir texto
        self.textoHoras.place(x=20,y=30)
        self.textoMinutos=Label(self, text="Minutos",fg="black",font=("Arial",15)) #para anadir texto
        self.textoMinutos.place(x=100,y=30)
        self.textoSegundos=Label(self, text="Segundos",fg="black",font=("Arial",15)) #para anadir texto
        self.textoSegundos.place(x=195,y=30)

        #____________________CAJAS DE TEXTO_________________________#

        self.cajaHoras = Entry(self,width=0,font=("Arial",20),name="cajah")
        self.cajaHoras.place(x=30,y=60)
        self.cajaHoras.insert(0,"00")
        self.cajaMinutos = Entry(self,width=0,font=("Arial",20),name="cajam")
        self.cajaMinutos.place(x=115, y= 60)
        self.cajaMinutos.insert(0,"00")
        self.cajaSegundos = Entry(self,width=0,font=("Arial",20),name="cajas")
        self.cajaSegundos.place(x=225, y= 60)
        self.cajaSegundos.insert(0,"00")

        #____________________MINI TECLADO_______________________________#
        
        self.buttonteclado=Button(self, text="0", activebackground="gray", fg = "white", bg = "black", font = ("Arial", 13), width=3, heigh=0, command = lambda: self.teclado("0"))
        self.buttonteclado.place(x=137,y=249)
        self.buttonteclado=Button(self, text=" ", activebackground="gray", fg = "white", bg = "black", font = ("Arial", 13), width=3, heigh=0)
        self.buttonteclado.place(x=100,y=249)
        self.buttonteclado=Button(self, text=" ", activebackground="gray", fg = "white", bg = "black", font = ("Arial", 13), width=3, heigh=0)
        self.buttonteclado.place(x=174,y=249)
        self.buttonteclado=Button(self, text="1", activebackground="gray", fg = "white", bg = "black", font = ("Arial", 13), width=3, heigh=0, command = lambda: self.teclado("1"))
        self.buttonteclado.place(x=100,y=216)
        self.buttonteclado=Button(self, text="2", activebackground="gray", fg = "white", bg = "black", font = ("Arial", 13), width=3, heigh=0, command = lambda: self.teclado("2"))
        self.buttonteclado.place(x=137,y=216)
        self.buttonteclado=Button(self, text="3", activebackground="gray", fg = "white", bg = "black", font = ("Arial", 13), width=3, heigh=0, command = lambda: self.teclado("3"))
        self.buttonteclado.place(x=174,y=216)
        self.buttonteclado=Button(self, text="4", activebackground="gray", fg = "white", bg = "black", font = ("Arial", 13), width=3, heigh=0, command = lambda: self.teclado("4"))
        self.buttonteclado.place(x=100,y=183)
        self.buttonteclado=Button(self, text="5", activebackground="gray", fg = "white", bg = "black", font = ("Arial", 13), width=3, heigh=0, command = lambda: self.teclado("5"))
        self.buttonteclado.place(x=137,y=183)
        self.buttonteclado=Button(self, text="6", activebackground="gray", fg = "white", bg = "black", font = ("Arial", 13), width=3, heigh=0, command = lambda: self.teclado("6"))
        self.buttonteclado.place(x=174,y=183)
        self.buttonteclado=Button(self, text="7", activebackground="gray", fg = "white", bg = "black", font = ("Arial", 13), width=3, heigh=0, command = lambda: self.teclado("7"))
        self.buttonteclado.place(x=100,y=150)
        self.buttonteclado=Button(self, text="8", activebackground="gray", fg = "white", bg = "black", font = ("Arial", 13), width=3, heigh=0, command = lambda: self.teclado("8"))
        self.buttonteclado.place(x=137,y=150)
        self.buttonteclado=Button(self, text="9", activebackground="gray", fg = "white", bg = "black", font = ("Arial", 13), width=3, heigh=0, command = lambda: self.teclado("9"))
        self.buttonteclado.place(x=174,y=150)


        #___________________BOTONES FUNCIONES___________________#
        
        self.buttonJuego=Button(self, text="Juego", activebackground="gray", fg = "white", bg = "purple", font = ("Arial", 13), width=10, heigh=0, command=self.jugar)
        self.buttonJuego.place(x=27,y=320)
        self.buttonConfi=Button(self, text="Regresar a configuración", activebackground="gray", fg = "white", bg = "green", font = ("Arial", 13), width=25, heigh=0, command=self.configuraciones)
        self.buttonConfi.place(x=35,y=370)
        self.buttonMenu=Button(self, text="Menú principal", activebackground="gray", fg = "white", bg = "purple", font = ("Arial", 13), width=15, heigh=0, command=self.regresar)
        self.buttonMenu.place(x=140,y=320)
        

    def teclado(self,digito):
        elije=self.focus_get() #reconoce cada cuadro
        nombre=elije.winfo_name() #reconoce el nombre del cuadro seleccionado
        elije.delete(0,1) #elimina idigitos en la posicion 0 y 1
        if nombre=="cajah" or nombre=="cajas" or nombre=="cajam":
            elije.insert(END,digito) #inserta los digitos

    def regresar(self):
        """Destruir esta ventana"""
        self.destroy()
        #"""Crear la nueva ventana"""
        menu_principal().mainloop()

    def jugar(self):
        global horasOrig
        global minutosOrig
        global segundosOrig
        horas = self.cajaHoras.get()
        minutos =self.cajaMinutos.get()
        segundos =self.cajaSegundos.get()
        horasOrig = self.cajaHoras.get()
        minutosOrig =self.cajaMinutos.get()
        segundosOrig =self.cajaSegundos.get()

        
        horasNuevas=self.cajaHoras.get()
        HORAS(horasNuevas)
        
        minsNuevas=self.cajaMinutos.get()
        MINS(minsNuevas)
        
        segsNuevas=self.cajaSegundos.get()
        SEGS(segsNuevas)

        horasverifica=horasNuevas.isdigit()
        minsverifica=minsNuevas.isdigit()
        segsverifica=segsNuevas.isdigit()

        if horasverifica==False or minsverifica==False or  segsverifica==False:
            messagebox.showerror(message="Solo se admiten números")

        if int(horasNuevas)>3 or 0>int(horasNuevas):
            messagebox.showerror(message="El rango permitido de horas es entre 0 y 3")
            
        if int(minsNuevas)>59 or int(segsNuevas)>59 or 0>int(segsNuevas) or 0>int(minsNuevas):
            messagebox.showerror(message="El rango permitido de minutos y segundos es entre 0 y 59")

        elif horasverifica==True and minsverifica==True and  segsverifica==True and int(horasNuevas)<=3 and int(segsNuevas)<60 and int(minsNuevas)<60:
            self.destroy()
            name().mainloop()
        


        

        

    def configuraciones(self):
        """Destruir esta ventana"""
        self.destroy()

        """Crear la nueva ventana"""
        configuracion().mainloop()
        

class name (tkinter.Tk):
    def __init__(menu):
        #_____________________VENTANA___________________________#
        """Esta es la primer ventana"""
        tkinter.Tk.__init__(menu);

        """Titulo"""
        menu.title("Hola! Por favor inserta tu nombre");

        """Tamaño"""
        menu.geometry("400x50");

        """Indica que la ventana no se puede ampliar"""
        menu.resizable(width=False, height=False)
        
        #______________________BOTONES__________________________#
        global nombreusuario
        nombreusuario   =  "Secret"        

        menu.textnombre     = crearTexto   (menu, "textnombre",     100,         10, 15);
        menu.textnombre.configure       (bg = "paleturquoise1")
        menu.labelnombre    = crearEtiqueta(menu, "labelnombre",    "Nombre",    10, 10)
        menu.labelnombre.configure    (fg = "black")
        menu.botonsiguiente = crearBoton   (menu, "botonsiguiente", "Siguiente", 250, 5, 10, menu.listonombre)
        menu.botonsiguiente.configure   (bg = "blue")

    def listonombre (menu):
        global nombreusuario
        if menu.textnombre.get() != "":
            nombreusuario   =  (menu.textnombre.get())
            #print (nombreusuario)

            """MUESTRA INFORMACIÓN SOBRE EL PROGRAMA"""
            menu.destroy()

            """Crear la nueva ventana"""
            juego().mainloop()            
        else:
            respuesta = tkinter.messagebox.askyesno("ERROR","¿JUGAR CON NOMBRE OCULTO?")
            
            if respuesta:
                
                nombreusuario   =  ("Secreto")
                """MUESTRA INFORMACIÓN SOBRE EL PROGRAMA"""
                menu.destroy()

                """Crear la nueva ventana"""
                juego().mainloop()                 

            else:                
                 messagebox.showinfo("ERROR", "DIGITE SU NOMBRE")

            
            




class juego(tkinter.Tk):
    def __init__(menu):

        #____________________GLOBALES__________________________#

        global horas
        global minutos
        global segundos
        global sexo
        global crono
        global ranking
        global cuadro
        ranking = False
            
        #_____________________VENTANA___________________________#

        """Esta es la primer ventana"""
        tkinter.Tk.__init__(menu);

        """Titulo"""
        menu.title("Disfruta tu juego!");

        """Indica que la ventana no se puede ampliar"""        
        menu.resizable(width=False, height=False)               


        """Tamaño"""
        menu.geometry("1150x610");

        canvas = Canvas(menu)

        Kenken=Label(menu, text="Kenken",fg="black",font=("Harlow Solid Italic",35)) #para anadir texto
        Kenken.place(x=350,y=30)

        #____________________IMAGEN________________________________#
        if sexo==1:
            menu.imagen=tkinter.PhotoImage(file="ranmamujer.png")
            menu.fondo=Label(menu,image=menu.imagen)
            menu.fondo.place(x=630,y=160)

        if sexo==2:
            menu.imagen=tkinter.PhotoImage(file="ranmahombre.png")
            menu.fondo=Label(menu,image=menu.imagen)
            menu.fondo.place(x=657,y=170)

        if sexo==0:
            menu.imagen=tkinter.PhotoImage(file="otro.png")
            menu.fondo=Label(menu,image=menu.imagen)
            menu.fondo.place(x=640,y=130)


        #_____________________BOTTON BORRADOR______________________#

        menu.borrador=tkinter.PhotoImage(file="borra.png")
        menu.borra=Button(menu,image=menu.borrador, command = menu.nada)
        menu.borra.place(x=100,y=285)
        


        #____________________CRONOMETRO___________________________#


        #Barra del menú
        """Agregar etiquetas"""
        menubar = Menu(menu)
        menubar.add_command(label="Acerca De",            command=menu.acercaDe)
        menubar.add_command(label="Ayuda",                   command=menu.ayuda)
        menubar.add_command(label="Salir",                 command=menu.destroy)

        #Desplegar el menú
        menu.config(menu = menubar)
        
        ################################################################################################



        #_______________________CUADROS TIMER_______________________#

        if crono==2:
            menu.textboxhrs = Entry(menu,width=0,font=("Arial",15),name="textboxhrs")
            menu.textboxhrs.place(x=698, y= 50)
            menu.textboxhrs.insert(0,str(horas))
            menu.textboxmins = Entry(menu,width=0,font=("Arial",15),name="textboxmins")
            menu.textboxmins.place(x=770, y= 50)
            menu.textboxmins.insert(0,str(minutos))
            menu.textboxsegs = Entry(menu,width=0,font=("Arial",15),name="textboxsegs")
            menu.textboxsegs.place(x=845, y= 50)
            menu.textboxsegs.insert(0,str(segundos))
           


        #____________________CAJA CRONO_________________________#

        if crono==1:

            menu.textboxhrs = Entry(menu,width=0,font=("Arial",15),name="textboxhrs")
            menu.textboxhrs.place(x=698, y= 50)
            menu.textboxhrs.insert(0,"00")
            menu.textboxmins = Entry(menu,width=0,font=("Arial",15),name="textboxmins")
            menu.textboxmins.place(x=770, y= 50)
            menu.textboxmins.insert(0,"00")
            menu.textboxsegs = Entry(menu,width=0,font=("Arial",15),name="textboxsegs")
            menu.textboxsegs.place(x=845, y= 50)
            menu.textboxsegs.insert(0,"00")

        if crono==1 or crono==2:

            menu.labelhrs=Label(menu, text="Horas",fg="black",font=("Arial",13)) #para anadir texto
            menu.labelhrs.place(x=685,y=25)
            
            menu.labelmins=Label(menu, text="Minutos",fg="black",font=("Arial",13)) #para anadir texto
            menu.labelmins.place(x=750,y=25)
            
            menu.labelsegs=Label(menu, text="Segundos",fg="black",font=("Arial",13)) #para anadir texto
            menu.labelsegs.place(x=817,y=25)

            menu.botoncronome = crearBoton(menu, "botoncrono", "Parar",   745, 100, 10, menu.nada)
            menu.botoncronome.configure(bg = "yellow3")
            menu.botoncronome.configure(fg = "yellow3")              

        else:
            pass


        #______________________BOTONES__________________________#

        menu.botoniniciar        = crearBoton(menu, "botoniniciar",  "Iniciar Juego",          15, 500, 12, menu.iniciar)
        menu.botoniniciar.configure       (bg = "red")

        menu.botonvalidacion = crearBoton(menu, "botonvalidacion", "Validar Juego",   145, 500, 12, menu.nada)
        menu.botonvalidacion.configure(bg = "yellow3")
        menu.botonvalidacion.configure(fg = "yellow3")        

        menu.botonotrojuego  = crearBoton(menu, "botonotrojuego",  "Otro Juego",      275, 500, 10, menu.nada)
        menu.botonotrojuego.configure (bg = "turquoise4")
        menu.botonotrojuego.configure (fg = "turquoise4")

        menu.botonreinicio   = crearBoton(menu, "botonreinicio",   "Reiniciar Juego", 385, 500, 14, menu.nada)
        menu.botonreinicio.configure  (bg = "gray64")
        menu.botonreinicio.configure  (fg = "gray64")

        menu.botontermina    = crearBoton(menu, "botontermina",    "Terminar Juego",  533, 500, 14, menu.nada)
        menu.botontermina.configure   (bg = "gray1")
        menu.botontermina.configure   (fg = "gray1")

        menu.botontop        = crearBoton(menu, "botontop",        "Top 10",          680, 500, 8, menu.top)
        menu.botontop.configure       (bg = "aquamarine4")

        menu.regreso         = crearBoton(menu, "botoninicio", "Regresar al menú", 595, 550, 17, menu.regresar)
        menu.regreso.configure        (bg = "lightblue")

        menu.guardar         = crearBoton(menu, "botonguardar", "Guardar juego", 773, 500, 13, menu.guardar)
        menu.guardar.configure        (bg = "red")

        menu.cargar         = crearBoton(menu, "botoncargar", "Cargar juego", 770, 550, 13, menu.cargar)
        menu.cargar.configure        (bg = "turquoise4")

        menu.deshacer        = crearBoton(menu, "botondeshacer", "Deshacer jugada", 250, 450, 14, menu.deshacer)
        menu.deshacer.configure        (bg = "gray64")

        menu.rehacer        = crearBoton(menu, "botonrehacer", "Rehacer jugada", 400, 450, 14, menu.rehacer)
        menu.rehacer.configure        (bg = "lightblue")


        #_______________________VALORES______________________________________________#

        """Valores por defecto"""
        global matriz
        contador = 0
        equis    = 270
        igriega  = 100
        matriz   = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        """Se crean las cajas de texto donde el ususario va a introducir las respuestas"""
        
        for i in range(6):
            equis       = 270 + 45 * i
            
            for j in range(6):
                igriega = 100 + 45 * j
                """Le  asigna nombre al cuadro de texto dependiendo de la posicion"""
                menu.texto1 = Text(menu, height=1, width=2, name = "texto"+str(i+1)+str(j+1), padx=12, pady=12)
                menu.texto1.pack  (side = RIGHT, fill = Y)
                menu.texto1.place  (x   = equis, y    = igriega)

        #########################################BOTONES########################################################
                                          
        menu.boton0    = crearBoton(menu, "boton0", "1", 550, 100, 5, menu.nada)
        menu.boton0.configure    (bg = "gray")

        menu.boton1    = crearBoton(menu, "boton1", "2", 550, 145, 5, menu.nada)
        menu.boton1.configure    (bg = "gray")

        menu.boton2    = crearBoton(menu, "boton2", "3", 550, 190, 5, menu.nada)
        menu.boton2.configure    (bg = "gray")

        menu.boton3    = crearBoton(menu, "boton3", "4", 550, 235, 5, menu.nada)
        menu.boton3.configure    (bg = "gray")

        menu.boton4    = crearBoton(menu, "boton4", "5", 550, 280, 5, menu.nada)
        menu.boton4.configure    (bg = "gray")

        menu.boton5    = crearBoton(menu, "boton5", "6", 550, 325, 5, menu.nada)
        menu.boton5.configure    (bg = "gray")

        menu.nombre = crearEtiqueta(menu, "nombre", "Nombre del jugador", 50, 550)
        menu.nombre.configure (fg = "black")

        menu.txtnombre = crearEtiqueta(menu, "recibe nombre",str(nombreusuario), 250, 550)

        menu.crearCajas(canvas)

        canvas.pack(fill=BOTH, expand=1)


    def crearCajas(menu, canvas):
        """Valores por defecto"""                                          
        global fin
        fin     = False
        doc     = "";
        guardar = False
        
        for digito in documento:
            
            """Para separar niveles"""
            if digito   == "I" or digito == "F" or digito == "D":
                guardar =  False;            
            if guardar  == True:
                doc     += digito;
            if digito   == nivel:
                guardar =  True;
                
        """valores por defecto"""                
        global document
        document = ast.literal_eval(doc)
        doc      = ast.literal_eval(doc)
        contador = 1;

        """mientras el documento no este vacio"""
        while doc != {}:
            """Se generan las lineasque separa cada cuadro"""
            menu.pintarCaja(canvas, doc[contador], doc[contador][0], list(doc[contador][1:]))
            del doc[contador]
            contador +=1;

    def guardar(menu):
        pass

    def cargar(menu):
        pass

    def deshacer(menu):
        pass

    def rehacer(menu):
        pass

    def regresar(menu):
        
        """Destruir esta ventana"""
        menu.destroy();
        
        """Crear la nueva ventana"""
        menu_principal().mainloop();



    def pintarCaja(menu, canvas, numero, etiqueta, lista):

        """la lista deberia de venir ordenada, de izquierda a derecha, de arriba hacia abajo, y deberia de tener al menos un elemento"""
        i = int(lista[0][0]);
        j = int(lista[0][1]);
        
        anchoLinea = 3;
        shiftLeft  = anchoLinea / 2 + 1;

        """primero pintamos la etiqueta"""
        w = Label(menu, name="caja"+str(numero), text= etiqueta, bg =  "#ffffff", fg =  "#4285f4", font = ("Serif", 6));
        w.place  (x=menu.calcularPosX(i-1)+1   , y=menu.calcularPosY(j-1)+1);


        """luego pintamos la caja"""
        size = len (lista)
        for elemento in range (size):
            
            i     = int(lista[elemento][0])
            try:
                j = int(lista[elemento][1])
            except:
                j = lista[elemento][1]
            i2    = i
            j2    = j

            """definimos si hay que remarcar la linea superior"""
            pintarLineaSuperior = True

            for nodo in lista:
                i2 = nodo[0]
                j2 = nodo[1]
                if (i2 == i and j2 == j -1):
                    pintarLineaSuperior =  False;

                if pintarLineaSuperior  == False:
                    break

            if pintarLineaSuperior:
                id = canvas.create_line(menu.calcularPosX(i-1)-shiftLeft, menu.calcularPosY(j-1)-shiftLeft, menu.calcularPosX(i-1)+45, menu.calcularPosY(j-1)-shiftLeft,width=anchoLinea)

            """definimos si hay que remarcar la linea superior"""
            pintarLineaInferior = True
            
            for nodo in lista:
                
                i2 = nodo[0]
                j2 = nodo[1]
                
                if (i2 == i and j2 == j + 1):
                    pintarLineaInferior =  False;

                if pintarLineaInferior  == False:
                    break

            if pintarLineaInferior:
                id = canvas.create_line(menu.calcularPosX(i-1)-shiftLeft, menu.calcularPosY(j-1)+45-shiftLeft, menu.calcularPosX(i-1)+45, menu.calcularPosY(j-1)+45-shiftLeft,width=anchoLinea)
               


            """definimos si hay que remarcar la linea a la izquierda"""
            pintarLineaIzquierda = True
            
            for nodo in lista:

                i2 = nodo[0]
                j2 = nodo[1]

                if (i2 == i - 1 and j2 == j):
                    pintarLineaIzquierda = False

                if pintarLineaIzquierda == False:
                    break

            if pintarLineaIzquierda:
                id = canvas.create_line(menu.calcularPosX(i-1)-shiftLeft, menu.calcularPosY(j-1)-shiftLeft, menu.calcularPosX(i-1)-shiftLeft, menu.calcularPosY(j-1)+45,width=anchoLinea)
             

            """definimos si hay que remarcar la linea a la derecha"""
            pintarLineaDerecha = True
            
            for nodo in lista:

                i2 = nodo[0]
                j2 = nodo[1]

                if (i2 == i + 1 and j2 == j):
                    pintarLineaDerecha =  False

                if pintarLineaDerecha  == False:
                    break

            if pintarLineaDerecha:
                id = canvas.create_line(menu.calcularPosX(i-1)+45-shiftLeft, menu.calcularPosY(j-1)-shiftLeft, menu.calcularPosX(i-1)+45-shiftLeft, menu.calcularPosY(j-1)+45,width=anchoLinea)
              


    def calcularPosX(self, i):
        return 270 + 45 * i

    def calcularPosY(self, j):
        return  100 + 45 * j

    def digitaNumero(menu, numero):
        """Obtiene el nombre del widget"""
        foco       =  menu.focus_get()
        campoTexto = foco.winfo_name()
        try:
            matriz [int(campoTexto[-1])-1][int(campoTexto[-2])-1]= numero
        except:
            messagebox.showinfo("ERROR","PRIMERO DEBE SELECCIONAR UNA CASILLA.")

        """ubica el valor recibido en el campo que tenga el mismo nombre leido anteriormente"""
        if (campoTexto == "texto11" or campoTexto == "texto12" or campoTexto == "texto13"or campoTexto == "texto14"or campoTexto == "texto15"or campoTexto == "texto16"or campoTexto == "texto21"or campoTexto == "texto22"or campoTexto == "texto23"or campoTexto == "texto24"or campoTexto == "texto25"or campoTexto == "texto26"or campoTexto == "texto31"or campoTexto == "texto32"or campoTexto == "texto33"or campoTexto == "texto34"or campoTexto == "texto35"or campoTexto == "texto36"or campoTexto == "texto41"or campoTexto == "texto42"or campoTexto == "texto43"or campoTexto == "texto42"or campoTexto == "texto43"or campoTexto == "texto44"or campoTexto == "texto45"or campoTexto == "texto46"or campoTexto == "texto51"or campoTexto == "texto52"or campoTexto == "texto53"or campoTexto == "texto54"or campoTexto == "texto55"or campoTexto == "texto56"or campoTexto == "texto60"or campoTexto == "texto61"or campoTexto == "texto62"or campoTexto == "texto63"or campoTexto == "texto64"or campoTexto == "texto65"or campoTexto == "texto66"):
            foco.delete('1.0', END)
            foco.insert(END, numero)

            
    def nada (menu):
        messagebox.showinfo("ERROR","NO SE HA INICIADO EL JUEGO.")

    def Key(self, event):
        char = event.char
        foco = self.focus_get()
        foco.delete('1.0', END)

        if char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' :
            numero = int (char)
            campoTexto = foco.winfo_name()
            matriz[int(campoTexto[-1]) - 1][int(campoTexto[-2]) - 1] = numero


    def valida (menu):

        #print ("validar", document)
        #print (matriz)

        #print (document)
        #doc = dic(tuple (doc))
        #if(isinstance(doc, tuple))

        #recorremos todos los elementos de la lista de validaciones, cada elemento corresponde a una validacion especifica
        contador = 1;
        repetidos = True;
        ultimoElemento = len (document)
        #print (menu.iguales())
        if (menu.iguales() == False):
            repetidos = False;
        else:
            repetidos = True
        while contador <= ultimoElemento:
            # el elemento corresponde a una validacion especifica
            elemento = document[contador]
            #print (contador,elemento)

            #obtenemos el tipo de operacion para la validacion que hay que realizar
            operacion = elemento[0][-1]
            #obtenemos el resultado esperado para la validacion que hay que realizar
            resultadoHilera = elemento[0][:len(elemento[0])-1]
            if resultadoHilera == '':
                resultadoHilera = 0
            resultado = int (resultadoHilera)
            #variable para guardar el total calculado en las casillas
            res=0
            #variable que nos indica si la validacion actual es exitosa
            exitoso = False
            #variables para recorrer la lista de casillas a validar, una es la posicion actual, y la otra la final
            posicion = 1
            ultimo = len(elemento)
            # validamos si es multiplicacion
            if (operacion == "x"):
                #print ("validar multiplicacion", contador, elemento)
                #Si es multiplicacion, el valor inicial es 1
                res = 1
                #print ("--",matriz)
                #recorremos todas las casillas, calculando el total mientras lo hacemos
                while posicion < ultimo:
                    caja = elemento[posicion]
                    #print ("----posiciones: ",caja[0], caja[1], "valor",matriz[caja[1]-1][caja[0]-1])
                    valorCaja = int(matriz[caja[1]-1][caja[0]-1])
                    res = res * valorCaja
                    #print ("----valores multi", caja, valorCaja, res)
                    posicion += 1
                #print ("----Esperado", resultado, "Obtenido", res)
                if resultado == res:
                    exitoso = True
                    #print ("----validacion EXITOSA")
                else:
                    #print ("----validacion FALLIDA")
                    repetidos = False

            # validamos si es Suma
            elif (operacion == "+"):
                #print ("validar Suma", contador, elemento)
                #Si es suma, el valor inicial es 0
                res = 0
                #print ("--",matriz)
                #recorremos todas las casillas, calculando el total mientras lo hacemos
                while posicion < ultimo:
                    caja = elemento[posicion]
                    #print ("----posiciones: ",caja[0], caja[1], "valor",matriz[caja[1]-1][caja[0]-1])
                    valorCaja = int(matriz[caja[1]-1][caja[0]-1])
                    res = res + valorCaja
                    #print ("----valores suma", caja, valorCaja, res)
                    posicion += 1
                #print ("----Esperado", resultado, "Obtenido", res)
                if resultado == res:
                    exitoso = True
                    #print ("----validacion EXITOSA")
                else:
                    #print ("----validacion FALLIDA")
                    repetidos = False

            # validamos si es resta
            elif (operacion == "-"):
                #print ("validar Resta", contador, elemento)
                #Si es resta, el valor inicial es -1, como bandera de que debe de ser inicializado con el valor del primer elemento
                res = -1
                #print ("--",matriz)
                #recorremos todas las casillas, calculando el total mientras lo hacemos
                while posicion < ultimo:
                    caja = elemento[posicion]
                    #print ("----posiciones: ",caja[0], caja[1], "valor",matriz[caja[1]-1][caja[0]-1])
                    valorCaja = int(matriz[caja[1]-1][caja[0]-1])
                    if res == -1:
                        res = valorCaja
                    else:
                        res = res - valorCaja
                    #print ("----valores resta", caja, valorCaja, res)
                    posicion += 1
                #print ("----Esperado", resultado, "Obtenido", res)
                if resultado == res:
                    exitoso = True
                    #print ("----validacion EXITOSA")
                else:
                    #print ("----validacion FALLIDA")
                    repetidos = False

            # validamos si es division
            elif (operacion == "/"):
                #print ("validar Division", contador, elemento)
                #Si es division, el valor inicial es -1, como bandera de que debe de ser inicializado con el valor del primer elemento
                res = -1
                #print ("--",matriz)
                #recorremos todas las casillas, calculando el total mientras lo hacemos
                while posicion < ultimo:
                    caja = elemento[posicion]
                    #print ("----posiciones: ",caja[0], caja[1], "valor",matriz[caja[1]-1][caja[0]-1])
                    valorCaja = int(matriz[caja[1]-1][caja[0]-1])
                    if res == -1:
                        res = valorCaja

                    # esto es para evitar division por cero, se podria conciderar enviar un error aca, ç
                    # o talvez validar al inicio que todas las casillas tengan valores validos (de 1 a 6)
                    # y/o que ninguna casilla este vacia.
                    # se podria conciderar dar un mensaje de error si la casilla esta vacia
                    elif res != 0:
                        res = res / valorCaja
                    #print ("----valores division", caja, valorCaja, res)
                    posicion += 1
                #print ("----Esperado", resultado, "Obtenido", res)
                if resultado == res:
                    exitoso = True
                    #print ("----validacion EXITOSA")
                else:
                    #print ("----validacion FALLIDA")
                    repetidos = False

            #menu.pintarCaja(canvas, elemento, elemento[0], list(elemento[1:]))
            #print ( operacion , resultado,veces, list(elemento[1:] ))
            #finalmente modificamos el contador, para asi pasar a la siguiente validacion
            contador +=1     
                
        if repetidos == True:                
            messagebox.showinfo("CORRECTO","¡ FELICITACIONES, JUEGO COMPLETADO !")
            top = leerTop()
            print (top)
            global nombreusuario
            global crono
            if crono == 1:
                global segs
                global mins
                global hrs
                print (str(nombreusuario), hrs, mins, segs)
         
                    
                modificarTop(top,str(nombreusuario), hrs, mins, segs)
            if crono == 2:
                global horasOrig
                global minutosOrig
                global segundosOrig
                global horas
                global minutos
                global segundos
                print (str(nombreusuario), abs(horasOrig-horas), abs (minutosOrig-minutos), abs (SegundosOrig-segundos))
                modificarTop(top,str(nombreusuario), abs(horasOrig-horas), abs (minutosOrig-minutos), abs (SegundosOrig-segundos))
                
            global sonido
            if sonido == True:
                import os
                os.system("xx.mp3")
                

               
            
        else:
            messagebox.showinfo("INCORRECTO","HAY ERRORES EN EL JUEGO")


        
    def iguales(menu):
        valida = True
        for i in range(len(matriz)):
            repetido = False
            repetidos = ""
            for j in range(len(matriz[i])):
                for k in range(len(repetidos)):
                    if repetidos[k] == matriz[i][j]:
                        repetido = True
                        return False
                if not repetido:
                    repetidos += str(matriz[i][j])
                    no_repetidos=0
                    return False
                else:
                    repetidos=1
                    #print("hola")
                    #return True

                
        for h in range(len(matriz)):
            repetido = False
            repetidos = ""
            for d in range(len(matriz)):
                for l in range(len(repetidos)):
                    if repetidos[l] == matriz[d][h]:
                        repetido = True
                        return False
                if not repetido:
                    repetidos += str(matriz[d][h])
                    no_repetidos=0
                    return False
                else:
                    repetidos=1
                    #print("hola")
        return True
        



    """Esta es para cuando se selecciona la imagen del borrador en el juego habiendo seleccionado una casilla"""
    def borrar (menu):
        """Obtiene el nombre del widget"""
        foco       =  menu.focus_get()
        campoTexto = foco.winfo_name()
            
        """ubica el valor recibido en el campo que tenga el mismo nombre leido anteriormente"""
        if (campoTexto == "texto11" or campoTexto == "texto12" or campoTexto == "texto13"or campoTexto == "texto14"or campoTexto == "texto15"or campoTexto == "texto16"or campoTexto == "texto21"or campoTexto == "texto22"or campoTexto == "texto23"or campoTexto == "texto24"or campoTexto == "texto25"or campoTexto == "texto26"or campoTexto == "texto31"or campoTexto == "texto32"or campoTexto == "texto33"or campoTexto == "texto34"or campoTexto == "texto35"or campoTexto == "texto36"or campoTexto == "texto41"or campoTexto == "texto42"or campoTexto == "texto43"or campoTexto == "texto42"or campoTexto == "texto43"or campoTexto == "texto44"or campoTexto == "texto45"or campoTexto == "texto46"or campoTexto == "texto51"or campoTexto == "texto52"or campoTexto == "texto53"or campoTexto == "texto54"or campoTexto == "texto55"or campoTexto == "texto56"or campoTexto == "texto60"or campoTexto == "texto61"or campoTexto == "texto62"or campoTexto == "texto63"or campoTexto == "texto64"or campoTexto == "texto65"or campoTexto == "texto66"):
            foco.delete('1.0', END)
            foco.insert(END, " ")
        else:
            messagebox.showinfo("ERROR","PRIMERO DEBE SELECCIONAR UNA CASILLA.")
    



    def acercaDe(menu):
        """Despliega informacion sobre el programa"""
        messagebox.showinfo("Acerca De", "Autores: Tania María Sánchez Irola\n                Valeria Quesada Benavides \nFecha: 15 de octubre del 2018 \nVersión: 9.2 \nPrograma: Kenken")




    """DESPLEGA LA AYUDA"""
    def ayuda(menu):
        os.startfile("Manual.pdf")
        
    def parar (menu):
        global tiempo
        tiempo = False

        respuesta = tkinter.messagebox.askyesno("DETENIDO","¿REANUDAR?")
        
        if respuesta:
            if crono == 2:
                threading.Thread(target=menu.timer).start()
            else:
                pass
            

        else:
            menu.parar();          
        """menu.botoncronome.   configure(text    = "Continuar"   )
        menu.botoncronome.   configure(command = menu.continuar)"""
        
    def continuar (menu):
        menu.botoncronome.   configure(text    = "Parar"   )
        menu.botoncronome.   configure(command = menu.parar)

    def errores (menu):
        print ("holaaa")
        menu.iniciar;
        

    def iniciar (menu):
        #print("entra")
        global crono

        """Activamos los otros botones"""

        menu.boton0.configure    (command = lambda: menu.digitaNumero("1"))

        menu.boton1.configure    (command = lambda: menu.digitaNumero("2"))

        menu.boton2.configure    (command = lambda: menu.digitaNumero("3"))

        menu.boton3.configure    (command = lambda: menu.digitaNumero("4"))

        menu.boton4.configure    (command = lambda: menu.digitaNumero("5"))

        menu.boton5.configure    (command = lambda: menu.digitaNumero("6"))

        menu.borra.configure     (command = menu.borrar)        

        menu.botoncronome.   configure(fg      = "white"      )
        menu.botoncronome.   configure(command = menu.parar   )
        menu.botontermina.   configure(fg      = "white"      )
        menu.botontermina.   configure(command = menu.termina )
        menu.botonreinicio.  configure(fg      = "white"      )
        menu.botonreinicio.  configure(command = menu.reinicio)
        menu.botonvalidacion.configure(fg      = "white"      )
        menu.botonvalidacion.configure(command = menu.valida  )        
        menu.botonotrojuego. configure(fg      = "white"      )
        menu.botonotrojuego. configure(command = menu.otro    ) 
        menu.botoniniciar.   configure(fg      = "red"        )
        
        threading.Thread(target=menu.coloresCajas).start()
        
        if crono == 2:
            threading.Thread(target=menu.timer).start()
            
        if crono==1:
            #print ("Si")
            menu.textboxhrs = Entry(menu,width=0,font=("Arial",15),name="textboxhrs")
            menu.textboxhrs.place(x=698, y= 50)
            menu.textboxhrs.insert(0,"00")
            menu.textboxmins = Entry(menu,width=0,font=("Arial",15),name="textboxmins")
            menu.textboxmins.place(x=770, y= 50)
            menu.textboxmins.insert(0,"00")
            menu.textboxsegs = Entry(menu,width=0,font=("Arial",15),name="textboxsegs")
            menu.textboxsegs.place(x=845, y= 50)
            menu.textboxsegs.insert(0,"00")               
            global pare
            global flpausa
            global cambiartexto
            global mili
            global segs
            global mins
            global hrs
            global iniciar
            global horasOrig
            global minutosOrig
            global segundosOrig

            #print (segundosOrig)
            
            cambiartexto = 0
            iniciar      = 0
            flpausa      = 0
            
            cont = 0
            fls  = 1
            flh  = 1
            pare = 0

            mili = 0
            segs = int(segundosOrig)
            mins = int(minutosOrig)
            hrs  = int(horasOrig)

            if iniciar==0:
                
                first = time.time()

            elif iniciar!=0:
                
                first = mili

            if flpausa==0 :
                
                while cont<time.time() and pare==0 and fin == False:
                    
                    paso_del_tiempo = int(time.time() - first)
                    mili            = time.time() - first
                    
                    if mili > 0.99:
                        first = time.time()
                        mili  = 0
                        segs  = segs+1
                        
                        """Borrar el resultado anterior cronometro"""
                        
                        menu.textboxsegs.delete(0, END)
                        
                        """Insertar el resultado nuevo cronometro"""
                        menu.textboxsegs.insert(0,'{:02d}'.format(segs))
                        
                    if segs == 59:
                        segs = -1
                
                    if segs==00 and fls == 0:
                        mins = mins + 1

                        """Borrar el resultado anterior"""
                        menu.textboxmins.delete(0, END)

                        """Insertar el resultado nuevo"""
                        menu.textboxmins.insert(0, '{:02d}'.format(mins))
                        fls = 1
                        
                    if segs== 1 and fls == 1:
                        fls = 0

                    if mins == 59:
                        mins = -1
                        
                    if mins == 00 and flh ==0:
                        hrs = hrs+1

                        """Borrar el resultado anterior"""
                        menu.textboxhrs.delete(0, END)
                        
                        """Insertar el resultado nuevo"""
                        menu.textboxhrs.insert(0, '{:02d}'.format(hrs))          

                        """Borrar el resultado anterior"""
                        flh = 1
                        
                    if mins == 1 and flh == 1:
                        flh = 0

                    """cambia el tiempo"""
                    menu.update()
                    """continuar el bucle"""
                    cont    = cont+1
                    iniciar = 1

         
    def timer (menu):
        """Valores por defecto"""
        global horas
        global minutos
        global segundos
        global tiempo
        tiempo   = True
        horas    = int (horas)
        minutos  = int (minutos)
        segundos = int (segundos)
        
        while fin == False and tiempo == True:
            """Actualiza el timer"""
            
            if segundos != 0:
                segundos -= 1

                """Actualiza el cuadro de texto"""
                menu.textboxsegs.delete (0, END)
                menu.textboxsegs.insert (0, segundos)
                
            elif minutos != 0 and segundos == 0:

                segundos =  59
                minutos  -= 1

                """Actualiza el cuadro de texto"""
                menu.textboxsegs.delete (0, END)
                menu.textboxsegs.insert (0, segundos)
                menu.textboxmins.delete (0, END)
                menu.textboxmins.insert (0, minutos)
                
            elif horas != 0 and minutos == 0:
                
                horas   -= 1
                minutos  = 59
                segundos = 59

                """Actualiza el cuadro de texto"""
                menu.textboxhrs.delete (0, END)
                menu.textboxhrs.insert (0, horas)
                menu.textboxmins.delete (0, END)               
                menu.textboxmins.insert (0, minutos)
                menu.textboxsegs.delete (0, END)
                menu.textboxsegs.insert (0, segundos)
                
            elif horas == 0 and minutos == 0 and segundos == 0:
                tiempo = False
                respuesta = tkinter.messagebox.askyesno("CONTINUAR","¿DESEA CONTINUAR?")
                
                if respuesta:
                    global horasOrig
                    global minutosOrig
                    global segundosOrig
                    global segs
                    global mins
                    global hrs
                    global crono
                    segs = segundosOrig
                    #print (segundosOrig)
                    mins = minutosOrig
                    hrs = horasOrig
                    crono = 1                 
                    menu.iniciar();                  

                else:
                    tiempo   = True
                    horas    = int (horasOrig)
                    minutos  = int (minutosOrig)
                    segundos = int (segundosOrig)                    
                    
                    """MUESTRA INFORMACIÓN SOBRE EL PROGRAMA"""
                    menu.destroy()

                    """Crear la nueva ventana"""
                    juego().mainloop()               
                
                
            time.sleep(1)

            
              

    def coloresCajas (menu):
        
        anterior = menu.focus_get()
        
        while fin == False:
            
            """Obtiene el nombre del widget"""
            foco       =  menu.focus_get()
            campoTexto = foco.winfo_name()
            
            """ubica el valor recibido en el campo que tenga el mismo nombre leido anteriormente"""
            if (campoTexto == "texto11" or campoTexto == "texto12" or campoTexto == "texto13"or campoTexto == "texto14"or campoTexto == "texto15"or campoTexto == "texto16"or campoTexto == "texto21"or campoTexto == "texto22"or campoTexto == "texto23"or campoTexto == "texto24"or campoTexto == "texto25"or campoTexto == "texto26"or campoTexto == "texto31"or campoTexto == "texto32"or campoTexto == "texto33"or campoTexto == "texto34"or campoTexto == "texto35"or campoTexto == "texto36"or campoTexto == "texto41"or campoTexto == "texto42"or campoTexto == "texto43"or campoTexto == "texto42"or campoTexto == "texto43"or campoTexto == "texto44"or campoTexto == "texto45"or campoTexto == "texto46"or campoTexto == "texto51"or campoTexto == "texto52"or campoTexto == "texto53"or campoTexto == "texto54"or campoTexto == "texto55"or campoTexto == "texto56"or campoTexto == "texto60"or campoTexto == "texto61"or campoTexto == "texto62"or campoTexto == "texto63"or campoTexto == "texto64"or campoTexto == "texto65"or campoTexto == "texto66"):

                if (foco != anterior):
                    
                    anterior.configure (bg = "white")
                    foco.    configure (bg = "paleturquoise1")
                    
                    anterior = foco
                


                    

    def otro (menu):
        respuesta = tkinter.messagebox.askyesno("OTRO","¿ESTA SEGURO DE TERMINAR ESTE JUEGO Y EMPEZAR CON OTRO?")
        
        if respuesta:
            
            documentos = ["diccionarios.txt","diccionarios - copia.txt","diccionarios - copia (2).txt", "diccionarios - copia (3).txt","diccionarios - copia (4).txt"]   
            global diccionarios
            global documento
            diccionarios = open(str(random.choice(documentos)), "r")
            documento    = diccionarios.read()
            global horasOrig
            global minutosOrig
            global segundosOrig
            segundosOrig = 0
            minutosOrig = 0
            horasOrig = 0             
            
            """MUESTRA INFORMACIÓN SOBRE EL PROGRAMA"""
            menu.destroy()

            """Crear la nueva ventana"""
            juego().mainloop()

        else:
            pass;      



    def termina (menu):
        respuesta = tkinter.messagebox.askyesno("OTRO","¿ESTA SEGURO DE TERMINAR ESTE JUEGO?")
        
        if respuesta:
            """Destruir esta ventana"""
            menu.destroy()

            """Crear la nueva ventana"""
            menu_principal().mainloop()

        else:
            pass                




    def top (menu):
        global top
        try:
            global top2
            top = top2
            top = top.read()
        except:
            pass
        messagebox.showinfo("TOP 10",str(top))



    def reinicio (menu):
        respuesta = tkinter.messagebox.askyesno("REINICIO","¿ESTA SEGURO DE EMPEZAR NUEVAMENTE ESTE MISMO JUEGO?")
        
        if respuesta:
            """MUESTRA INFORMACIÓN SOBRE EL PROGRAMA"""
            menu.destroy()

            """Crear la nueva ventana"""
            juego().mainloop()

        else:
            pass 


    def salir(menu):
        respuesta = tkinter.messagebox.askyesno("Salir","Desea salir?")
        
        if respuesta:
            menu.destroy()

        else:
            pass
    #def ranking (menu):

# lee el archivo top.txt y lo carga en memoria
def leerTop():
    top =[["",0,0,0], ["",0,0,0], ["",0,0,0], ["",0,0,0], ["",0,0,0], ["",0,0,0], ["",0,0,0], ["",0,0,0], ["",0,0,0], ["",0,0,0],]

    with open("top.txt", 'r+') as archivo:
        contenido = archivo.readlines()

        """lee cada linea y la separa"""
        for fila in range(10):
            columnas = contenido[fila].split(':')
            # 0 numero
            # 1 literal nombre
            # 2 nombre \t\tTiempo
            # 3 ' horas'
            # 4 minutos
            # 5 segundos

            #print(columnas)
            nombre  = ""
            horas   = ''
            minutos = ''
            segundos = ''
            #print (len(columnas[0]))

            """extrae el nombre"""
            datos = columnas[2].split(' \t\t')
            nombre = datos[0].lstrip()

            """extrae las horas, minutos y segundos"""
            horas = columnas[3]
            minutos = columnas[4]
            segundos = columnas[5]

            """almacena cada valor en la matriz top"""
            top[fila][0] = nombre;
            top[fila][1] = int(horas);
            top[fila][2] = int(minutos);
            top[fila][3] = int(segundos);
    return top

def guardarTop(top):
    #print (Top)
    global top2
    nuevoTop = ""
    for i in range(10):
        #print(top[i][1])
        n = top[i][0]
        #print (n)
        h = str(top[i][1])
        m = str(top[i][2])
        s = str(top[i][3])

        """compureba que los valores de las horas minutos y segundos sean de dos digitos,
        en caso contrario le agrega un cero adelante para mantener el formato"""

        #print ("nhms", n, h,m,s)

        if int(h) < 10:
            h = "0"+h

        if int(m) < 10:
            m = "0"+m

        if int(s) < 10:
            s = "0"+s

        """comprueba que i sea menor a 10,
        en caso contrario la linea se escribe con un espacio menos para mantener el formato """

        if (i < 9):
            nuevoTop += (str(i+1)+":   Nombre: "+n+" 		Tiempo: "+h+":"+m+":"+s+'\n')

        else:
            nuevoTop += (str(i+1)+":  Nombre: "+n+" 		Tiempo: "+h+":"+m+":"+s+'\n')

    with open("top.txt", 'w') as archivo:
        archivo.write(nuevoTop)
        top2 = open("top.txt", 'r')

def modificarTop(top, nombre, horas, minutos, segundos):
    entrada = [nombre,horas,minutos,segundos]
    modificado = False;

    # tiempo nuevo total, en segundos para que sea mas facil comparar
    nuevoTiempo = segundos + (60 * minutos) + (3600 * horas)
    for fila in range(10):
        #recorremos la lista, si esta en cero, es que no hay nadie en ese campo, asi que procedemos a insertar alli,
        # sacando el ultimo de la lista

        filaActual = top[fila]

        # tiempo actual total, en segundos para que sea mas facil comparar con el tiempo nuevo
        tiempoActual = filaActual[3] + (60 * filaActual[2]) + (3600 * filaActual[1])
        #print ("tiempos fna", fila, nuevoTiempo , tiempoActual)

        # si el nuevo tiempo es menor o igual, hay que insertar el nuevo record,
        # si el tiempo actual es cero, entonces tambien hay que insertar
        if (tiempoActual == 0 or nuevoTiempo <= tiempoActual):
            filaBorrar = top[9]
            top.insert(fila, entrada)
            top.remove (filaBorrar)
            modificado = True
        if (modificado):
            break

    #print ("modificado", modificado )
    if (modificado):
        guardarTop(top)






                
        

def HORAS(horanueva):
    global hay_horas
    global horas    
    hay_horas = 0
    horas     = horanueva
    
    if horas     != "00":
        hay_horas = 1





def MINS(minnuevo):
    global hay_mins
    global minutos
    
    hay_mins = 0
    minutos  = minnuevo

    if minutos!="00":
        hay_mins=1



    
def SEGS(segnuevo):
    global segundos    
    global hay_segs
    hay_segs  = 0
    segundos  = segnuevo
    
    if segundos != "00":
        hay_segs = 1



"""Valores por defecto"""
global top
top = open("top.txt", "r")
top = top.read()

"""Loop de la ventana"""
menu_principal().mainloop()

        

