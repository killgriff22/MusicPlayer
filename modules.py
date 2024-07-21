import pygame
import flask
import flask_bootstrap
import os
import eyed3
import json

pygame.mixer.init()

app = flask.Flask(__name__)
source_paths = []