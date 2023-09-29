import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)


 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("i am jarvis made by smit. .")


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizing...")
        quary = r.recognize_google(audio, language='en-in')
        print(f"User said: {quary}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return quary

if __name__ == "__main__":
    wishme()
    while True:
        quary=takecommand().lower()

        if 'wikipedia' in quary:
            speak('searching wikipedia...')
            quary = quary.replace("wikipedia","")
            results = wikipedia.summary(quary, sentences=2)
            # print(results)
            speak(results)

        elif 'open youtube' in quary:
            webbrowser.open("youtube.com")

        elif 'open google' in quary:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in quary:
            webbrowser.open("stackoverflow.com")

        elif 'open chatgpt' in quary:
            webbrowser.open("ai.com")

        elif 'the time' in quary:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time  is {strtime}")

        # elif 'open code' in quary:
        #     codepath = "C:\Users\hp\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        #     os.startfile('codepath')


        

    