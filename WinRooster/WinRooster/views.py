"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, make_response, Flask
from WinRooster import app
import urllib.request
import json
from ics import Calendar, Event

@app.route('/')
@app.route('/home')
def home():
    c = Calendar()
    with urllib.request.urlopen("http://api.windesheim.nl/api/Klas/ICTSECENG/Les") as url:
        data = json.loads(url.read().decode())
    for d in data:
        e = Event()
        e.name = d['commentaar']
        stijd = d['starttijd'] / 1000
        etijd = d['eindtijd'] / 1000
        e.begin = stijd
        e.end = etijd
        e.location = d['lokaal']
        c.events.add(e)
    response = make_response(str(c))
    response.headers["Content-Disposition"] = "attachment; filename=ICTSECENG.ics"
    return response