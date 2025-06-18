import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import pyjokes
import subprocess
import time
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("I am Your Voice Assistant Sir. Please tell me how may I help you")        

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in').lower()
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print("Say that again please...")  
            return "None"

def username():
    speak("What should I call you?")
    uname = takeCommand()
    if uname == "none":
        uname = "User"
    speak(f"Welcome {uname}")
    speak("How can I help you?")

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
        server.sendmail(os.getenv('EMAIL_USER'), to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send this email.")

if __name__ == "__main__":
    wishMe()
    username()
    while True:
        query = takeCommand()
        if query == "none":
            continue
        
        if "how are you" in query:
            speak("I am fine. Thank you for asking. How are you doing?")
        elif "fine" in query or "good" in query:
            speak("It's good to know that you are doing well.")
        elif "who am i" in query:
            speak("If you can talk then surely you are a human.")
        elif "love" in query:
            speak("It is the 7th sense that destroys all the other senses.")
        elif "who are you" in query:
            speak("I am your virtual assistant, Sita.")
        elif "i love you" in query:
            speak("Ohhh! That's so kind of you. I love you too.")
        elif "will you be my girlfriend" in query or "will you be my valentine" in query:
            speak("I am a virtual assistant, so I do not have feelings like humans. How can I help you?")
        elif "what is your name" in query:
            speak("My friends call me rama.")
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
        elif "open google" in query:
            webbrowser.open("https://www.google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("https://www.stackoverflow.com")
        elif "open myntra" in query:
            speak("Here you go to Myntra. Happy Shopping!")
        elif "who is your owner father" in query:
            speak("His name is Nageswara rao!")   
        elif "who is your owner sister" in query:
            speak("Her name is Sri Devi!")
        elif "who is your owner mother" in query:
            speak("Her name is Kamala!") 
        elif "open amazon" in query:
            speak("Happy Shopping!")
            webbrowser.open("https://www.amazon.com")
        elif "open linkedin" in query:
            speak("Sriram Profile")
            webbrowser.open("https://www.linkedin.com/in/sri-rama-kanth-pendikatla-080105288/")
        elif "where is" in query:
            location = query.replace("where is", "").strip()
            speak(f"Locating {location}...")
            webbrowser.open(f"https://www.google.com/maps/search/{location}")
        elif "joke" in query:
            speak(pyjokes.get_joke())
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif "shutdown" in query:
            speak("Shutting down the system. Please close all applications.")
            time.sleep(5)
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            speak("Restarting the system.")
            os.system("shutdown /r /t 1")
        elif "open notepad" in query:
            os.system("notepad")
        elif 'open spotify' in query:
            npath = "C:\\Users\\srira\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe"
            os.startfile(npath)
        elif 'open outlook' in query:
            npath = "C:\\Users\\srira\\AppData\\Local\\Microsoft\\WindowsApps\\Microsoft.OutlookForWindows_8wekyb3d8bbwe\\olk.exe"
            os.startfile(npath)
        elif "email to sriram" in query:
            speak("What should I say?")
            content = takeCommand()
            if content != "none":
                sendEmail("sriramakanthpendikatla84@gmail.com", content)
        elif "exit" in query or "quit" in query:
            speak("Thank you for using me. Have a good day!")
            sys.exit()
        elif "bmi" in query:
            speak("Please tell me your height in centimeters:")
            height = takeCommand()
            speak("Please tell me your weight in kilograms:")
            weight = takeCommand()
            try:
                height = float(height) / 100
                weight = float(weight)
                bmi = weight / (height * height)
                speak(f"Your Body Mass Index is {bmi:.2f}")
            except ValueError:
                speak("Sorry, I couldn't understand the input. Please try again.")