import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime #For date and Time
import wikipedia #pip install wikipedia
import webbrowser #Search in web browser
import os 
import smtplib

 

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

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sender_email_@gmail.com','password of sender_email_@gmail.com')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if "__init__" == "__main__":
    speak("Hello. I am Jarvis Nice to meet you..")
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:  # Wikipedia Search
            speak('SEARCHING WIKIPEDIA...')
            query = query.replace("wikipedia", "")
            # speak 2 sentences from results
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)  # speak 2 sentences from results

        elif 'good morning' or 'good evening' or 'good afternoon' or  'good night' in query:
            wishMe()

        elif 'open youtube' in query:  # open using Browser
            webbrowser.open("youtube.com")

        elif 'open google' in query:  # open using Browser
            webbrowser.open("google.com")

        elif 'open facebook' in query:  # open using Browser
            webbrowser.open("facebook.com")

        elif 'open flipkart' in query:  # open using Browser
            webbrowser.open("flipkart.com")

        elif 'open amazon' in query:  # open using Browser
            webbrowser.open("amazon.com")

        elif 'play music' in query:
            music_dir = 'C:\\My File LOK\\Musics_Lok'  # Path// Location of folder
            songs = os.listdir(music_dir)
            print(songs)
            # 0 for play 1st song
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:  # The Time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir The time is {strTime}')

        elif 'open code' in query:
            codePath = "C:\\Users\\lmaha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"#path or target location
            os.startfile(codePath)

        elif 'emil to me' in query:
            try:
               speak("What should i say?")
               content =takeCommand()
               to = "Enter_Your_Email_ID_@gmail.com" # Mail Id 
               sendEmail(to, content)
               speak('Email Has Been Sent!')
            except Exception as e :
                print(e)
                speak('Sorry my friend i can not send email now... Please Try Again...')
            
        elif 'Sleep' in query:
            break



