
import streamlit as st
from db import get_medicine_info
from chatbot import get_response


import speech_recognition as sr
from speech_recognition import WaitTimeoutError

from lab import process_lab_report

st.title("MediPal – Health & Medicine Assistant")


# --- Multilingual Voice Chat for Health Questions ---
st.header("🔄 Voice Chat: Ask General Health Questions")
voice_lang = st.selectbox("Choose voice chat language", ["English", "Hindi", "Malayalam"])
lang_code = {"English": "en-IN", "Hindi": "hi-IN", "Malayalam": "ml-IN"}[voice_lang]
if st.button("Start Voice Chat"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info(f"Listening in {voice_lang}... (please start speaking within 10 seconds)")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=7)
            user_voice_text = recognizer.recognize_google(audio, language=lang_code)
            st.write(f"Recognized: {user_voice_text}")
            answer = get_response(user_voice_text)
            st.write(answer)
        except WaitTimeoutError:
            st.warning("Listening timed out. Please try again and start speaking promptly.")
        except Exception as e:
            st.error(f"Speech recognition error: {e}")


# --- Medicine Info Lookup ---
st.header("Check Medicine Safety and Usage")
medicine_name = st.text_input("Enter the medicine name:")
if st.button("Check Medicine Info") and medicine_name:
    info = get_medicine_info(medicine_name)
    st.write(info)


# --- General Health Q&A ---
st.header("Ask General Health Questions")
user_question = st.text_input("Type your health question:")
if st.button("Ask Gemini") and user_question:
    answer = get_response(user_question)
    st.write(answer)

# --- AI Diet Planner ---
st.header("🥗 AI Diet Planner")
diet_condition = st.text_input("Enter your medical condition (e.g., diabetes, hypertension):")
if st.button("Get Diet Plan") and diet_condition:
    diet_prompt = f"Suggest a personalized diet plan for a patient with {diet_condition}."
    diet_plan = get_response(diet_prompt)
    st.write(diet_plan)

# --- Fitness Tracker Integration ---
st.header("🏃 Fitness Tracker Integration")
fitness_condition = st.text_input("Enter your health goal or condition (e.g., diabetes, hypertension, weight loss):")
if st.button("Suggest Exercises") and fitness_condition:
    fitness_prompt = f"Suggest safe and effective exercises for someone with {fitness_condition}."
    fitness_plan = get_response(fitness_prompt)
    st.write(fitness_plan)
#---Lab Report Summarizer--
st.header("Lab Report Summarizer")
lab_file=st.file_uploader("Please upload your report file",type=["pdf","jpg","jpeg","png"])
if lab_file is not None:
    with st.spinner("Processing lab report"):
        summary=process_lab_report(lab_file)
    st.write("Summary");
    st.write(summary)    