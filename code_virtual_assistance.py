import pyttsx3

#From pyttsx3
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #Shows details of current voice
# print(voices[0].id)#TTS_MS_EN-US_DAVID_11.0
# print(voices[1].id) #TTS_MS_EN-US_ZIRA_11.0
engine.setProperty('voice', voices[0].id)

#speak function
def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #With this command, speech will not be audible to us.

if "__init__" == "__main__":
    speak("Hello. I am Jarvis Nice to meet you..")
