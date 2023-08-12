import tkinter as tk
import pystray
from PIL import Image

def create_menu(icon, item):
    if item.text == 'Exit':
        icon.stop()

def setup(icon):
    icon.visible = True

def main():
    image_path = "img/can-opener.ico"
    image = Image.open(image_path)
    icon = pystray.Icon("name", image, "My System Tray Icon", menu=pystray.Menu(pystray.MenuItem('Version 0.1.0', lambda text: None), pystray.MenuItem('Exit', create_menu)))
    icon.run(setup)

if __name__ == "__main__":
    main()
