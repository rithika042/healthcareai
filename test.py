from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import CORS
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)  # Enable CORS for your app

# Load the trained CNN model
model = load_model("skin_cancer_cnn_model.h5")  # Replace with the path to your trained model

@app.route('/')
def home():
    return render_template('admin_dashboard.html')

@app.route('/classify', methods=['POST'])
def classify_image():
    try:
        # Get the uploaded image file from the request
        uploaded_file = request.files['file']

        if uploaded_file.filename != '':
            image = Image.open(uploaded_file).resize((224, 224))
            image = np.array(image) / 255.0
            image = np.expand_dims(image, axis=0)
            prediction = model.predict(image)

            # Assuming your model returns a binary classification result (0 or 1)
            classification_result = "Benign" if prediction < 0.5 else "Malignant"

            # Print the result in the terminal
            print(f"Image classified as: {classification_result}")

            return jsonify({'result': classification_result})
        else:
            return jsonify({'error': 'No file uploaded'})
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the image.'})

if __name__ == '__main__':
    app.run(debug=True)
