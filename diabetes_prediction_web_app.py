import numpy as np 
import pickle 
import streamlit as st 

# Load the saved model
loaded_model = pickle.load(open(r"C:\Users\DELL\Desktop\Newfolder\coding\python\ml_youtube\code\part5\trained_model.sav", 'rb'))
scaler_model = pickle.load(open(r"C:\Users\DELL\Desktop\Newfolder\coding\python\ml_youtube\code\part5\scaler.sav", 'rb'))
# Prediction function
def diabetes(input_data):
    input_data = np.asarray(input_data).reshape(1, -1)
    scaler_model.fit(input_data)
    input_data = scaler_model.transform(input_data)
    output = loaded_model.predict(input_data)
    result = 'diabetic' if output[0] == 1 else 'not diabetic'
    return output, result

def main():
    # giving a title
    st.title('Diabetes Prediction Web App')

    # Number input fields for all required parameters
    Pregnancies = st.number_input('Number of pregnancies', min_value=0, max_value=20, step=1)
    Glucose = st.number_input('Glucose level', min_value=0.0, max_value=300.0)
    BloodPressure = st.number_input('Blood Pressure', min_value=0.0, max_value=200.0)
    SkinThickness = st.number_input('Skin Thickness', min_value=0.0, max_value=100.0)
    Insulin = st.number_input('Insulin', min_value=0.0, max_value=1000.0)
    BMI = st.number_input('BMI', min_value=0.0, max_value=70.0)
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, format="%.3f")
    Age = st.number_input('Age', min_value=1, max_value=120, step=1)
# code for prediction
    diagnosis = ""
    # creating a button for prediction
    if st.button('Diabetes Test Result'):
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        _, diagnosis = diabetes(input_data)
        st.success(f"Prediction: {diagnosis}")

if __name__ == '__main__':
    main()
