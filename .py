from flask import Flask, send_file
from PIL import Image
import os

app = Flask(__name__)

# 1. On crée l'image une fois pour toutes
print("Création de l'image tracker...")
img = Image.new('RGBA', (1, 1), (0, 0, 0, 0))
img.save('tracker.png')

# 2. Route pour servir l'image
@app.route('/tracker')
def get_tracker():
    # Flask nous donne l'IP de la personne qui demande
