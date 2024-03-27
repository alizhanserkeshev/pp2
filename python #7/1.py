import tkinter as tk
from PIL import Image, ImageTk
import time
import math

# Function to update the time
def update_time():
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    hour_angle = math.radians((hour % 12) * 30 + minute / 2)
    minute_angle = math.radians(minute * 6 + second / 10)
    second_angle = math.radians(second * 6)

    # Update the clock hands
    canvas.coords(hour_hand, center_x, center_y, center_x + 50 * math.sin(hour_angle), center_y - 50 * math.cos(hour_angle))
    canvas.coords(minute_hand, center_x, center_y, center_x + 70 * math.sin(minute_angle), center_y - 70 * math.cos(minute_angle))
    canvas.coords(second_hand, center_x, center_y, center_x + 80 * math.sin(second_angle), center_y - 80 * math.cos(second_angle))

    # Update the time label
    label.config(text=time.strftime('%H:%M:%S'))
    label.after(1000, update_time)

# Creating the main window
root = tk.Tk()
root.title("Clock with Numbers")

# Load the background image
background_image = Image.open("mickey.png")
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas with background image
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
canvas.create_image(250, 250, image=background_photo)

# Center coordinates of the clock
center_x = 250
center_y = 250

# Draw the clock circle
canvas.create_oval(center_x - 150, center_y - 150, center_x + 150, center_y + 150, width=5)

# Draw the clock numbers
for i in range(1, 13):
    angle = math.radians(i * 30)
    x = center_x + 120 * math.sin(angle)
    y = center_y - 120 * math.cos(angle)
    canvas.create_text(x, y, text=str(i), font=('Arial', 14))

# Load and resize the photo
photo = Image.open("mickey.png")
photo = photo.resize((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(photo)

# Display the photo in the center of the clock
canvas.create_image(center_x, center_y, image=photo)

# Draw the clock hands
hour_hand = canvas.create_line(0, 0, 0, 0, width=6, fill='black')
minute_hand = canvas.create_line(0, 0, 0, 0, width=4, fill='black')
second_hand = canvas.create_line(0, 0, 0, 0, width=2, fill='red')

# Create a label to display the time
label = tk.Label(root, font=('Arial', 20), bg='white')
label.pack()

# Update the time
update_time()

# Run the GUI
root.mainloop()
