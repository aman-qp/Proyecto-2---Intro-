import tkinter as tk
from PIL import Image, ImageTk
import pygame

pygame.init()

ventana = tk.Tk()
ventana.minsize(width=1000, height=700)
ventana.maxsize(width=1000, height=700)


def mostrar_error(mensaje):
    error_label.config(text=mensaje)

def borrar_error():
    error_label.config(text="")

def nombre_jugador():
    nombre_jugador = nombre.get().strip()
    if nombre_jugador:
        with open("Players.txt", "a") as file:
            file.write(nombre_jugador + "\n")
        nombre.delete(0, "end")
        borrar_error()
        stop()
        play_2()
        pantalla_de_juego(nombre_jugador)
    else:
        mostrar_error("Ingrese un nombre")


def play():
    pygame.mixer.music.load("Multi/sound.mp3")
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def play_2():
    pygame.mixer.music.load("Multi/sound.mp3")
    pygame.mixer.music.play()

canvas = tk.Canvas(ventana, height=700, width=1000)
canvas.pack()

Fondo = Image.open("Multi/bg.png")
Fondo = Fondo.resize((1000, 700))
imagen_tk = ImageTk.PhotoImage(Fondo)
imagen_id = canvas.create_image(0, 0, anchor="nw", image=imagen_tk)

canvas.create_text(430, 263, text="Player:",font=("Fixedsys", 20),fill="white")
nombre = tk.Entry(ventana, font=("Fixedsys", 15))
nombre.place(x=500, y=255)

error_label = tk.Label(ventana, text="", font=("Fixedsys", 15), fg="#EE9322", bg="black")
error_label.place(x=500, y=290)

def pantalla_de_juego(nombre_jugador):
    # Inicializar Pygame
    pygame.init()

    # Definir el tamaño de la ventana
    ventana_ancho = 800
    ventana_alto = 600

    # Crear la ventana
    ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))

    # Definir el título de la ventana
    pygame.display.set_caption("Ventana Principal")
    pygame.mixer.music.load("Multi/sound.mp3")
    pygame.mixer.music.play()
    # Bucle principal del juego
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        # Puedes agregar aquí la lógica de tu juego

        # Actualizar la pantalla
        pygame.display.update()

    # Salir de Pygame
    pygame.quit()


def acerca_de():
    window3= tk.Toplevel(ventana)
    window3.minsize(height=600, width=700)
    window3.maxsize(height=600, width=700)
    window3.config(background="#3D30A2")

    canvas = tk.Canvas(window3, width=700, height=600, bg="#3D30A2")
    canvas.pack()

    Foto_personal = Image.open("Multi/yop.png")
    Foto_personal = Foto_personal.resize((200, 215))
    imagen_tk = ImageTk.PhotoImage(Foto_personal)
    imagen_id = canvas.create_image(0, 0, anchor=tk.NW, image=imagen_tk)
    canvas.coords(imagen_id, 120, 50)
    canvas.image= imagen_tk

    # Agrega la segunda imagen
    Foto_personal2 = Image.open("Multi/Foto-de-portada.png")
    Foto_personal2 = Foto_personal2.resize((200, 215))
    imagen_tk2 = ImageTk.PhotoImage(Foto_personal2)
    imagen_id2 = canvas.create_image(0, 0, anchor=tk.NW, image=imagen_tk2)
    canvas.coords(imagen_id2, 350, 50)  # Ajusta las coordenadas para la segunda imagen

    texto = tk.Label(canvas, text="Instituto Tecnológico de Costa Rica\nIntroducción a la Programación\nIng.Computadores\nEstudiantes: Amanda Quesada Porras\n   Carnet: 2023086337\nIsidro Adrián Acuña Vega\nCarnet: 2023157361\nProfesor: Jeff Smith\nCosta Rica\nVersión: 3.11\n2023",font=("bahnschrift condensed", 18), background="#3D30A2")
    texto.place(x=165, y=270)

    boton = tk.Button(window3, height=2, width=6, background="white", text="Back", font=("Fixedsys", 14),command=window3.destroy)
    boton.place(x=638, y=555)
    window3.mainloop()

def ayuda():
    window2= tk.Toplevel(ventana)
    window2.minsize(height=600, width=500)
    window2.maxsize(height=600, width=500)
    window2.config(background="#EE9322")

    canvas = tk.Canvas(window2, width=500, height=600, bg="#EE9322")
    canvas.pack()

    texto = tk.Label(canvas,text="--Indicaciones a tomar en cuenta--\n\n1.Ingrese un nombre antes de empezar,\nde lo contario el juego no empezará.\n2.Los movimientos del jugador se realizan\ncon las flechas en pantalla.\n3.Asegurese que la versión de python sea\nigual a la que el juego requiere (3.11).\n4.El objetivo principal es matar a todos\nlos robots y pasar al nivel siguiente.\n5.Para eliminar a los robots se puede hacer\nde direfentes maneras, haciendolos chocar\n o utilizando las balas.\n6.Evita chocar con los enemigos porque\npodrías morir.\n7.Usa los metodos de teletranspotación\ncomo una ventaja para ganar.\n8.Toma en cuenta que las balas solo\nfuncionan a dos cuadros de distancia.",font=("bahnschrift condensed", 18), background="#EE9322")
    texto.place(x=85, y=25)

    boton = tk.Button(window2, height=2, width=6, background="white", text="Back", font=("Fixedsys", 14),command=window2.destroy)
    boton.place(x=437, y=553)

#Pantalla de salon de la fama
def salon_de_la_fama():
    window4 = tk.Tk()  # Create a new Tkinter window
    window4.title("Salon de la Fama")
    window4.minsize(height=700, width=700)
    window4.maxsize(height=700, width=700)
    window4.config(background="#EE9322")

    boton = tk.Button(window4, height=2, width=6, background="white", text="Back", font=("Fixedsys", 14), command=window4.destroy)
    boton.place(x=940, y=658)


boton_juego = tk.Button(ventana, height=1, width=15, bg="#3D30A2", borderwidth=8, text="Start Game", font=("Fixedsys", 30), command=nombre_jugador)
boton_ayuda = tk.Button(ventana, height=2, width=16, bg="#3D30A2", borderwidth=8, text="Ayuda", font=("Fixedsys", 17),command=ayuda)
boton_Acerca_de = tk.Button(ventana, height=2, width=12, bg="#3D30A2", borderwidth=8, text="Acerca de.", font=("Fixedsys", 17), command=acerca_de)
boton_salon = tk.Button(ventana, height=2, width=16, bg="#3D30A2", borderwidth=8, text="Salon de la fama", font=("Fixedsys", 17),command=salon_de_la_fama)
boton_salir = tk.Button(ventana, height=2, width=5, bg="#3D30A2", borderwidth=8, text="Salir", font=("Fixedsys", 16), command= ventana.destroy)
boton_play = tk.Button(ventana, height=2, width=5, bg="#3D30A2", borderwidth=8, text="Play", font=("Fixedsys", 16))
boton_mute = tk.Button(ventana, height=2, width=5, bg="#3D30A2", borderwidth=8, text="Mute", font=("Fixedsys", 16))

boton_juego.place(x=320, y=330)
boton_ayuda.place(x=60, y=500)
boton_Acerca_de.place(x=405, y=500)
boton_salon.place(x=680, y=500)
boton_salir.place(x=935, y=645)
boton_play.place(x=4, y=645)
boton_mute.place(x=70, y=645)


ventana.mainloop()