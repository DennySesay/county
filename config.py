# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'LesFuckingGo??'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///county_game.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False