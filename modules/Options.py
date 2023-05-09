"""Archivo de configuracion"""
#Ancho de la pantalla
WIDTH = 1000
#Alto de la pantalla
HEIGHT = 600

#Color negro y blanco, evita tenet que declararlo
BLACK = (0,0,0)
WHITE =(255, 255, 255)
#velocidad estandar. Se usa tanto en la nave, como en la velocidad vertical de los asteroides
SPEED = 3

#Rutas a los sprites de los asteroides
MED_ASTEROID_IMG_1 = "assets/sprites/asteroid_med1.png"
BIG_ASTEROID_IMG_1 = "assets/sprites/asteroid_big1.png"

#Lista de frames de la explosion

EXPLOSION_LIST =["assets/sprites/Explosion00.png","assets/sprites/Explosion01.png","assets/sprites/Explosion02.png","assets/sprites/Explosion03.png","assets/sprites/Explosion04.png","assets/sprites/Explosion05.png","assets/sprites/Explosion06.png","assets/sprites/Explosion07.png","assets/sprites/Explosion08.png"]

#Ruta del sprite de la nave
SHIP_IMG= "assets/sprites/ship.png"

#Ruta al fondo de la pantalla
BACKGROUND_IMG = "assets/images/fondo.png"

#Ruta a la imagen de la bala
BULLET_IMG="assets/sprites/bullet.png"
#Ruta al sonido de disparo de la bala
BULLET_SD="assets/sounds/bullet_sound.ogg"
#Ruta al sonido de la explosion.
EXPLOSION_SD="assets/sounds/explosion.wav"

#Instrucciones del juego
INSTRUCTIONS = "W(Arriba) S(Abajo) A(Izquierda) D (Derecha)"

