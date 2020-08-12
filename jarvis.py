import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
print("Hello Shivam goyal!\nIntilializing jarvis")

sir="Shivam Goyal..."

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


#speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

speak(" Initializing your jarvis....")


def wishme():
    hour = int(datetime.datetime.now().hour)    
    
    if hour>=0 and hour<12:
        speak("Good morning.."+sir)
    
    elif hour>=12 and hour<18:
        speak("Good afternoon..."+sir)

    else:
        speak("Good evening..." + sir)

wishme()   

speak("I am your jarvis! How may i help you?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)

    try : 
        print("Recognizing..")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print("Say that again please")
        query = None
    return query

query = takecommand()


if 'wikipedia' in query.lower():
    speak("Searching wikipedia..")
    query = query.replace("wikipedia","")
    result = wikipedia.summary(query, sentences = 5)
    print(result)
    speak(result)

elif 'open youtube' in query.lower():
    url = "youtube.com"
    #webbrowser.open("youtube.com")
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():
    url = "google.com"
    #webbrowser.open("youtube.com")
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query.lower():
    songs_dir = "C:\\Users\\hp\\Music"
    songs = os.listdir(songs_dir)
    print(songs)
    playsong = os.startfile(os.path.join(songs_dir, songs[1]))
    print(playsong)

    
elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{sir} the time is {strTime}")

elif 'open code' in query.lower():
    codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)
    