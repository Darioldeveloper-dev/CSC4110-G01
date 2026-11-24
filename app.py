import joblib
import pandas as pd
import streamlit as st
from pathlib import Path

# The saved pipeline sits in models/ next to the app folder
MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "G01_model.joblib"
THRESHOLD = 0.30   # chosen in Task 5: a missed deserving student is worse than one extra interview

st.set_page_config(page_title="Scholarship nomination helper", page_icon=":mortar_board:")
st.title("Scholarship nomination helper")
st.write("**CSC 4110 Machine Learning, Group G01**")
st.write("Members: Dariol Temko, Raphael Wanyama, Elisha Eddie, Abdul Razak, Emmanuel Rotich")
st.write("Dataset: Student Performance Factors (about 6,600 student records)")
st.write("Enter a student's details to see how likely they are to score 70 or more.")


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


model = load_model()

hours = st.slider("Hours studied per week", 1, 44, 20)
attendance = st.slider("Attendance (%)", 60, 100, 80)
previous = st.slider("Previous exam score", 50, 100, 75)
motivation = st.selectbox("Motivation level", ["Low", "Medium", "High"], index=1)
parental = st.selectbox("Parental involvement", ["Low", "Medium", "High"], index=1)
access = st.selectbox("Access to resources", ["Low", "Medium", "High"], index=1)

if st.button("Predict"):
    row = pd.DataFrame([{
        "Hours_Studied": hours, "Attendance": attendance, "Previous_Scores": previous,
        "Motivation_Level": motivation, "Parental_Involvement": parental, "Access_to_Resources": access}])
    prob = float(model.predict_proba(row)[0, 1])
    st.metric("Probability of scoring 70 or more", f"{prob:.1%}")
    if prob >= THRESHOLD:
        st.success("Suggested: invite this student for a scholarship interview.")
    else:
        st.info("Not suggested for interview on these details alone. Teachers should still use their own judgement.")
    st.caption("This tool supports a decision, it does not make one. It must never be used to lower "
               "expectations for any student.")
