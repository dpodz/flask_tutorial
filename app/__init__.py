# -*- coding: utf-8 -*-
"""
Created on Mon May  1 13:12:55 2017

@author: podloda
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models