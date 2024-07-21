import pygame
import flask
import flask_bootstrap
import os
import eyed3
import json
import threading
import atexit
import sys
import ast

pygame.mixer.init()
queuefile = "queue.txt"
app = flask.Flask(__name__)
source_paths = [
    "/media/New Volume/Music/Skye's/Backup/Heap/",
    "C:/Users/kilgr/Music",
    "./"
]

Shutdown_Flag = threading.Event()

def print_at(x, y, content):
    sys.stdout.write(f"\x1b7\x1b[{y};{x}f{content}\x1b8")
    sys.stdout.flush()


def clear():
    os.system("clear")


class Fore:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'


class Back:
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'


RESET = '\033[0m'


def info(message: str) -> None:
    return (f"{Fore.BLACK}{Back.BLUE}{message}{RESET}")


def warn(message: str) -> None:
    return (f"{Fore.BLACK}{Back.YELLOW}{message}{RESET}")


def error(message: str) -> None:
    return f"{Fore.BLACK}{Back.RED}{message}{RESET}"


def success(message: str) -> None:
    return (f"{Fore.BLACK}{Back.GREEN}{message}{RESET}")