# CARE-AI Nova Copilot

CARE-AI Nova Copilot is a simple AI-powered healthcare assistant that helps users understand their symptoms and medical reports.

The system analyzes user-entered symptoms and uploaded medical reports to generate basic health insights, risk levels, and suggested actions.

⚠️ This project is for educational purposes only and does not replace professional medical advice.

---

## Features

- Symptom analysis based on user input
- Medical report (PDF) text extraction
- Detection of possible health conditions
- Risk level indication (Low / Medium / High)
- Immediate actions for the patient
- Suggested recovery plan

---

## Tech Stack

- Python  
- Streamlit  
- PDFPlumber  

---

## How It Works

1. The user enters symptoms in the text field.
2. The system analyzes the symptoms and predicts a possible health condition.
3. The application displays:
   - Possible condition
   - Risk level
   - Immediate actions
   - Recovery suggestions
4. Users can also upload a medical report (PDF) for basic report text extraction and analysis.

---

## Installation

Clone the repository:

git clone https://github.com/Hareesh169/care-ai-nova-copilot.git

Go to the project folder:

cd care-ai-nova-copilot

Install dependencies:

pip install -r requirements.txt

---

## Run the Application

Start the Streamlit application:

streamlit run app.py

Then open the browser at:

http://localhost:8501

---

## Example Usage

Enter symptoms such as:

fever headache fatigue

The system will generate:

- Possible health condition  
- Risk severity level  
- Immediate actions to take  
- Recovery guidance  

Users can also upload a medical report PDF for analysis.

---

## Project Structure

care-ai-nova-copilot  
│  
├── app.py  
├── requirements.txt  
└── README.md  

---

## Disclaimer

This project provides general health insights based on simple symptom matching and medical report keywords.  
It is not intended for real medical diagnosis. Always consult a qualified healthcare professional for medical advice.
