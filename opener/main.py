import logging
import time
import tkinter as tk
import pystray  # type: ignore
import json
import subprocess
from PIL import Image


_LOGGER = logging.getLogger(__name__)
VERSION = "0.0.0-develop"


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


def launch_apps() -> None:
    """
    Launches the applications listed in the config.

    Returns:
        None
    """
    config = read_config()
    for app in config["apps"]:
        _LOGGER.info("- Launching %s", app["name"])
        subprocess.Popen(app["command"])

        # Wait for the application to launch
        time.sleep(5)


def setup_systray_menu_and_launch_apps(icon: pystray.Icon) -> None:
    """
    Sets up the systray menu and launches the applications.

    Parameters:
        icon (Icon): The icon to set up the systray menu for.

    Returns:
        None
    """
    icon.visible = True

    _LOGGER.info("Launching applications")
    launch_apps()


def main() -> None:
    """
    Initializes the main function.
    """
    _LOGGER.info("Reading configuration file")
    config = read_config()
    _LOGGER.setLevel(config.get("logLevel", "INFO"))
    _LOGGER.info("Creating systray menu")
    image_path = config.get("image_path", "img/can-opener.ico")
    image = Image.open(image_path)
    icon = pystray.Icon(
        "name",
        image,
        "Opener",
        menu=pystray.Menu(
            pystray.MenuItem(f"Opener v{VERSION}", lambda text: None),
            pystray.MenuItem("Exit", create_menu),
        ),
    )

    icon.run(setup_systray_menu_and_launch_apps)


if __name__ == "__main__":
    main()
