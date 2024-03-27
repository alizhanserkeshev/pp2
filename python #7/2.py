import keyboard
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Load music file
pygame.mixer.music.load("DO4A.mp3")

# Define keyboard shortcuts
keyboard.add_hotkey('<your play key>', pygame.mixer.music.play)
keyboard.add_hotkey('<your stop key>', pygame.mixer.music.stop)
keyboard.add_hotkey('<your next key>', pygame.mixer.music.stop)
keyboard.add_hotkey('<your previous key>', pygame.mixer.music.rewind)

# Main loop
while True:
    if pygame.mixer.music.get_busy() == False:
        # If the music is not playing, wait for a key press
        keyboard.wait()