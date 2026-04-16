from flask import Flask, render_template, request, jsonify
import random
import time

app = Flask(__name__)

# ---------------- DISEASE DATABASE ---------------- #

DATA = {
    "skin": ["Acne", "Psoriasis", "Eczema", "Fungal Infection", "Vitiligo", "Skin Cancer"],
    "eye": ["Glaucoma", "Cataract", "Retinopathy"],
    "general": ["Diabetes", "Hypertension", "Asthma", "Migraine", "Fever", "Anemia"]
}

DESCRIPTIONS = {
    "Acne": "Skin condition caused by blocked pores.",
    "Psoriasis": "Autoimmune skin disorder.",
    "Eczema": "Inflammation causing itching.",
    "Fungal Infection": "Fungal infection of skin.",
    "Vitiligo": "Loss of skin pigmentation.",
    "Skin Cancer": "Abnormal skin cell growth.",

    "Glaucoma": "Damage to optic nerve due to pressure.",
    "Cataract": "Clouding of eye lens.",
    "Retinopathy": "Damage to retina due to diabetes.",

    "Diabetes": "High blood sugar condition.",
    "Hypertension": "High blood pressure.",
    "Asthma": "Airway inflammation.",
    "Migraine": "Severe headache disorder.",
    "Fever": "Increase in body temperature.",
    "Anemia": "Low hemoglobin level."
}

# ---------------- HOME ---------------- #

@app.route('/')
def home():
    return render_template("index.html")

# ---------------- MOCK CNN AI PREDICTION ---------------- #

@app.route('/predict', methods=['POST'])
def predict():

    file = request.files.get('image')
    category = request.form.get("category")

    if not file:
        return jsonify({
            "prediction": "No Image Uploaded",
            "confidence": 0,
            "description": "Please upload an image.",
            "model": "None"
        })

    # ---------------- SIMULATE AI PROCESSING ---------------- #
    time.sleep(2)  # AI processing delay

    def ai_engine(diseases):
        prediction = random.choice(diseases)
        confidence = round(random.uniform(88, 98), 2)
        return prediction, confidence

    # ---------------- CATEGORY MODELS ---------------- #

    if category in DATA:
        prediction, confidence = ai_engine(DATA[category])
    else:
        prediction = "Unknown"
        confidence = 80.0

    # ---------------- RESPONSE ---------------- #

    return jsonify({
        "prediction": prediction,
        "confidence": confidence,
        "description": DESCRIPTIONS.get(prediction, "Consult a doctor."),
        "model": category + "_CNN_Model (Simulated)"
    })

# ---------------- RUN APP ---------------- #

if __name__ == '__main__':
    app.run(debug=True)