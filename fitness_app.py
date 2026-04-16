import streamlit as st
import pandas as pd
import joblib

#load model

@st.cache_resource
def load_model():
    return joblib.load("fitness.pkl")   

app_model=load_model()

#sidebar
st.sidebar.title("Navigation")
page=st.sidebar.selectbox("Go to",["Prediction","About"])

#prediction page
if page=="Prediction":
    st.write("Calories Burning Prediction APP 🔥")   
    st.write("Enter your fitness detail below:")

    #input
    gender=st.selectbox('Gender',["Male","Female"])
    age=st.number_input("Age",1,100,25)
    height=st.number_input("Height (cm)",140,250,175)
    weight=st.number_input("Weight (kg)",40,200,65)
    duration=st.number_input("Training Duration in minutes",20,180,60)
    heart_rate=st.number_input("Heart Rate",60,200,100)
    body_temp=st.number_input("Body Temperature in Celsius",35.0,45.0,37.0)

    user_inputs={
        'gender': 0 if gender=="Male" else 1,
        'age':age,
        'height':height,
        'weight':weight,
        'duration':duration,
        'heart_rate':heart_rate,
        'body_temp':body_temp
    }

    if st.button('Predict'):
        model_predict=app_model.predict(pd.DataFrame(user_inputs,index=[0]))
        st.markdown(f"the Burnt Calories is :{model_predict[0]:,.2f}")
   
