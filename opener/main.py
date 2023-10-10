import tkinter as tk
import pystray  # type: ignore
import json
from PIL import Image


def create_menu(icon, item) -> None:
    """
    Creates a menu.

    Args:
        icon: The icon for the menu.
        item: The item in the menu.

    Returns:
        None
    """
    if item.text == "Exit":
        icon.stop()


def read_config(path: str = "config.json") -> dict:
    """
    Reads the configuration from the 'config.json' file.

    Returns: (dict) The configuration data as a dictionary.
    """
    with open(path, "r") as f:
        config = json.load(f)
    return config


def setup(icon: pystray.Icon) -> None:
    """
    Sets the visibility of the given icon.

    Parameters:
        icon (Icon): The icon to set the visibility for.

    Returns:
        None
    """
    icon.visible = True


def main() -> None:
    """
    Initializes the main function.
    """
    config = read_config()
    image_path = config.get("image_path", "img/can-opener.ico")
    image = Image.open(image_path)
    icon = pystray.Icon(
        "name",
        image,
        "My System Tray Icon",
        menu=pystray.Menu(
            pystray.MenuItem("Opener v0.1.0", lambda text: None),
            pystray.MenuItem("Exit", create_menu),
        ),
    )
    icon.run(setup)


if __name__ == "__main__":
    main()
