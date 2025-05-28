import numpy as np
import pickle
import streamlit 
#load the saved model 
loaded_model = pickle.load(open(r"C:\Users\DELL\Desktop\Newfolder\coding\python\ml_youtube\code\part5\trained_model.sav",'rb'))
input = (5,166,72,19,175,25.8,0.587,51)
input = np.asarray(input).reshape(1,-1)
output  = loaded_model.predict(input)
result  = 'diabetic' if output[0] == 1 else 'not diabetic'
print(output,result )