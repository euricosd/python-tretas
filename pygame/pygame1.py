import pygame
from time import sleep

pygame.init()

window = pygame.display.set_mode((500, 400))

pygame.draw.rect(window, (255,0,0), (0,0,400,100))

pygame.display.update()

sleep(10)

pygame.quit()
