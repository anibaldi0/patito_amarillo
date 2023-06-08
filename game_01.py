import pygame, sys

pygame.init()


screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Patito Amarillo")

running = True

coord_x = 50
coord_y = 50

velocidad_x = 0
velocidad_y = 0
presionado = pygame.key.get_pressed()


player_one = pygame.image

while(running):
    for event in pygame.event.get():
#        print(event)
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
        presionado = pygame.key.get_pressed()
        if presionado[pygame.K_w]:
            velocidad_y = - 0.15
        if presionado[pygame.K_s]:
            velocidad_y = + 0.15
        if presionado[pygame.K_a]:
            velocidad_x = - 0.15
        if presionado[pygame.K_d]:
            velocidad_x = + 0.15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                velocidad_y = 0
            if event.key == pygame.K_s:
                velocidad_y = 0
            if event.key == pygame.K_a:
                velocidad_x = 0
            if event.key == pygame.K_d:
                velocidad_x = 0

        

    screen.fill((255, 255, 255))
    #scope para el draw
    coord_x += velocidad_x
    coord_y += velocidad_y
    image = pygame.image.load("patito_amarillo.png")
    image = pygame.transform.scale(image, (50, 50))
    screen.blit(image, (coord_x, coord_y))



    #actualizar screen
    pygame.display.flip()

pygame.quit()