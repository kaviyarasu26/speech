import pyttsx3 
import datetime
import speech_recognition as sr
engin=pyttsx3.init('sapi5')
voice =engin.getProperty('voices')
engin.setProperty('voice',voice[0].id)




def speak(audio):
    engin.say(audio)
    engin.runAndWait()

def wish():
    currentTime = datetime.datetime.now()
    currentTime.hour  
    if currentTime.hour < 12:
        speak("Good Morning ,sir")
    elif 12 <= currentTime.hour < 18:
        speak("Good afternoon, sir")
    else:
        speak("Good evening, sir")


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("Sri,Listening....") 
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        query = r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please")


if __name__=="__main__":
    wish()
    takecommand()

