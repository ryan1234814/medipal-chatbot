import speech_recognition as sr
import pyttsx3

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except Exception:
        return "Sorry, I didn't catch that."

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
