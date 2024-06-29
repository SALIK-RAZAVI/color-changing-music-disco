import tkinter as tk
import random
import winsound  # Windows-specific library for playing .wav files

# Dictionary mapping temperature ranges to music files
temperature_music = {
    (0, 10): "winter_wind.wav",
    (11, 20): "spring_birds.wav",
    (21, 30): "summer_beach.wav",
    (31, 40): "autumn_leaves.wav"
}

# List of colors for the disco ball
disco_ball_colors = [
    "red", "green", "blue", "yellow", "purple", "orange"
]

# Function to change disco ball color randomly
def change_color():
    color = random.choice(disco_ball_colors)
    ball.config(bg=color)

# Function to play music based on temperature
def play_music():
    temperature = random.randint(0, 40)  # Simulating room temperature
    for temp_range, music_file in temperature_music.items():
        if temp_range[0] <= temperature <= temp_range[1]:
            winsound.PlaySound(music_file, winsound.SND_ASYNC | winsound.SND_LOOP)
            break
    else:
        winsound.PlaySound("default_music.wav", winsound.SND_ASYNC | winsound.SND_LOOP)  # Default music

# Creating main window
root = tk.Tk()
root.title("Color-Changing Disco Ball with Temperature-based Music")

# Disco ball widget
ball = tk.Label(root, width=20, height=20, bg="white", relief="sunken")
ball.pack(pady=20)

# Buttons to change color and play music
tk.Button(root, text="Change Color", command=change_color).pack(pady=10)
tk.Button(root, text="Play Music", command=play_music).pack(pady=10)

# Running the GUI loop
root.mainloop()
