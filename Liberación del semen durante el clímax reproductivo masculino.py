import pygame
import random
import math

pygame.init()

ANCHO = 800
ALTO = 600

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi interfaz")
clock = pygame.time.Clock()

GRAVEDAD = 0.5
FRICCION = 0.85

circulos = []
CREAR_CIRCULO = pygame.USEREVENT + 1
pygame.time.set_timer(CREAR_CIRCULO, 1)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CREAR_CIRCULO:
            radio = 5
            circulos.append({
                "x": 400,
                "y": 300,
                "radio": radio,
                "color": (255,255,255),
                "vx": random.uniform(-3, 3),
                "vy": 0
            })
   
    # física
    for c in circulos:
        c["vy"] += GRAVEDAD
        c["x"] += c["vx"]
        c["y"] -= c["vy"]

        if c["y"] + c["radio"] >= ALTO:
              c["y"] = ALTO - c["radio"]
    #         c["vy"] *= -FRICCION

    #     if c["x"] - c["radio"] <= 0 or c["x"] + c["radio"] >= ANCHO:
    #         c["vx"] *= -1

    # # colisiones
    # for i in range(len(circulos)):
    #     for j in range(i + 1, len(circulos)):
    #         a = circulos[i]
    #         b = circulos[j]
    #         dx = b["x"] - a["x"]
    #         dy = b["y"] - a["y"]
    #         distancia = math.sqrt(dx**2 + dy**2)
    #         if distancia < a["radio"] + b["radio"]:
    #             a["vx"], b["vx"] = b["vx"], a["vx"]
    #             a["vy"], b["vy"] = b["vy"], a["vy"]

    #             overlap = (a["radio"] + b["radio"]) - distancia
    #             a["x"] -= dx / distancia * overlap / 2
    #             a["y"] -= dy / distancia * overlap / 2
    #             b["x"] += dx / distancia * overlap / 2
    #             b["y"] += dy / distancia * overlap / 2

    # dibujo
    ventana.fill((30, 30, 30))

    pygame.draw.circle(ventana, (255, 192, 203), (400, 300), 50)
    pygame.draw.line(ventana, (0, 0, 0), (400, 300), (400, 250), 5)
    pygame.draw.circle(ventana, (226, 188, 157), (400, 390), 50)
    pygame.draw.circle(ventana, (226, 188, 157), (400, 480), 50)
    pygame.draw.circle(ventana, (226, 188, 157), (350, 530), 50)
    pygame.draw.circle(ventana, (226, 188, 157), (450, 530), 50)

    for c in circulos:
        pygame.draw.circle(ventana, c["color"], (int(c["x"]), int(c["y"])), c["radio"])

    pygame.display.update()
    clock.tick(60)

pygame.quit()