import pyttsx3
import speech_recognition as sr
import datetime

 

#From pyttsx3
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #With this command, speech will not be audible to us.


#Take Command Function
def takeCommand():    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        print(e)    
        print("Say that again please...")
        return "None" #None string will be returned
    return query

#wish to me
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Morning")
    else:
        speak("Good Night")
    speak("I am Jarvis Sir. Please tell me how may I Help you.")

if "__init__" == "__main__":
    speak("Hello. I am Jarvis Nice to meet you..")
    query = takeCommand().lower
    print(query)
    if 'good morning' or 'good night' or 'good evening' or 'good afternoon' in query:
        wishMe()
