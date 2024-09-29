from flask import Flask, render_template, request
import pickle # pour charger notre modèle catboost
import pandas as pd

# initialisation de l'application que l'on nomme "app"
app = Flask(__name__)
model = pickle.load(open) 