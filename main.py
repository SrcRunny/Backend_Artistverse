from flask import Flask, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def greeting():
    return ("Hello World!")

@app.route('/test', methods=['GET'])
def homepage():
    return jsonify({'text':"Python blyt",
                    'Pree':404}), 200

with open("./Model/LyricsGenerator/model.pkl", "rb") as input_file:
    model = pickle.load(input_file)

if __name__ == '__main__':
    app.run(debug=True)

