from datetime import datetime
import pickle
import uuid
from flask import Flask, request, jsonify
import logging

from predictor import PythonPredictor

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    """Direct API Call"""
    if request.method == "POST":
        model = PythonPredictor()
        payload = request.get_json(force=True)
        prediction = model.predict(payload)

        response = {
            "status": 200,
            "modelID": uuid.uuid1(),
            "prediction": prediction,
            "modelType": "RandomForestModel",
            "created_at": datetime.now(),
            "message": "Success",
        }

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=1957)
