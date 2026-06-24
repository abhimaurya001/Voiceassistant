import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from datetime import datetime

# Voice Engine
engine = pyttsx3.init()

def speak(text):
    print("Shadow:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except:
        return ""

# Welcome Message
speak("Hello, I am Shadow. How can I help you?")

while True:
    command = listen()

    # Wake Word
    if "shadow" not in command:
        continue

    # Remove wake word
    command = command.replace("shadow", "").strip()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")
        
    elif "open" in command:
       app_name = command.replace("open", "").strip()
       speak(f"Opening {app_name}")
       os.system(f"start {app_name}")

    elif "hello" in command:
        speak("Hello Abhishek, nice to meet you.")

    elif "goodbye" in command or "good bye" in command or "exit" in command or "stop" in command:
        speak("Goodbye. Shutting down.")
        break

    else:
        speak("Sorry, I did not understand that command.")