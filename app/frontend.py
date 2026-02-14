import streamlit as st
import requests
from src.exception import CustomException
import sys

st.title('Student Performance Evaluator')

with st.form('Student Data: '):
    gender = st.selectbox(
    'Gender: ', ['male', 'female']
    )
    race_ethnicity = st.selectbox(
        'Race/Ethnicity', ['group A', 'group B', 'group C', 'group D', 'group E']
    )
    parental_level_of_education = st.selectbox(
        'Parental level of education', ["bachelor's degree", 'some college', "master's degree", "associate's degree", 'high school', 'some high school']
    )
    lunch = st.selectbox(
        'Lunch', ['standard', 'free/reduced']
    )
    test_preparation_course = st.selectbox(
        'Test preparation course', ['none', 'completed']
    )
    reading_score = st.number_input(
        'Reading score', min_value = 1, max_value = 100, value = 50
    )
    writing_score = st.number_input(
        'Writing score', min_value = 1, max_value = 100, value = 50
    )
    submit = st.form_submit_button('Submit')

if submit:
    payload = {
        'gender': gender,
        'race_ethnicity': race_ethnicity,
        'parental_level_of_education': parental_level_of_education,
        'lunch': lunch,
        'test_preparation_course': test_preparation_course,
        'reading_score': reading_score,
        'writing_score': writing_score
    }

    try:
        with st.spinner('Pinging the backend'):
            response = requests.post('http://127.0.0.1:8000/predict', json = payload)

        if response.status_code == 200:
            prediction = response.json()
            value = response.json().get('predicted', [0])[0]
            st.success(f"The predicted math score is: {round(value, 2)}")
            st.divider()
            st.balloons() # Added a little flair for the win
            st.metric(label="Predicted Math Score", value=f"{round(value, 2)}%")
            
            # Contextual feedback
            if round(value, 2) > 80:
                st.success("High performance predicted! 🚀")
            elif round(value, 2) > 50:
                st.info("Average performance predicted.")
            else:
                st.warning("Needs improvement.")
        else:
            st.error(f'Error: {response.status_code}. Check Backend logs')

    except Exception as e:
        raise CustomException(e, sys)