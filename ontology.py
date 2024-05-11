
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Set up MongoDB connection
client = MongoClient('mongodb+srv://test:771377@cluster0.06rut.mongodb.net/')
db = client['test']
collection = db['music']

# Model
class Entity:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description
        }


@app.route('/', methods=['POST'])
def create_ontology():
    try:
        data = request.json
        entity = Entity(data['name'], data['description'])
        collection.insert_one(entity.to_json())
        return jsonify(entity.to_json()), 201

    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        app.logger.error(f"Request data: {request.data}")
        app.logger.error(f"Request headers: {request.headers}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)