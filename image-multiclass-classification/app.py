import base64
import io

from flask import Flask, jsonify, request
from PIL import Image


app = Flask(__name__)


def get_model_prediction(img):
    '''Run model inference for a single image and return results here.'''
    
    # This is an example stub that returns a pre-generated output.
    # You should implement the body of this function to parse the 
    # `img` input data as features for your model, run the model
    # inference and return the output based on the documented
    # model prediction format under Docker Image Details section.
    
    # Example model output for multiclass classification with 5 classes:
    return [ 0.1, 0.5, 0.1, 0.2, 0.1 ]


@app.route('/health-check', methods=['GET'])
def healt_check():
    return 'OK'


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    img = Image.open(io.BytesIO(base64.b64decode(data['image'])))
    try:
        preds = get_model_prediction(img)
    except Exception:
        return 'Failed to get prediction', 500
    return jsonify({'predictions': preds})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)