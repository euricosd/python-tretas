import pygame
from time import sleep
import winsound
from random import randint

def Randomizer():
    global red, green, blue, tone
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    tone = randint(20, 15000)
    return red, green, blue, tone



pygame.init()

window = pygame.display.set_mode((300, 100))

Randomizer()
pygame.draw.rect(window, (red, green, blue), (0, 0, 100, 100))
pygame.display.update()
winsound.Beep(tone, 1000)

Randomizer()
pygame.draw.rect(window, (red, green, blue), (100, 0, 100, 100))
pygame.display.update()
winsound.Beep(tone, 1000)

Randomizer()
pygame.draw.rect(window, (red, green, blue), (200, 0, 100, 100))
pygame.display.update()
winsound.Beep(tone, 1000)

sleep(1)

pygame.quit()
