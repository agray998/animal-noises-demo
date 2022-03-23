from application import app
from flask import jsonify
from random import choice

animals = ['cow', 'dog', 'cat', 'sheep', 'pig']

@app.route('/get-animal', methods=['GET'])
def get_animal():
    animal = choice(animals)
    return jsonify(animal=animal)