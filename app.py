import streamlit as st
import pdfplumber

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="CARE-AI Nova Copilot",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------
# CUSTOM UI STYLE
# -----------------------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

.main {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

.title {
    text-align:center;
    font-size:48px;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    font-size:22px;
    margin-bottom:30px;
}

.card {
    background:#1e293b;
    padding:25px;
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.markdown('<div class="title">🩺 CARE-AI Nova Copilot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Health Assistant Prototype</div>', unsafe_allow_html=True)

st.write("Enter your symptoms, upload medical reports, or ask a health question.")

# -----------------------------
# USER INPUT
# -----------------------------
user_input = st.text_area(
    "Describe your symptoms",
    placeholder="Example: fever headache fatigue"
)

uploaded_file = st.file_uploader(
    "Upload medical report (PDF or Image)",
    type=["pdf","png","jpg","jpeg"]
)

# -----------------------------
# PDF READER
# -----------------------------
def read_pdf(file):

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()

    return text


# -----------------------------
# SYMPTOM ANALYSIS
# -----------------------------
def analyze_symptoms(symptoms):

    symptoms = symptoms.lower()

    result = {
        "condition": "General health discomfort",
        "risk": "Low",
        "actions": [
            "Drink plenty of water",
            "Get enough rest",
            "Monitor symptoms for 24 hours"
        ],
        "recovery": [
            "Maintain healthy diet",
            "Stay hydrated",
            "Consult a doctor if symptoms worsen"
        ]
    }

    if "fever" in symptoms and "headache" in symptoms:

        result = {
            "condition": "Possible Viral Fever or Flu",
            "risk": "Medium",
            "actions": [
                "Take adequate rest",
                "Drink warm fluids frequently",
                "Use fever medication like paracetamol if needed"
            ],
            "recovery": [
                "Maintain hydration",
                "Eat light nutritious food",
                "Avoid cold drinks and heavy meals",
                "Consult doctor if fever lasts more than 3 days"
            ]
        }

    elif "cough" in symptoms and "sore throat" in symptoms:

        result = {
            "condition": "Upper Respiratory Infection",
            "risk": "Low",
            "actions": [
                "Drink warm water frequently",
                "Use throat lozenges",
                "Avoid cold foods and drinks"
            ],
            "recovery": [
                "Take steam inhalation twice daily",
                "Drink herbal tea or warm soup",
                "Rest your voice",
                "Visit doctor if cough lasts more than 5 days"
            ]
        }

    elif "chest pain" in symptoms or "shortness of breath" in symptoms:

        result = {
            "condition": "Possible Cardiovascular or Lung Issue",
            "risk": "High",
            "actions": [
                "Stop any physical activity immediately",
                "Sit in a comfortable upright position",
                "Seek emergency medical assistance"
            ],
            "recovery": [
                "Get immediate medical evaluation",
                "Follow doctor’s prescribed treatment",
                "Avoid physical stress",
                "Monitor blood pressure regularly"
            ]
        }

    elif "stomach pain" in symptoms or "vomiting" in symptoms:

        result = {
            "condition": "Possible Gastritis or Food Poisoning",
            "risk": "Medium",
            "actions": [
                "Drink oral rehydration solution (ORS)",
                "Avoid spicy or oily food",
                "Rest the stomach for few hours"
            ],
            "recovery": [
                "Eat light foods like rice or toast",
                "Stay hydrated with electrolyte drinks",
                "Avoid dairy and heavy meals",
                "Consult doctor if vomiting persists"
            ]
        }

    elif "fatigue" in symptoms and "dizziness" in symptoms:

        result = {
            "condition": "Possible Dehydration or Low Blood Pressure",
            "risk": "Medium",
            "actions": [
                "Drink water or electrolyte drinks",
                "Sit or lie down immediately",
                "Avoid sudden movements"
            ],
            "recovery": [
                "Increase fluid intake",
                "Eat balanced meals",
                "Ensure proper sleep",
                "Monitor blood pressure if symptoms continue"
            ]
        }

    return result

# -----------------------------
# RISK METER
# -----------------------------
def risk_meter(level):

    if level == "Low":
        st.success("🟢 Low Risk")

    elif level == "Medium":
        st.warning("🟡 Medium Risk")

    elif level == "High":
        st.error("🔴 High Risk")


# -----------------------------
# ANALYZE BUTTON
# -----------------------------
if st.button("Analyze"):

    if user_input:

        result = analyze_symptoms(user_input)

        st.markdown("## 🧠 AI Health Insight")

        st.markdown("### 🩺 Possible Condition")
        st.success(result["condition"])

        st.markdown("### ⚠️ Risk Level")
        risk_meter(result["risk"])

        st.markdown("### 🚑 Immediate Actions")

        for action in result["actions"]:
            st.write("✔️", action)

        st.markdown("### 🌿 Recovery Plan")

        for step in result["recovery"]:
            st.write("🔹", step)

        st.markdown("---")
        st.caption("⚠️ This is not medical advice. Please consult a healthcare professional.")

    # -----------------------------
    # REPORT ANALYSIS
    # -----------------------------
    

    if uploaded_file.type == "application/pdf":

        report_text = read_pdf(uploaded_file)

        st.markdown("## 📄 Medical Report Analysis")

        text = report_text.lower()

        problem = "No major abnormalities detected"
        risk = "Low"
        actions = []
        recovery = []

        if "high glucose" in text or "blood sugar" in text:
            problem = "Possible Diabetes or High Blood Sugar"
            risk = "Medium"

            actions = [
                "Reduce sugar intake immediately",
                "Drink plenty of water",
                "Monitor blood sugar levels"
            ]

            recovery = [
                "Follow a low sugar diet",
                "Exercise regularly",
                "Consult a doctor for medication"
            ]

        elif "low hemoglobin" in text or "anemia" in text:
            problem = "Possible Anemia (Low Hemoglobin)"
            risk = "Medium"

            actions = [
                "Increase iron rich foods",
                "Avoid excessive tea or coffee",
                "Consult doctor if weakness continues"
            ]

            recovery = [
                "Eat spinach, beetroot, dates",
                "Take iron supplements if prescribed",
                "Maintain balanced nutrition"
            ]

        elif "cholesterol" in text and "high" in text:
            problem = "High Cholesterol Levels"
            risk = "Medium"

            actions = [
                "Reduce oily and fried foods",
                "Increase physical activity",
                "Monitor cholesterol levels"
            ]

            recovery = [
                "Eat fiber rich foods",
                "Follow heart healthy diet",
                "Regular medical checkups"
            ]

        st.markdown("### 🩺 Detected Health Issue")
        st.success(problem)

        st.markdown("### ⚠️ Risk Level")
        risk_meter(risk)

        st.markdown("### 🚑 Immediate Actions")

        for action in actions:
            st.write("✔️", action)

        st.markdown("### 🌿 Recovery Plan")

        for step in recovery:
            st.write("🔹", step)