import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Corredor')
clock = pygame.time.Clock()

teste_superfice = pygame.Surface((100, 200))
teste_superfice.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(teste_superfice, (200, 100))

    pygame.display.update()
    clock.tick(60)