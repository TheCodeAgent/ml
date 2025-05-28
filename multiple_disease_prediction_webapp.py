import pickle
import streamlit as st
from streamlit_option_menu import option_menu
diabetes_model = pickle.load(open("trained_model.sav", 'rb'))
heart_model = pickle.load(open("heart.sav", 'rb'))


# st.title('multiple  prediction using ml')
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction','Heart Disease Prediction'],
                            icons = ['activity','heart-pulse'],
                           default_index =0)

# 
if (selected =='Diabetes Prediction'):
    
    #page title('Diabetes prediction using ml')
    st.title('Diabetes prediction using ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input('Number of pregnancies', min_value=0, max_value=20, step=1)
    with col2:
        Glucose = st.number_input('Glucose level', min_value=0.0, max_value=300.0)
    with col3:
        BloodPressure = st.number_input('Blood Pressure', min_value=0.0, max_value=200.0)
    with col1:
        SkinThickness = st.number_input('Skin Thickness', min_value=0.0, max_value=100.0)
    with col2:
        Insulin = st.number_input('Insulin', min_value=0.0, max_value=1000.0)
    with col3:
        BMI = st.number_input('BMI', min_value=0.0, max_value=70.0)
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, format="%.3f")
    with col2: 
        Age = st.number_input('Age', min_value=1, max_value=120, step=1)

# code for prediction
    diagnosis = ""
    # creating a button for prediction
    if st.button('Diabetes Test Result'):
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        dia = diabetes_model.predict([input_data])
        diagnosis = 'diabetic' if dia[0] == 1 else 'not diabetic'
    st.success(f"Prediction: {diagnosis}")

if (selected =='Heart Disease Prediction'):
    
    #page title('Diabetes prediction using ml')
    st.title('Heart Disease prediction using ml')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
#code for prediction
    heart_diagnosis = ''
    # creating prediciton button 
    if st.button('Heart Disease Test Result'):
        prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if(prediction[0]==1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
            
    st.success(heart_diagnosis)
        
    
