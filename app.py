
import streamlit as st 
import pickle 
import os
from streamlit_option_menu import option_menu
from streamlit_option_menu import option_menu
import streamlit as st

# Page configuration
st.set_page_config(page_title="Multiple Disease Prediction", layout="wide", page_icon="👨‍⚕️")



# Get working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load all models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes.pkl','rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart.pkl','rb'))
kidney_disease_model = pickle.load(open(f'{working_dir}/saved_models/kidney.pkl','rb'))
liver_disease_model = pickle.load(open(f'{working_dir}/saved_models/liver.pkl','rb'))

# Initialize feature variables
NewBMI_Overweight=0
NewBMI_Underweight=0
NewBMI_Obesity_1=0
NewBMI_Obesity_2=0 
NewBMI_Obesity_3=0
NewInsulinScore_Normal=0 
NewGlucose_Low=0
NewGlucose_Normal=0 
NewGlucose_Overweight=0
NewGlucose_Secret=0

# Sidebar navigation
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction", 
                ['Diabetes Prediction',
                 'Heart Disease Prediction',
                 'Kidney Disease Prediction',
                 'Liver Disease Prediction'],
                 menu_icon='hospital-fill',
                 icons=['activity','heart','person','droplet-half'],
                 default_index=0)

# ================= Diabetes Prediction ====================
# Correct loading of scaler and model
# Correct loading of scaler and model


if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction Using Machine Learning")
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
        Insulin = st.text_input("Insulin Value")
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age = st.text_input("Age")

    diabetes_result = ""

    if st.button("Diabetes Test Result"):
        input_fields = [Pregnancies, Glucose, BloodPressure, SkinThickness,
                        Insulin, BMI, DiabetesPedigreeFunction, Age]

        if all(field.strip() != "" for field in input_fields):
            try:
                # Convert inputs to float
                Pregnancies = float(Pregnancies)
                Glucose = float(Glucose)
                BloodPressure = float(BloodPressure)
                SkinThickness = float(SkinThickness)
                Insulin = float(Insulin)
                BMI = float(BMI)
                DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
                Age = float(Age)

                # Input for model — only 8 features
                user_input = [[
                    Pregnancies, Glucose, BloodPressure, SkinThickness,
                    Insulin, BMI, DiabetesPedigreeFunction, Age
                ]]

                # Predict using model (no scaler)
                prediction = diabetes_model.predict(user_input)

                if prediction[0] == 1:
                    diabetes_result = "✅ The person **has diabetes**."
                else:
                    diabetes_result = "✅ The person **does not have diabetes**."

            except Exception as e:
                diabetes_result = f"❌ Error in input conversion: {e}"
        else:
            diabetes_result = "❌ Please fill all fields with valid numbers."

    st.success(diabetes_result)



# ================= Heart Disease Prediction ====================
if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction Using Machine Learning")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex (1 = male, 0 = female)")
    with col3:
        cp = st.text_input("Chest Pain Type (0-3)")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholesterol")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)")
    with col1:
        restecg = st.text_input("Resting ECG results")
    with col2:
        thalach = st.text_input("Max Heart Rate Achieved")
    with col3:
        exang = st.text_input("Exercise Induced Angina (1 = yes; 0 = no)")
    with col1:
        oldpeak = st.text_input("ST depression induced by exercise")
    with col2:
        slope = st.text_input("Slope of the peak exercise ST segment")
    with col3:
        ca = st.text_input("Major vessels colored by fluoroscopy")
    with col1:
        thal = st.text_input("Thal (0 = normal; 1 = fixed defect; 2 = reversable defect)")

    heart_disease_result = ""

    if st.button("Heart Disease Test Result"):
        input_fields = [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                        exang, oldpeak, slope, ca, thal]
        
        if all(field.strip() != "" for field in input_fields):
            try:
                user_input = [float(x) for x in input_fields]
                st.write("Debug Input to Model:", user_input)  # Helpful for debugging
                prediction = heart_disease_model.predict([user_input])
                if prediction[0] == 1:
                    heart_disease_result = "The person has heart disease."
                else:
                    heart_disease_result = "The person does not have heart disease."
            except Exception as e:
                heart_disease_result = f"❌ Error in input conversion: {e}"
        else:
            heart_disease_result = "❌ Please fill all fields with valid numbers."

    st.success(heart_disease_result)

# ================= Kidney Disease Prediction ====================
if selected == 'Kidney Disease Prediction':
    st.title("Kidney Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        age = st.text_input('Age')
    with col2:
        blood_pressure = st.text_input('Blood Pressure')
    with col3:
        specific_gravity = st.text_input('Specific Gravity')
    with col4:
        albumin = st.text_input('Albumin')
    with col5:
        sugar = st.text_input('Sugar')
    with col1:
        red_blood_cells = st.text_input('Red Blood Cell')
    with col2:
        pus_cell = st.text_input('Pus Cell')
    with col3:
        pus_cell_clumps = st.text_input('Pus Cell Clumps')
    with col4:
        bacteria = st.text_input('Bacteria')
    with col5:
        blood_glucose_random = st.text_input('Blood Glucose Random')
    with col1:
        blood_urea = st.text_input('Blood Urea')
    with col2:
        serum_creatinine = st.text_input('Serum Creatinine')
    with col3:
        sodium = st.text_input('Sodium')
    with col4:
        potassium = st.text_input('Potassium')
    with col5:
        haemoglobin = st.text_input('Haemoglobin')
    with col1:
        packed_cell_volume = st.text_input('Packed Cell Volume')
    with col2:
        white_blood_cell_count = st.text_input('White Blood Cell Count')
    with col3:
        red_blood_cell_count = st.text_input('Red Blood Cell Count')
    with col4:
        hypertension = st.text_input('Hypertension')
    with col5:
        diabetes_mellitus = st.text_input('Diabetes Mellitus')
    with col1:
        coronary_artery_disease = st.text_input('Coronary Artery Disease')
    with col2:
        appetite = st.text_input('Appetite')
    with col3:
        peda_edema = st.text_input('Pedal Edema')
    with col4:
        aanemia = st.text_input('Anaemia')

    kindey_diagnosis = ""
    if st.button("Kidney's Test Result"):
        user_input = [age, blood_pressure, specific_gravity, albumin, sugar,
                      red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
                      blood_glucose_random, blood_urea, serum_creatinine, sodium,
                      potassium, haemoglobin, packed_cell_volume,
                      white_blood_cell_count, red_blood_cell_count, hypertension,
                      diabetes_mellitus, coronary_artery_disease, appetite,
                      peda_edema, aanemia]
        user_input = [float(x) for x in user_input]
        prediction = kidney_disease_model.predict([user_input])
        if prediction[0] == 1:
            kindey_diagnosis = "The person has Kidney disease."
        else:
            kindey_diagnosis = "The person does not have Kidney disease."
    st.success(kindey_diagnosis)

# ================= Liver Disease Prediction ====================
if selected == 'Liver Disease Prediction':
    st.title("Liver Disease Prediction using Machine Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input("Age")
    with col2:
        Gender = st.selectbox("Gender", options=["Male", "Female"])
    with col3:
        Total_Bilirubin = st.text_input("Total Bilirubin")

    with col1:
        Direct_Bilirubin = st.text_input("Direct Bilirubin")
    with col2:
        Alkaline_Phosphotase = st.text_input("Alkaline Phosphotase")
    with col3:
        Alamine_Aminotransferase = st.text_input("Alamine Aminotransferase")

    with col1:
        Aspartate_Aminotransferase = st.text_input("Aspartate Aminotransferase")
    with col2:
        Total_Proteins = st.text_input("Total Proteins")
    with col3:
        Albumin = st.text_input("Albumin")

    with col1:
        Albumin_and_Globulin_Ratio = st.text_input("Albumin and Globulin Ratio")

    liver_diagnosis = ""
    if st.button("Liver Disease Test Result"):
        Gender_val = 1 if Gender == "Male" else 0
        user_input = [Age, Gender_val, Total_Bilirubin, Direct_Bilirubin,
                      Alkaline_Phosphotase, Alamine_Aminotransferase,
                      Aspartate_Aminotransferase, Total_Proteins, Albumin,
                      Albumin_and_Globulin_Ratio]
        user_input = [float(x) for x in user_input]
        prediction = liver_disease_model.predict([user_input])
        if prediction[0] == 1:
            liver_diagnosis = "The person has Liver disease."
        else:
            liver_diagnosis = "The person does not have Liver disease."
    st.success(liver_diagnosis)
# ================= Additional Tools ====================
st.markdown("---")
st.markdown("### 🛠️ More Tools")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <a href="http://127.0.0.1:8000" target="_blank">
            <button style="background-color:#4CAF50; color:white; padding:10px 20px; border:none; border-radius:5px; font-size:16px;">
                💬 Medical Chatbot
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <a href="http://127.0.0.1:5000" target="_blank">
            <button style="background-color:#2196F3; color:white; padding:10px 20px; border:none; border-radius:5px; font-size:16px;">
                🧬 Minor Disease Predictor
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )
