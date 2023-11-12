import tkinter as tk
from PIL import Image, ImageTk
import pygame
import sys
import numpy as np
from pygame.locals import MOUSEBUTTONDOWN
import random

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

canvas.create_text(430, 263, text="Player:", font=("Fixedsys", 20), fill="white")
nombre = tk.Entry(ventana, font=("Fixedsys", 15))
nombre.place(x=500, y=255)

error_label = tk.Label(ventana, text="", font=("Fixedsys", 15), fg="#EE9322", bg="black")
error_label.place(x=500, y=290)


def guardar_puntaje(nombre_jugador, puntos):
    with open("Players.txt", "a") as file:
        file.write(f"{nombre_jugador} - Puntos: {puntos}\n")


def pantalla_de_juego(nombre_jugador):
    # Definir dimensiones del tablero
    ancho = 40
    alto = 36

    # Crear una matriz para representar el tablero
    tablero = np.zeros((ancho, alto), dtype=int)

    # Llenar el tablero con las paredes azules (valor 0)
    tablero.fill(0)
    puntos = 0

    class Pacman:
        def __init__(self, x, y, tablero):
            self.x = x
            self.y = y
            self.tablero = tablero
            self.direction = (0, 0)
            self.image = pygame.image.load("Multi/pacman.png")
            self.image = pygame.transform.scale(self.image, (20, 20))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)
            self.is_alive = True

        def move(self):
            if self.is_alive:
                new_x = self.x + self.direction[0]
                new_y = self.y + self.direction[1]

                # Verificar colisiones con las paredes
                if not self.collides_with_wall(new_x, new_y) and 0 <= new_x < ancho and 0 <= new_y < alto:
                    # Verificar si la casilla de destino no es 5
                    if self.tablero[new_x][new_y] != 5:
                        # Dibujar un cuadro negro en la casilla anterior
                        self.draw_black_square()
                        self.x = new_x
                        self.y = new_y
                        self.rect.topleft = (self.x * TILE_SIZE, self.y * TILE_SIZE)
                        # Marcar el alimento como comido si es 1
                        self.eat_puntos()
                        # Marcar la cápsula como comida si es 2
                        self.eat_capsule(bola_1, bola_2)
                        # Marcar la cápsula como comida si es 3
                        self.eat_food()

        def collides_with_wall(self,x, y):
            # Verificar colisiones con las paredes en el tablero
            if 0 <= x < ancho and 0 <= y < alto and self.tablero[x][y] == 0:
                return True
            return False

        def eat_puntos(self):
            nonlocal puntos
            if self.is_alive and self.tablero[self.x][self.y] == 1:
                self.tablero[self.x][self.y] = 4  # Marcar el alimento como comido
                puntos += 1

        def eat_food(self):
            nonlocal puntos
            if self.is_alive and self.tablero[self.x][self.y] == 3:
                self.tablero[self.x][self.y] = 4  # Marcar el alimento como comido
                puntos += 50

        def eat_capsule(self, bola_1, bola_2):
            nonlocal puntos
            if self.is_alive and self.tablero[self.x][self.y] == 2:
                self.tablero[self.x][self.y] = 4  # Marcar la cápsula como comida
                puntos += 50

        def draw_black_square(self):
            # Dibujar un cuadro negro en la casilla anterior
            surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
            surface.fill((0, 0, 0))
            ventana.blit(surface, (self.x * TILE_SIZE, self.y * TILE_SIZE))

        def die(self):
            self.is_alive = False

        def display(self, screen):
            if self.is_alive:
                screen.blit(self.image, self.rect)

        def check_collision(self, fantasmas):
            for fantasma in fantasmas:
                if fantasma.estado and self.rect.colliderect(fantasma.rect):
                    return True
            return False

    class Fantasma:
        def __init__(self, x, y, color, tablero):
            self.estado = True  # Inicialmente vivo
            self.x = x
            self.y = y
            self.color = color
            self.tablero = tablero
            self.velocidad = 1  # Velocidad por defecto
            self.imagen = pygame.image.load(f"Multi/{color}.png")
            self.imagen = pygame.transform.scale(self.imagen, (20, 20))
            self.rect = self.imagen.get_rect()
            self.rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)
        def display(self, screen):
            if self.estado:
                screen.blit(self.imagen, self.rect)

        def move(self):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            possible_moves = []

            for direction in directions:
                next_x = self.x + direction[0]
                next_y = self.y + direction[1]

                # Verificar si la siguiente posición es válida (no es una pared)
                if 0 <= next_x < len(self.tablero) and 0 <= next_y < len(self.tablero[0]) and self.tablero[next_x][next_y] != 0:
                    possible_moves.append(direction)

            if possible_moves:
                self.direction = random.choice(possible_moves)

        def update(self):
            if self.estado:
                self.move()
                self.x += self.direction[0] * self.velocidad
                self.y += self.direction[1] * self.velocidad
                self.rect.topleft = (self.x * TILE_SIZE, self.y * TILE_SIZE)


    # Constante para el tamaño de las casillas (tiles)
    TILE_SIZE = 20  # Tamaño de 20x20 píxeles

    # Agregar puntos de alimento (valor 1) y cápsulas (valor 2) en posiciones específicas
    # Por ejemplo, aquí agregamos alimento en las coordenadas (5, 5) y cápsulas en las coordenadas (10, 10)

    tablero[0][5] = 1
    tablero[1][5] = 1
    tablero[2][5] = 1
    tablero[3][5] = 1
    tablero[4][5] = 1
    tablero[5][5] = 1
    tablero[6][5] = 1
    tablero[7][5] = 3
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
    tablero[0][20] = 3
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
    tablero[29][20] = 3
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

    tablero[22][21] = 5
    tablero[22][22] = 5

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
    tablero[32][33] = 3
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
    tablero[20][9] = 3
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
    tablero[29][6] = 3
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
    tablero[3][21] = 3
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
    tablero[5][33] = 3
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

    tablero[24][24] = 5
    tablero[23][24] = 5
    tablero[22][24] = 5
    tablero[21][24] = 5
    tablero[20][24] = 5

    tablero[24][23] = 5
    tablero[23][23] = 5
    tablero[22][23] = 5
    tablero[21][23] = 5
    tablero[20][23] = 5

    # Inicializar variables para las bolas
    bola_1 = []
    bola_2 = []

    # Crear una instancia de Pacman
    pacman = Pacman(17, 5, tablero)

    # Crear instancias de Fantasmas
    fantasma_rojo = Fantasma(24, 23, "rojo", tablero)
    fantasma_celeste = Fantasma(23, 23, "celes", tablero)
    fantasma_rosa = Fantasma(22, 23, "rosa", tablero)
    fantasma_naranja = Fantasma(21, 23, "naran", tablero)

    # Iniciar el juego y actualizar el tablero en tiempo real
    pygame.init()

    # Crear una ventana principal
    ventana_ancho= (ancho+20)*TILE_SIZE
    ventana_alto = alto * TILE_SIZE
    ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
    pygame.display.set_caption("Pacman")

    imagen_pared = pygame.image.load("Multi/Fondo (1).png")
    imagen_TNT = pygame.image.load("Multi/TNT (1).png")
    imagen_comida=pygame.image.load("Multi/comida.png")

    # Cargar la imagen del cuadro negro
    imagen_negra = pygame.Surface((TILE_SIZE, TILE_SIZE))
    imagen_negra.fill((0, 0, 0))

    def parpadeo():
        # Obtén el tiempo actual
        tiempo_actual = pygame.time.get_ticks()

        # Haz que la imagen parpadee entre imagen_TNT y imagen_pared cada medio segundo
        if (tiempo_actual // 300) % 2 == 0:
            imagen = imagen_TNT
        else:
            imagen = pygame.Surface((TILE_SIZE, TILE_SIZE))  # Crea un cuadro negro de 20x20
            imagen.fill((0, 0, 0))  # Llena el cuadro con color negro
        return imagen

    clock = pygame.time.Clock()
    frame_rate = 60  # Cambia la tasa de fotogramas a 60 FPS
    tiempo_anterior = pygame.time.get_ticks()

    button_rect = pygame.Rect(ventana_ancho - 110, 10, 100, 40)

    def draw_exit_button():
        # Dibujar el botón de salida en la esquina superior derecha
        font = pygame.font.Font(None, 36)
        button_text = font.render("Salir", True, (0, 0, 0))
        button_rect = button_text.get_rect()
        button_rect.topleft = (ventana_ancho - button_rect.width - 10, 10)
        ventana.blit(button_text, button_rect)
        pygame.draw.rect(ventana, (255, 0, 0), button_rect, 0)
        ventana.blit(button_text, button_rect.topleft)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    guardar_puntaje(nombre_jugador, puntos)
                    pygame.quit()
                    #sys.exit()


        # Manejo de entrada del jugador para mover al Pac-Man
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            pacman.direction = (0, -1)
        elif keys[pygame.K_DOWN]:
            pacman.direction = (0, 1)
        elif keys[pygame.K_LEFT]:
            pacman.direction = (-1, 0)
        elif keys[pygame.K_RIGHT]:
            pacman.direction = (1, 0)

        # Mover al Pac-Man
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - tiempo_anterior >= 12000 / frame_rate:
            pacman.move()
            # Actualizar la posición de los fantasmas
            fantasma_rojo.update()
            fantasma_celeste.update()
            fantasma_rosa.update()
            fantasma_naranja.update()
            tiempo_anterior = tiempo_actual

        # Verificar colisiones con fantasmas
        if pacman.check_collision([fantasma_rojo, fantasma_celeste, fantasma_rosa, fantasma_naranja]):
            # Mostrar el mensaje en el centro de la ventana
            font_perdiste = pygame.font.Font(None, 72)
            mensaje_perdiste = font_perdiste.render("PERDISTE", True, (255, 0, 0))
            mensaje_rect = mensaje_perdiste.get_rect(center=(ventana_ancho // 2, ventana_alto // 2))
            ventana.blit(mensaje_perdiste, mensaje_rect)

            pygame.display.flip()

            # Esperar un momento antes de cerrar la ventana
            pygame.time.delay(8000)


        pygame.draw.rect(ventana, (0, 0, 0), (0, 0, ventana_ancho, ventana_alto))

        # Dibujar el tablero en la pantalla
        for x in range(ancho):
            for y in range(alto):
                if tablero[x][y] == 0:
                    ventana.blit(imagen_pared, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif tablero[x][y] == 1:
                    color = (255, 255, 0)  # Amarillo para la bola
                    pygame.draw.circle(ventana, color, (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2),4)
                    bola_1.append((x, y))
                elif tablero[x][y] == 2:
                    imagen = parpadeo()
                    ventana.blit(imagen, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                    bola_2.append((x, y))
                elif tablero[x][y] == 3:
                    ventana.blit(imagen_comida, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif tablero[x][y] == 4:
                    color = (0, 0, 0)
                    pygame.draw.circle(ventana, color, (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2),4)
                elif tablero[x][y] == 5:
                    color = (0, 0, 0)
                    pygame.draw.circle(ventana, color, (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2),4)

        # Verificar si todos los 1 han sido cambiados por 4
        if all(1 not in fila for fila in tablero):
            # Mostrar el mensaje en el centro del lado derecho de la ventana
            font = pygame.font.Font(None, 36)
            mensaje_ganador = font.render("¡Felicidades, ganaste!", True, (255, 255, 255))
            mensaje_rect = mensaje_ganador.get_rect(topleft=(880, 315))
            ventana.blit(mensaje_ganador, mensaje_rect)

            # Añadir un botón "Siguiente nivel"
            font_boton = pygame.font.Font(None, 30)
            texto_boton = font_boton.render("Siguiente nivel", True, (0,0,0))
            boton_rect = texto_boton.get_rect(topleft=(950, 360))

            # Dibujar el botón
            pygame.draw.rect(ventana, (0x61, 0xA3, 0xBA), boton_rect)
            ventana.blit(texto_boton, boton_rect.topleft)
            pygame.time.delay(5000)

        #Dibujar los fantasmas en la pantalla

        fantasma_rojo.display(ventana)
        fantasma_celeste.display(ventana)
        fantasma_rosa.display(ventana)
        fantasma_naranja.display(ventana)

        # Dibujar al Pac-Man en la pantalla
        pacman.display(ventana)

        # Dibujar el botón de salida
        draw_exit_button()

        #Muestra el nombre del jugador
        font = pygame.font.Font(None, 36)
        text = font.render(f"Player: {nombre_jugador}", True, (0, 0, 0))
        text_rect = text.get_rect(topleft=(850, 90))
        pygame.draw.rect(ventana, (0x61, 0xA3, 0xBA), text_rect, 0)
        ventana.blit(text, text_rect.topleft)

        # Muestrar puntos en la pantalla
        font = pygame.font.Font(None, 36)
        text = font.render(f"Points: {puntos}", True, (0, 0, 0))
        text_rect = text.get_rect(topleft=(850, 130))
        pygame.draw.rect(ventana, (0x61, 0xA3, 0xBA), text_rect, 0)
        ventana.blit(text, text_rect.topleft)

        # Muestrar nivel en la pantalla
        font = pygame.font.Font(None, 36)
        text = font.render(f"Level: 1", True, (0, 0, 0))
        text_rect = text.get_rect(topleft=(850, 50))
        pygame.draw.rect(ventana, (0x61, 0xA3, 0xBA), text_rect, 0)
        ventana.blit(text, text_rect.topleft)

        pygame.display.flip()
        clock.tick(frame_rate)


def acerca_de():
    window3= tk.Toplevel(ventana)
    window3.minsize(height=600, width=550)
    window3.maxsize(height=600, width=550)
    window3.config(background="#61A3BA")

    canvas = tk.Canvas(window3, width=550, height=600, bg="#61A3BA")
    canvas.pack()

    def add_border(image, border_size):
        width, height = image.size
        new_width = width + 2 * border_size
        new_height = height + 2 * border_size
        new_image = Image.new("RGB", (new_width, new_height), "grey")
        new_image.paste(image, (border_size, border_size))
        return new_image

    Foto_personal = Image.open("Multi/yop.png")
    Foto_personal = Foto_personal.resize((200, 215))
    Foto_personal = add_border(Foto_personal, border_size=5)
    imagen_tk = ImageTk.PhotoImage(Foto_personal)
    imagen_id = canvas.create_image(0, 0, anchor=tk.NW, image=imagen_tk)
    canvas.coords(imagen_id, 60, 40)
    canvas.image= imagen_tk

    # Agrega la segunda imagen
    Foto_personal2 = Image.open("Multi/Foto-de-portada.png")
    Foto_personal2 = Foto_personal2.resize((200, 215))
    Foto_personal2 = add_border(Foto_personal2, border_size=5)
    imagen_tk2 = ImageTk.PhotoImage(Foto_personal2)
    imagen_id2 = canvas.create_image(0, 0, anchor=tk.NW, image=imagen_tk2)
    canvas.coords(imagen_id2, 290, 40)  # Ajusta las coordenadas para la segunda imagen

    texto = tk.Label(canvas, text="Instituto Tecnológico de Costa Rica\nIntroducción a la Programación\nIng.Computadores\nEstudiantes: Amanda Quesada Porras\n   Carnet: 2023086337\nIsidro Adrián Acuña Vega\nCarnet: 2023157361\nProfesor: Jeff Smith\nCosta Rica\nVersión: 3.11\n2023",font=("bahnschrift condensed", 18), background="#61A3BA")
    texto.place(x=130, y=270)

    boton = tk.Button(window3, height=2, width=6, background="white", text="Back", font=("Fixedsys", 14),command=window3.destroy)
    boton.place(x=487, y=555)
    window3.mainloop()

def ayuda():
    window2= tk.Toplevel(ventana)
    window2.minsize(height=650, width=550)
    window2.maxsize(height=650, width=550)
    window2.config(background="#61A3BA")

    canvas = tk.Canvas(window2, width=550, height=650, bg="#61A3BA")
    canvas.pack()

    texto = tk.Label(canvas,text="Este famoso juego consiste en personificar a Pac-Man–quien\nestá en un laberinto neón– y su objetivo es recorrer el espacio\n para comer todas las bolas “energizantes” \nsin ser atrapado por los fantasmas.\n\n--Indicaciones a tomar en cuenta--\n\n1.Ingrese un nombre antes de empezar,\nde lo contario el juego no empezará.\n2.Los movimientos del pacman se realizan\ncon las flechas del teclado.\n3.Asegurese que la versión de python sea\nigual a la que el juego requiere (3.11).\n4.El objetivo principal es comerse todos los \npuntos amarillos a lo largo de el mapa.\n5.Para eliminar a los fantasmas debera\ncomerse un TNT para tener la \nhabilidad de comerselos.\n6.Evita chocar con los fantasmas sin el \n poder o moriras.\n7.Las manzanas suman 50 puntos más.",font=("bahnschrift condensed", 18), background="#61A3BA")
    texto.place(x=10, y=25)

    boton = tk.Button(window2, height=2, width=6, background="white", text="Back", font=("Fixedsys", 14),command=window2.destroy)
    boton.place(x=487, y=603)

#Pantalla de salon de la fama
def salon_de_la_fama():
    window4 = tk.Tk()  # Create a new Tkinter window
    window4.title("Salon de la Fama")
    window4.minsize(height=600, width=500)
    window4.maxsize(height=600, width=500)
    window4.config(background="#61A3BA")

    canvas = tk.Canvas(window4, width=500, height=600, bg="#61A3BA")
    canvas.pack()

    texto = tk.Label(canvas,text="Mejores Puntuaciones",font=("bahnschrift condensed", 26), background="#61A3BA")
    texto.place(x=130, y=25)

    boton = tk.Button(window4, height=2, width=6, background="white", text="Back", font=("Fixedsys", 14), command=window4.destroy)
    boton.place(x=940, y=658)

    # Leer los nombres desde el archivo
    try:
        with open("Players.txt", "r") as file:
            nombres = file.readlines()
    except FileNotFoundError:
        nombres = []

    # Mostrar los nombres en la ventana con enumeración
    y_position = 100
    for i, nombre in enumerate(nombres, start=0):
        label = tk.Label(canvas, text=f"{i}. {nombre.strip()}", font=("Fixedsys", 18), background="#61A3BA")
        label.place(x=80, y=y_position)
        y_position += 50

boton_juego = tk.Button(ventana, height=1, width=15, bg="#3D30A2", borderwidth=8, text="Start Game", font=("Fixedsys", 30), command=nombre_jugador)
boton_ayuda = tk.Button(ventana, height=2, width=16, bg="#3D30A2", borderwidth=8, text="Ayuda", font=("Fixedsys", 17),command=ayuda)
boton_Acerca_de = tk.Button(ventana, height=2, width=12, bg="#3D30A2", borderwidth=8, text="Acerca de.", font=("Fixedsys", 17), command=acerca_de)
boton_salon = tk.Button(ventana, height=2, width=16, bg="#3D30A2", borderwidth=8, text="Salon de la fama", font=("Fixedsys", 17),command=salon_de_la_fama)
boton_salir = tk.Button(ventana, height=2, width=5, bg="#3D30A2", borderwidth=8, text="Salir", font=("Fixedsys", 16), command= ventana.destroy)


boton_juego.place(x=320, y=330)
boton_ayuda.place(x=60, y=500)
boton_Acerca_de.place(x=405, y=500)
boton_salon.place(x=680, y=500)
boton_salir.place(x=935, y=645)
ventana.mainloop()
