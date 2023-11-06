import tkinter as tk
from PIL import Image, ImageTk
import pygame
import sys
import numpy as np

bola_1 = []
bola_2 = []

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
    tablero[28][16] = 1
    tablero[28][17] = 1
    tablero[28][18] = 1
    tablero[28][19] = 1
    tablero[28][20] = 1

    tablero[5][16] = 1
    tablero[5][15] = 1
    tablero[5][14] = 1
    tablero[6][14] = 1
    tablero[7][14] = 1
    tablero[7][13] = 1
    tablero[7][12] = 1
    tablero[7][11] = 1
    tablero[7][10] = 1
    tablero[7][9] = 1
    tablero[6][9] = 1
    tablero[5][9] = 1
    tablero[4][9] = 1
    tablero[4][8] = 1
    tablero[4][7] = 1
    tablero[4][5] = 1
    tablero[4][6] = 1

    tablero[0][20] = 1
    tablero[0][21] = 1
    tablero[0][22] = 1
    tablero[0][23] = 1
    tablero[0][24] = 1
    tablero[0][25] = 1
    tablero[1][25] = 1
    tablero[2][25] = 1
    tablero[3][25] = 1
    tablero[4][25] = 1
    tablero[5][25] = 1
    tablero[6][25] = 1
    tablero[7][25] = 1
    tablero[7][24] = 1
    tablero[7][23] = 1
    tablero[7][22] = 1
    tablero[8][22] = 1
    tablero[9][22] = 1
    tablero[10][22] = 1
    tablero[11][22] = 1
    tablero[12][22] = 1
    tablero[13][22] = 1
    tablero[14][22] = 1
    tablero[10][21] = 1
    tablero[10][20] = 1
    tablero[10][19] = 1
    tablero[10][18] = 1
    tablero[7][22] = 1
    tablero[6][22] = 1
    tablero[5][22] = 1
    tablero[5][21] = 1
    tablero[4][21] = 1
    tablero[3][21] = 1
    tablero[2][21] = 1
    tablero[1][21] = 1
    tablero[4][26] = 1
    tablero[4][27] = 1
    tablero[4][28] = 1
    tablero[4][29] = 1
    tablero[5][29] = 1
    tablero[6][29] = 1
    tablero[6][30] = 1
    tablero[6][31] = 1
    tablero[6][32] = 1
    tablero[7][29] = 1
    tablero[8][29] = 1
    tablero[9][29] = 1
    tablero[9][28] = 1
    tablero[10][28] = 1
    tablero[11][28] = 1
    tablero[11][27] = 1
    tablero[11][26] = 1
    tablero[12][26] = 1
    tablero[13][26] = 1
    tablero[14][26] = 1
    tablero[13][33] = 1
    tablero[14][33] = 1
    tablero[12][33] = 1
    tablero[11][33] = 1
    tablero[10][33] = 1
    tablero[9][33] = 1
    tablero[8][33] = 1
    tablero[7][33] = 1
    tablero[6][33] = 1
    tablero[5][33] = 1
    tablero[4][33] = 1
    tablero[3][33] = 1
    tablero[2][33] = 1
    tablero[1][33] = 1
    tablero[0][33] = 1
    tablero[0][17] = 2
    tablero[28][10] = 2
    tablero[34][31] = 2
    tablero[6][34] = 2
    tablero[15][20] = 2



    # Iniciar el juego y actualizar el tablero en tiempo real
    pygame.init()
    ventana = pygame.display.set_mode((ancho * 20, alto * 20))

    imagen_pared = pygame.image.load("Multi/Fondo (1).png")
    imagen_TNT = pygame.image.load("Multi/TNT (1).png")

    def parpadeo():
        # Obtén el tiempo actual
        tiempo_actual = pygame.time.get_ticks()

        # Haz que la imagen parpadee entre imagen_TNT y imagen_pared cada medio segundo
        if (tiempo_actual // 300) % 2 == 0:
            imagen = imagen_TNT
        else:
            imagen = pygame.Surface((20, 20))  # Crea un cuadro negro de 20x20
            imagen.fill((0, 0, 0))  # Llena el cuadro con color negro
        return imagen

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Dibujar el tablero en la pantalla
        for x in range(ancho):
            for y in range(alto):
                if tablero[x][y] == 0:
                    ventana.blit(imagen_pared, (x * 20, y * 20, 20, 20))
                elif tablero[x][y] == 1:
                    color = (255, 255, 0)  # Amarillo para la bola
                    pygame.draw.circle(ventana, color, (x * 20 + 10, y * 20 + 10), 4)
                    bola_1.append((x, y))  # Guardar las coordenadas de la bola 1
                elif tablero[x][y] == 2:
                    imagen = parpadeo()  # Usa la función de parpadeo para obtener la imagen
                    ventana.blit(imagen, (x * 20, y * 20, 20, 20))
                    bola_2.append((x, y))  # Guardar las coordenadas de la bola 2

        pygame.display.flip()



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