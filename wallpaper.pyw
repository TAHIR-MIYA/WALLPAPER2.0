import ctypes
import os
import random

WALLPAPER_FOLDER = r"D:\TAHIR CODE\wallpaper2.0\wallpaperimage"

images = [file for file in os.listdir(WALLPAPER_FOLDER) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

chosen_image = random.choice(images)
image_path = os.path.join(WALLPAPER_FOLDER, chosen_image)

ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
