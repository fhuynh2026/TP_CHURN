from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Charger le modèle
model = joblib.load('data/churn_model_clean.pkl')

# Page principale
@app.route('/')
def home():
    return render_template('index.html')

# API de prédiction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        features = np.array([[
            float(data['Age']),
            float(data['Account_Manager']),
            float(data['Years']),
            float(data['Num_Sites'])
        ]])

        prediction = model.predict(features)[0]
        proba = model.predict_proba(features)[0][1]

        return jsonify({
            'prediction': int(prediction),
            'probability': float(proba)
        })

    except Exception as e:
        return jsonify({'error': str(e)})

# Lancer l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
