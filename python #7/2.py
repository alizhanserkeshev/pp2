import keyboard
import pygame

pygame.mixer.init()

pygame.mixer.music.load("DO4A.mp3")
pygame.mixer.music.play(0)

keyboard.add_hotkey('<your play key>', pygame.mixer.music.play)
keyboard.add_hotkey('<your stop key>', pygame.mixer.music.stop)
keyboard.add_hotkey('<your next key>', pygame.mixer.music.stop)
keyboard.add_hotkey('<your previous key>', pygame.mixer.music.rewind)

while True:
    if pygame.mixer.music.get_busy() == False:
        keyboard.wait()