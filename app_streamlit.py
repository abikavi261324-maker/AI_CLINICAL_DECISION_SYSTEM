import streamlit as st
import random
import time
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

# ---------------- PDF FUNCTION ---------------- #

def generate_pdf(department, prediction, confidence, description):

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(180, 750, "AI Medical Report")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 700, f"Department: {department}")
    pdf.drawString(50, 680, f"Disease: {prediction}")
    pdf.drawString(50, 660, f"Confidence: {confidence}%")
    pdf.drawString(50, 640, f"Description: {description}")

    pdf.drawString(50, 600, "Note: This is a simulated AI system.")

    pdf.save()
    buffer.seek(0)

    return buffer


# ---------------- DATA ---------------- #

data = {
    "Skin": ["Acne", "Psoriasis", "Eczema", "Fungal Infection", "Vitiligo", "Skin Cancer"],
    "Eye": ["Glaucoma", "Cataract", "Retinopathy"],
    "General": ["Diabetes", "Hypertension", "Asthma", "Migraine", "Fever", "Anemia"]
}

descriptions = {
    "Acne": "Skin condition caused by blocked pores.",
    "Psoriasis": "Autoimmune skin disorder.",
    "Eczema": "Inflammation causing itching.",
    "Fungal Infection": "Fungal skin infection.",
    "Vitiligo": "Loss of skin pigmentation.",
    "Skin Cancer": "Abnormal skin cell growth.",

    "Glaucoma": "Damage to optic nerve due to pressure.",
    "Cataract": "Clouding of eye lens.",
    "Retinopathy": "Damage to retina due to diabetes.",

    "Diabetes": "High blood sugar condition.",
    "Hypertension": "High blood pressure.",
    "Asthma": "Airway inflammation.",
    "Migraine": "Severe headache condition.",
    "Fever": "Body temperature rise.",
    "Anemia": "Low hemoglobin level."
}

# ---------------- UI ---------------- #

st.set_page_config(page_title="AI Clinical System", layout="centered")

st.title("🧠 AI Clinical Decision System")
st.markdown("Upload image and get AI-based disease prediction")

category = st.selectbox("Select Disease Type", ["Skin", "Eye", "General"])

uploaded_file = st.file_uploader("Upload Medical Image", type=["jpg", "png", "jpeg"])

# Show image
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

# ---------------- PREDICTION ---------------- #

if st.button("Predict"):

    if uploaded_file is None:
        st.error("Please upload an image first!")

    else:
        st.info("🧠 AI is analyzing image...")
        time.sleep(2)

        prediction = random.choice(data[category])
        confidence = round(random.uniform(88, 98), 2)
        description = descriptions[prediction]

        st.success("Prediction Completed!")

        st.markdown("## 🧾 Result")
        st.write("**Prediction:**", prediction)
        st.write("**Confidence:**", str(confidence) + "%")
        st.write("**Description:**", description)
        st.write("**Model:**", category + "_CNN_Model (Simulated)")

        # ---------------- PDF ---------------- #

        pdf_file = generate_pdf(category, prediction, confidence, description)

        st.download_button(
    label="📄 Download Medical Report (PDF)",
    data=pdf_file,
    file_name="AI_Medical_Report.pdf",
    mime="application/pdf"
)
        


# ---------------- FOOTER ---------------- #

st.markdown("---")
st.markdown(
    "<h3 style='text-align:center;'>🏥 AI Clinical Decision Support System</h3>",
    unsafe_allow_html=True
)