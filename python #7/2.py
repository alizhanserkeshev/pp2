import keyboard
import pygame
import tkinter as tk
from tkinter import messagebox

pygame.mixer.init()

music_files = ["DO4A.wav", "Major.wav", "Shape.wav"]

current_music = 0

def play_music():
    global current_music
    if current_music < len(music_files):
        pygame.mixer.music.load(music_files[current_music])
        pygame.mixer.music.play()
        label.config(text=f"Now playing: {music_files[current_music]}")
        current_music += 1
    else:
        label.config(text="All music files played!")

def pause_music():
    pygame.mixer.music.pause()
    label.config(text="Music paused")

def stop_music():
    pygame.mixer.music.stop()
    label.config(text="Music stopped")

def next_music():
    global current_music
    if current_music!=(music_files.count-1):
        current_music = max(0, current_music - 1)
    else:
        current_music = 0
    play_music()

def previous_music():
    global current_music
    if current_music!=(music_files.count-1):
        current_music = max(0, current_music + 1)
    else:
        current_music = (music_files.count-1)
    play_music()

root = tk.Tk()
root.title("Music Player")
root.geometry("300x200")

label = tk.Label(root, text="", font=("Helvetica", 12))
label.pack(pady=10)

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack()

previous_button = tk.Button(root, text="Previous", command=previous_music)
previous_button.pack()

next_button = tk.Button(root, text="Next", command=next_music)
next_button.pack()

root.mainloop()
