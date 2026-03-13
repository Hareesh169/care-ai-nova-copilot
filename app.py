import streamlit as st
import pdfplumber

st.set_page_config(page_title="CARE-AI Nova Copilot", page_icon="🧠")

st.title("CARE-AI Nova Copilot")
st.subheader("AI Health Assistant Prototype")

st.write("""
CARE-AI Nova Copilot is designed to help users understand their symptoms and
interpret medical reports using AI-assisted analysis.

Enter your symptoms or upload a medical report to receive simplified health insights.
""")

# ---------------- USER INPUT ----------------
user_input = st.text_area("Describe your symptoms")

uploaded_file = st.file_uploader(
    "Upload medical report (PDF or Image)",
    type=["pdf","png","jpg","jpeg"]
)

# ---------------- SYMPTOM ANALYSIS ----------------
def analyze_symptoms(symptoms):

    symptoms = symptoms.lower()

    detected_symptoms = []

    if "fever" in symptoms:
        detected_symptoms.append("Fever")

    if "headache" in symptoms:
        detected_symptoms.append("Headache")

    if "cough" in symptoms:
        detected_symptoms.append("Cough")

    if "fatigue" in symptoms:
        detected_symptoms.append("Fatigue")

    if "chest pain" in symptoms:
        detected_symptoms.append("Chest Pain")

    if "stomach pain" in symptoms:
        detected_symptoms.append("Stomach Pain")

    # Determine possible condition
    if "fever" in symptoms and "headache" in symptoms:
        condition = "Possible viral infection or flu."

    elif "cough" in symptoms:
        condition = "Possible respiratory infection."

    elif "chest pain" in symptoms:
        condition = "Possible cardiovascular issue."

    elif "stomach pain" in symptoms:
        condition = "Possible digestive issue such as gastritis."

    elif "fatigue" in symptoms:
        condition = "Possible dehydration, anemia, or infection."

    else:
        condition = "Symptoms unclear. Further medical evaluation recommended."

    return detected_symptoms, condition


# ---------------- PDF REPORT READER ----------------
def read_pdf(file):

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()

    return text


# ---------------- ANALYZE BUTTON ----------------
if st.button("Analyze Health Data"):

    # SYMPTOM ANALYSIS
    if user_input:

        detected_symptoms, condition = analyze_symptoms(user_input)

        st.subheader("Detected Symptoms")

        if detected_symptoms:
            for symptom in detected_symptoms:
                st.write("•", symptom)
        else:
            st.write("No specific symptoms detected.")

        st.subheader("Possible Health Insight")

        st.success(condition)

        st.subheader("Recommended Actions")

        st.write("""
• Monitor symptoms for changes  
• Stay hydrated and rest  
• Maintain balanced nutrition  
• Seek professional medical advice if symptoms persist
""")

        st.warning("This system provides informational insights only and does not replace professional medical diagnosis.")

    # REPORT ANALYSIS
    if uploaded_file:

        if uploaded_file.type == "application/pdf":

            report_text = read_pdf(uploaded_file)

            st.subheader("Extracted Medical Report Data")

            st.write(report_text[:800])

            st.subheader("Basic Report Interpretation")

            st.write("""
The uploaded report has been successfully processed.  
CARE-AI Nova Copilot extracted textual information from the document.

In a full implementation, advanced AI models would analyze medical metrics,
identify abnormal values, and generate clinical insights.
""")

        else:

            st.info("Medical report uploaded successfully. Image-based analysis would be performed in the full AI version.")