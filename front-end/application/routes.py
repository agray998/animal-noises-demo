from application import app
import requests

@app.route('/')
def index():
    animal = requests.get('http://animal-api:5000/get-animal')
    noise = requests.post('http://noise-api:5000/noise', json=animal.json())
    return f'{animal.json()["animal"]} goes {noise.json()["noise"]}'