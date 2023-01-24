import pickle


class PythonPredictor:
    def __init__(self):
        # Load Model
        self.model = pickle.load(open("rental.pkl", "rb"))

    def predict(self, payload):
        """Predict function"""
        measurements = [
            payload["postcode"],
            payload["sqm"],
            payload["rooms"],
            payload["has_balcony"],
            payload['has_kitchen'],
            payload['has_garden']
        ]
        # Make Predictions
        scores = self.model.predict([measurements])[0]
        return scores
