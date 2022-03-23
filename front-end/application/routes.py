from application import app, db
from application.models import Results
from flask import render_template
import requests

@app.route('/')
def index():
    animal = requests.get('http://animal-api:5000/get-animal')
    noise = requests.post('http://noise-api:5000/noise', json=animal.json())
    db.session.add(Results(animal=animal.json()["animal"], noise=noise.json()["noise"]))
    db.session.commit()
    results = Results.query.all()
    return render_template('index.html', results = results)