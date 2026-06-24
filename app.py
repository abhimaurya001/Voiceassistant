import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except Exception:
        speak("Sorry, I could not understand.")
        return ""

speak("Voice Assistant Started")

while True:
    command = listen()

    if "open notepad" in command:
        os.system("notepad")

    elif "open calculator" in command:
        os.system("calc")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")

    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")

    elif any(word in command for word in ["exit", "stop", "goodbye", "good bye"]):
     speak("Goodbye")
     break