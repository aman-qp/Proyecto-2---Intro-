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
    window1 = tk.Toplevel(ventana)
    window1.geometry("1000x700")
    window1.minsize(height=700, width=1000)
    window1.maxsize(height=700, width=1000)
    window1.config(background="white")

    def stop():
        pygame.mixer.music.stop()

    def play():
        pygame.mixer.music.load("Multi/sound.mp3")
        pygame.mixer.music.play()

    def regreso():
        stop()
        window1.destroy()

    canvas = tk.Canvas(window1, width=1000, height=700, bg="white")
    canvas.pack()

    frame = tk.Frame(window1, bg="#EE9322", width=100, height=100)
    frame.place(x=25, y=110)
    nombre = tk.Label(frame, text=f"Player: {nombre_jugador}", font=("Fixedsys", 16), fg="white", bg="#EE9322")
    nombre.pack(fill="both", expand=False, padx=0, pady=10)

    frame1 = tk.Frame(window1, bg="#EE9322", width=100, height=100)
    frame1.place(x=25, y=175)
    score = tk.Label(frame1, text=f"Score: 0", font=("Fixedsys", 16), fg="white", bg="#EE9322")
    score.pack(fill="both", expand=False, padx=0, pady=10)

    frame2 = tk.Frame(window1, borderwidth=3, relief="solid", bg="#219C90", width=100, height=100)
    frame2.place(x=760, y=10)
    nivel = tk.Label(frame2, text=f"Nivel 1", font=("Fixedsys", 20), fg="white", bg="#219C90")
    nivel.pack(fill="both", expand=False, padx=0, pady=10)

    boton = tk.Button(window1, height=2, width=6, background="white", text="Back", font=("Fixedsys", 14),command=regreso)
    boton.place(x=935, y=6)

    boton = tk.Button(window1, height=2, width=6, background="white", text="Mute", font=("Fixedsys", 14), command=stop)
    boton.place(x=10, y=6)

    boton = tk.Button(window1, height=2, width=6, background="white", text="Play", font=("Fixedsys", 14), command=play)
    boton.place(x=70, y=6)

    window1.mainloop()

def acerca_de():
    window3= tk.Toplevel(ventana)
    window3.minsize(height=600, width=700)
    window3.maxsize(height=600, width=700)
    window3.config(background="#3D30A2")

    canvas = tk.Canvas(window3, width=700, height=600, bg="#3D30A2")
    canvas.pack()

    Foto_personal = Image.open("Multi/yop.png")
    Foto_personal = Foto_personal.resize((200, 200))
    imagen_tk = ImageTk.PhotoImage(Foto_personal)
    imagen_id = canvas.create_image(0, 0, anchor=tk.NW, image=imagen_tk)
    canvas.coords(imagen_id, 120, 50)
    canvas.image= imagen_tk

    texto = tk.Label(canvas,text="Estudiantes: Amanda Quesada Porras\nCarnet: 2023086337\nInstituto Tecnológico de Costa Rica\nIntroducción a la Programación\nIng.Computadores\nProfesor:Jeff Smith\nCosta Rica\nVersión:3.11\n2023", font=("bahnschrift condensed", 18), background="#3D30A2")
    texto.place(x=110, y=290)

    boton = tk.Button(window3, height=2, width=6, background="white", text="Back", font=("Fixedsys", 14),command=window3.destroy)
    boton.place(x=638, y=555)

boton_juego = tk.Button(ventana, height=1, width=15, bg="#3D30A2", borderwidth=8, text="Start Game",font=("Fixedsys", 30), command=nombre_jugador)
boton_ayuda = tk.Button(ventana, height=2, width=16, bg="#3D30A2", borderwidth=8, text="Ayuda", font=("Fixedsys", 17))
boton_Acerca_de = tk.Button(ventana, height=2, width=12, bg="#3D30A2", borderwidth=8, text="Acerca de.",font=("Fixedsys", 17),command=acerca_de)
boton_salon = tk.Button(ventana, height=2, width=16, bg="#3D30A2", borderwidth=8, text="Salon de la fama",font=("Fixedsys", 17))
boton_salir = tk.Button(ventana, height=2, width=5, bg="#3D30A2", borderwidth=8, text="Salir", font=("Fixedsys", 16))
boton_play = tk.Button(ventana, height=2, width=5, bg="#3D30A2", borderwidth=8, text="Play", font=("Fixedsys", 16))
boton_mute = tk.Button(ventana, height=2, width=5, bg="#3D30A2", borderwidth=8, text="Mute", font=("Fixedsys", 16))
boton_config = tk.Button(ventana, height=2, width=6, bg="#3D30A2", borderwidth=8, text="Config.", font=("Fixedsys", 16))

boton_juego.place(x=320, y=330)
boton_ayuda.place(x=60, y=500)
boton_Acerca_de.place(x=405, y=500)
boton_salon.place(x=680, y=500)
boton_salir.place(x=935, y=645)
boton_play.place(x=4, y=645)
boton_mute.place(x=70, y=645)
boton_config.place(x=860, y=645)

ventana.mainloop()