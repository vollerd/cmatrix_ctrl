"""A simple script to start and stop cmatrix with a given color and speed."""

import subprocess
import argparse
from enum import Enum

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"
    CYAN = "cyan"
    MAGENTA = "magenta"
    WHITE = "white"
    BLACK = "black"
    MULTI = "multi"

def start_cmatrix(speed=1, color=Color.GREEN.value):
    """Starts the cmatrix command with the given speed and color."""
    if color == Color.MULTI.value:
        command = f"cmatrix -s {speed} | lolcat"
    else:
        command = f"cmatrix -s {speed} -C {color}"
    try:
        subprocess.Popen(command, shell=True)
    except Exception as e:
        print(f"Failed to start cmatrix: {e}")

def stop_cmatrix():
    """Stops the cmatrix command."""
    try:
        subprocess.run("pkill cmatrix", shell=True)
    except Exception as e:
        print(f"Failed to stop cmatrix: {e}")

def parse_args():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description='Control cmatrix.')
    parser.add_argument('command', choices=['start', 'stop'] + [color.value for color in Color], help='The command to execute.')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if args.command == "start":
        start_cmatrix()
    elif args.command == "stop":
        stop_cmatrix()
    elif args.command in [color.value for color in Color]:
        start_cmatrix(1, args.command)