from application import app
from flask import request, jsonify

noises = dict(cow='moo', dog='woof', sheep='baa', cat='meow', pig='oink')

@app.route('/noise', methods=['POST'])
def noise():
    animal_json = request.get_json()
    animal = animal_json["animal"]
    return jsonify(noise=noises[animal])