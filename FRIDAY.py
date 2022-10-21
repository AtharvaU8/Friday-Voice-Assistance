import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
import subprocess as sp
import requests
from email.message import EmailMessage

paths = {
    'chrome': "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    'code': "C:\\Users\\athar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    'notepad': "%windir%\\system32\\notepad.exe",
    'discord': "C:\\Users\\athar\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Users\\athar\\OneDrive\\Calculator\\calculator.exe"
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good morning sir")

    elif hour>= 12 and hour<18:
        speak("Good afternoon sir")
    
    else:
        speak("Good evening sir")

    speak("how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening....")
        r.pause_threshold = 1 
        r.energy_threshold = 4000  
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query or 'quit' in query:
            speak("Okay sir, I am working on it.")
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
        print(f"User: {query}\n")

    except Exception as e:
        print("Please say again....")
        return 'None'
    return query

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
    
def open_notepad():
    os.startfile(paths['notepad'])

def open_discord():
    os.startfile(paths['discord'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    os.startfile(paths['calculator'])

def open_code():
    os.startfile(paths['code'])

def open_chrome():
    os.startfile(paths['chrome'])

def open_explorer():
    sp.call("explorer C:\\temp\\yourpath", shell=True)



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            query = query.replace('wikipeadia','')
            results = wikipedia.summary(query, sentences = 2)
            speak('According to wikipeadia')
            speak(results)      

        elif 'google' in query:
            webbrowser.open('https://google.com')

        elif 'youtube' in query:
            webbrowser.open('https://youtube.com')
        
        elif 'stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com')
        
        elif 'instagram' in query:
            webbrowser.open('https://instagram.com')
        
        elif 'deadtoons' in query:
            webbrowser.open('https://deadtoons.net')
        
        elif 'w3school' in query:
            webbrowser.open('https://www.w3schools.com')

        elif 'github' in query or 'git hub' in query:
            webbrowser.open('https://github.com/')

        elif 'the time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            now = datetime.datetime.now()
            print(time,'\n',now.strftime("%d-%B-%Y"))
            speak(f'Sir, the time is {time}')

        elif 'play music' in query or 'play song' in query:
            foldermusic = random.randint(1,4)
            if foldermusic == 1:
                music = random.randint(1,27)
                music_dir=f'C:\\Users\\athar\\Music\\Hindi Songs'
                song = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,song[music]))
            elif foldermusic == 2:
                music = random.randint(1,11)
                music_dir=f'C:\\Users\\athar\\Music\\MJ Songs'
                song = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,song[music]))
            elif foldermusic == 3:
                music = random.randint(1,38)
                music_dir=f'C:\\Users\\athar\\Music\\Other Songs'
                song = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,song[music]))
            elif foldermusic == 4:
                music = random.randint(1,11)
                music_dir=f'C:\\Users\\athar\\Music\\Youtubers Song'
                song = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,song[music]))
        
        elif 'camera' in query:
            open_camera()
        
        elif 'vs code' in query or 'code' in query:
            open_code()

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)

        elif 'discord' in query:
            open_discord()
        
        elif 'notepad' in query:
            open_notepad()

        elif 'calculator' in query:
            open_calculator()
        
        elif 'command prompt' in query or 'open cmd' in query:
            open_cmd()
         
        elif 'file explorer' in query:
            open_explorer()
        
        elif 'hi' in query or 'hey' in query :
            speak("Hi sir")

        elif 'hello' in query:
            speak("Hello sir")
        
        elif 'what are you doing' in query:
            speak('Hatching a plan to help you out where I can.')
        
        elif 'who made you' in query or 'who invented you' in query or 'who created you' in query or 'who is your coder' in query or 'who coded you' in query or 'who programmed you' in query or 'who is your programmer' in query or 'who developed you' in query or 'who is your developer' in query:
            speak("I was conceived by Atharva")

        elif 'hello' in query:
            speak('hello sir')
        
        elif 'how are you' in query:
            speak('My AI mood levels are always positive.')

        elif 'exit' in query or 'quit' in query or 'stop' in query or 'close' in query :
            exit()

        else:
            speak("I amm sorry, but I can't help with that.")