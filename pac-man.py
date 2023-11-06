import tkinter as tk
from PIL import Image, ImageTk
import pygame
import sys
import numpy as np

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
        """stop()
        play_2()"""
        pantalla_de_juego()
    else:
        mostrar_error("Ingrese un nombre")


"""def play():
    pygame.mixer.music.load("Multi/sound.mp3")
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def play_2():
    pygame.mixer.music.load("Multi/sound.mp3")
    pygame.mixer.music.play()"""

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

def pantalla_de_juego():
    # Definir dimensiones del tablero
    ancho = 40
    alto = 36

    # Crear una matriz para representar el tablero
    tablero = np.zeros((ancho, alto), dtype=int)

    # Llenar el tablero con las paredes azules (valor 0)
    tablero.fill(0)

    # Agregar puntos de alimento (valor 1) y cápsulas (valor 2) en posiciones específicas
    # Por ejemplo, aquí agregamos alimento en las coordenadas (5, 5) y cápsulas en las coordenadas (10, 10)
    tablero[0][5] = 1
    tablero[1][5] = 1
    tablero[2][5] = 1
    tablero[3][5] = 1
    tablero[4][5] = 1
    tablero[5][5] = 1
    tablero[6][5] = 1
    tablero[7][5] = 1
    tablero[8][5] = 1
    tablero[9][5] = 1
    tablero[10][5] = 1
    tablero[11][5] = 1
    tablero[12][5] = 1
    tablero[13][5] = 1
    tablero[14][5] = 1
    tablero[15][5] = 1
    tablero[15][6] = 1
    tablero[15][7] = 1
    tablero[15][8] = 1
    tablero[15][9] = 1
    tablero[15][10] = 1
    tablero[15][11] = 1
    tablero[15][12] = 1
    tablero[15][13] = 1
    tablero[15][14] = 1
    tablero[15][15] = 1
    tablero[14][12] = 1
    tablero[13][12] = 1
    tablero[12][12] = 1
    tablero[11][12] = 1
    tablero[10][12] = 1
    tablero[9][12] = 1
    tablero[8][12] = 1
    tablero[7][12] = 1
    tablero[6][12] = 1
    tablero[5][12] = 1
    tablero[4][12] = 1
    tablero[3][12] = 1
    tablero[2][12] = 1
    tablero[1][12] = 1
    tablero[0][12] = 1
    tablero[0][13] = 1
    tablero[0][14] = 1
    tablero[0][15] = 1
    tablero[0][16] = 1
    tablero[0][17] = 1
    tablero[0][18] = 1
    tablero[0][19] = 1
    tablero[0][20] = 1
    tablero[15][12] = 1
    tablero[15][16] = 1
    tablero[15][17] = 1
    tablero[15][18] = 1
    tablero[15][19] = 1
    tablero[15][20] = 1
    tablero[15][21] = 1
    tablero[15][22] = 1
    tablero[1][17] = 1
    tablero[2][17] = 1
    tablero[3][17] = 1
    tablero[4][17] = 1
    tablero[5][17] = 1
    tablero[6][17] = 1
    tablero[7][17] = 1
    tablero[8][17] = 1
    tablero[9][17] = 1
    tablero[10][17] = 1
    tablero[11][17] = 1
    tablero[12][17] = 1
    tablero[13][17] = 1
    tablero[14][17] = 1
    tablero[15][17] = 1
    tablero[16][8] = 1
    tablero[17][8] = 1
    tablero[16][20] = 1
    tablero[17][20] = 1
    tablero[18][20] = 1
    tablero[19][20] = 1
    tablero[20][20] = 1
    tablero[21][20] = 1
    tablero[22][20] = 1
    tablero[23][20] = 1
    tablero[24][20] = 1
    tablero[25][20] = 1
    tablero[26][20] = 1
    tablero[27][20] = 1
    tablero[28][20] = 1
    tablero[29][20] = 1
    tablero[30][20] = 1
    tablero[31][20] = 1
    tablero[32][20] = 1
    tablero[33][20] = 1
    tablero[34][20] = 1
    tablero[35][20] = 1
    tablero[36][20] = 1
    tablero[37][20] = 1
    tablero[38][20] = 1
    tablero[39][20] = 1
    tablero[22][21] = 1
    tablero[20][22] = 1
    tablero[19][22] = 1
    tablero[19][23] = 1
    tablero[19][24] = 1
    tablero[19][25] = 1
    tablero[21][22] = 1
    tablero[22][22] = 1
    tablero[23][22] = 1
    tablero[24][22] = 1
    tablero[25][22] = 1
    tablero[25][23] = 1
    tablero[25][24] = 1
    tablero[20][25] = 1
    tablero[21][25] = 1
    tablero[22][25] = 1
    tablero[23][25] = 1
    tablero[24][25] = 1
    tablero[25][25] = 1
    tablero[15][23] = 1
    tablero[15][24] = 1
    tablero[15][25] = 1
    tablero[15][26] = 1
    tablero[15][27] = 1
    tablero[15][28] = 1
    tablero[15][29] = 1
    tablero[15][30] = 1
    tablero[15][31] = 1
    tablero[15][32] = 1
    tablero[15][33] = 1
    tablero[15][34] = 1
    tablero[15][35] = 1
    tablero[16][33] = 1
    tablero[17][33] = 1
    tablero[18][33] = 1
    tablero[19][33] = 1
    tablero[20][33] = 1
    tablero[21][33] = 1
    tablero[22][33] = 1
    tablero[23][33] = 1
    tablero[24][33] = 1
    tablero[25][33] = 1
    tablero[26][33] = 1
    tablero[27][33] = 1
    tablero[28][33] = 1
    tablero[29][33] = 1
    tablero[30][33] = 1
    tablero[31][33] = 1
    tablero[32][33] = 1
    tablero[33][33] = 1
    tablero[34][33] = 1
    tablero[35][33] = 1
    tablero[36][33] = 1
    tablero[37][33] = 1
    tablero[38][33] = 1
    tablero[39][33] = 1
    tablero[39][32] = 1
    tablero[39][31] = 1
    tablero[39][30] = 1
    tablero[39][29] = 1
    tablero[39][28] = 1
    tablero[39][27] = 1
    tablero[38][27] = 1
    tablero[37][27] = 1
    tablero[36][27] = 1
    tablero[35][27] = 1
    tablero[34][27] = 1
    tablero[33][27] = 1
    tablero[32][27] = 1
    tablero[31][27] = 1
    tablero[31][26] = 1
    tablero[31][25] = 1
    tablero[31][24] = 1
    tablero[31][23] = 1
    tablero[35][28] = 1
    tablero[35][29] = 1
    tablero[35][30] = 1
    tablero[34][30] = 1
    tablero[34][31] = 1
    tablero[32][28] = 1
    tablero[32][29] = 1
    tablero[32][30] = 1
    tablero[32][31] = 1
    tablero[32][32] = 1
    tablero[31][29] = 1
    tablero[30][29] = 1
    tablero[29][29] = 1
    tablero[29][28] = 1
    tablero[32][28] = 1
    tablero[29][28] = 1

    tablero[28][30] = 1
    tablero[29][30] = 1
    tablero[27][30] = 1
    tablero[26][30] = 1
    tablero[25][30] = 1
    tablero[24][30] = 1
    tablero[23][30] = 1
    tablero[23][29] = 1
    tablero[22][29] = 1
    tablero[23][31] = 1
    tablero[23][32] = 1

    tablero[20][10] = 1
    tablero[20][9] = 1
    tablero[19][9] = 1
    tablero[18][9] = 1
    tablero[17][9] = 1
    tablero[21][10] = 1
    tablero[22][10] = 1
    tablero[23][10] = 1
    tablero[24][10] = 1
    tablero[25][10] = 1
    tablero[26][10] = 1
    tablero[26][11] = 1
    tablero[26][12] = 1
    tablero[26][13] = 1
    tablero[26][14] = 1
    tablero[26][15] = 1
    tablero[27][15] = 1
    tablero[28][15] = 1

    tablero[29][15] = 1
    tablero[30][15] = 1
    tablero[31][15] = 1
    tablero[31][14] = 1
    tablero[31][13] = 1
    tablero[31][12] = 1
    tablero[31][11] = 1
    tablero[31][10] = 1
    tablero[30][10] = 1
    tablero[27][10] = 1
    tablero[28][10] = 1
    tablero[29][10] = 1
    tablero[28][9] = 1
    tablero[28][7] = 1
    tablero[28][8] = 1
    tablero[28][6] = 1
    tablero[29][6] = 1
    tablero[30][6] = 1
    tablero[31][6] = 1
    tablero[32][6] = 1
    tablero[27][6] = 1
    tablero[26][6] = 1
    tablero[25][6] = 1
    tablero[24][6] = 1
    tablero[22][5] = 1
    tablero[23][5] = 1
    tablero[24][5] = 1

    tablero[21][5] = 1
    tablero[20][5] = 1
    tablero[19][5] = 1
    tablero[18][5] = 1
    tablero[17][5] = 1
    tablero[16][5] = 1
    tablero[33][6] = 1
    tablero[34][6] = 1
    tablero[35][6] = 1
    tablero[36][6] = 1
    tablero[37][6] = 1
    tablero[37][7] = 1
    tablero[37][8] = 1
    tablero[37][9] = 1
    tablero[37][10] = 1
    tablero[37][11] = 1
    tablero[37][12] = 1
    tablero[36][12] = 1
    tablero[35][12] = 1
    tablero[34][12] = 1
    tablero[33][12] = 1
    tablero[32][12] = 1
    tablero[31][12] = 1























    tablero[0][17] = 2
    tablero[10][10] = 2

    # Iniciar el juego y actualizar el tablero en tiempo real
    pygame.init()
    ventana = pygame.display.set_mode((ancho * 20, alto * 20))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Dibujar el tablero en la pantalla
        for x in range(ancho):
            for y in range(alto):
                if tablero[x][y] == 0:
                    color = (0, 0, 255)  # Azul para las paredes
                elif tablero[x][y] == 1:
                    color = (255, 255, 255)  # Blanco para el alimento
                elif tablero[x][y] == 2:
                    color = (255, 0, 0)  # Rojo para las cápsulas
                pygame.draw.rect(ventana, color, (x * 20, y * 20, 20, 20))

        pygame.display.flip()


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
# Ejecutar la función principal del juego
ventana.mainloop()