# ============================================
# IMPORT LIBRARIES
# ============================================

import streamlit as st
import pandas as pd
import pickle

# ============================================
# LOAD TRAINED PIPELINE MODEL
# ============================================

model = pickle.load(
    open("best_pipeline.pkl", "rb")
)

# ============================================
# TITLE
# ============================================

st.title("Social Media Mental Health Predictor")

st.write(
    "Predict the overall impact of social media on mental health."
)

# ============================================
# USER INPUTS
# ============================================

age = st.number_input(
    "Enter Age",
    min_value=10,
    max_value=100,
    value=21
)

gender = st.selectbox(
    "Select Gender",
    ["Male", "Female"]
)

academic_level = st.selectbox(
    "Academic Level",
    [
        "High School",
        "Undergraduate",
        "Graduate"
    ]
)

avg_usage = st.slider(
    "Average Daily Usage Hours",
    0.0,
    15.0,
    5.0
)

platform = st.selectbox(
    "Most Used Platform",
    [
        "Facebook",
        "Instagram",
        "LinkedIn",
        "Snapchat",
        "Twitter",
        "YouTube",
        "TikTok"
    ]
)

academic_effect = st.selectbox(
    "Does Social Media Affect Academic Performance?",
    ["Yes", "No"]
)

sleep_hours = st.slider(
    "Sleep Hours Per Night",
    0.0,
    12.0,
    7.0
)

# ============================================
# MANUAL ENCODING
# ============================================

gender_map = {
    "Male": 1,
    "Female": 0
}

academic_map = {
    "High School": 0,
    "Graduate": 1,
    "Undergraduate": 2
}

platform_map = {
    "Facebook": 0,
    "Instagram": 1,
    "LinkedIn": 2,
    "Snapchat": 3,
    "Twitter": 4,
    "YouTube": 5,
    "TikTok": 6
}

effect_map = {
    "No": 0,
    "Yes": 1
}

# ============================================
# CREATE INPUT DATAFRAME
# ============================================

input_data = pd.DataFrame([{
    
    "Age": age,
    
    "Gender": gender_map[gender],
    
    "Academic_Level":
        academic_map[academic_level],
    
    "Avg_Daily_Usage_Hours":
        avg_usage,
    
    "Most_Used_Platform":
        platform_map[platform],
    
    "Affects_Academic_Performance":
        effect_map[academic_effect],
    
    "Sleep_Hours_Per_Night":
        sleep_hours
}])

# ============================================
# PREDICTION BUTTON
# ============================================

if st.button("Predict Impact"):
    
    prediction = model.predict(input_data)

    prediction = prediction[0]

    # ========================================
    # MANUAL LABEL DECODING
    # ========================================

    if prediction == 0:
        result = "Negative"

    elif prediction == 1:
        result = "Neutral"

    else:
        result = "Positive"

    # ========================================
    # DISPLAY RESULT
    # ========================================

    if result == "Positive":
    
        st.success(
            f"Predicted Overall Impact : {result}"
    )

    elif result == "Neutral":
    
        st.warning(
            f"Predicted Overall Impact : {result}"
    )

    else:
    
        st.error(
            f"Predicted Overall Impact : {result}"
    )