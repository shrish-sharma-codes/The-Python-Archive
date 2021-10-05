import datetime
import os
import random
import webbrowser

import pyttsx3  # for audio
import speech_recognition as sr  # for speech input
import wikipedia

engine = pyttsx3.init('sapi5')  # api to take voice
voices = engine.getProperty('voices')
# print(voices[1].id) #0 for male voice and 1 for female voice
engine.setProperty('voices', voices[0].id)


def speak(audio):  # to speak
    engine.say(audio)
    engine.runAndWait()


def wishMe():  # to wish
    hour = int(datetime.datetime.now().hour)  # to get current time
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Bunex , your virtual assistant . Please tell me how may I help you.")


def takeCommand():  # It takes microphone input from the user and returns string
    r = sr.Recognizer()  # will help us to recognize voice
    with sr.Microphone()as source:  # source microphone
        print("Listening...")
        r.pause_threshold = 0.5 # pause seconds like how much time asst will wait after a pause
        audio = r.listen(source)
    try:  # we use try when we think there could be any errror
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said:  {query}\n")  # we are using f str here .
    except Exception as e:
        speak("Sorry. Please say that again....")
        print("Sorry. Please say that again....")
        return "None"
    return query



if __name__ == "__main__":
   wishMe()
   while True: #to run continously
   #if 1: #to run once
       query = takeCommand().lower()

   # logic for executing tasks based onn queries
       if 'wikipedia' in query: #wikipedia
            speak("Searching ....")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1) #for 1 sentence
            speak("Wikipedia says")
            print(results)
            speak(results)
            
       elif 'open youtube' in query:
            webbrowser.open("youtube.com")

       elif 'open google' in query:
            webbrowser.open("google.com") 

       elif 'play music' in query:
             music_dir = 'address of music dir'
             songs = os.listed(music_dir)
             print(songs)
              # random gives random numbers
             os.startfile(os.path.join(music_dir,songs[random.randint(0,100)])) 

       elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}") 

    #    elif 'open my documents'in query:
    #         documents = "C:\\Users\\vidny\\Documents" #convert single slashes in double 
    #         os.startfile(documents)  

       elif 'open code' in query:
           vscPath = "C:\\Users\\vidny\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   
           os.startfile(vscPath)

       elif 'how are you' in query:
           speak('I am fine thank you , how are you')

       elif 'who is your boss' in query:
           speak("my boss's name is vidnyani umathee")

       elif 'who is your sister' in query:
           speak("my sister's name is vaishnavi didi")
           
       
       elif 'message panda' in query:
           speak("Hello panpan , this is bunniexa virtual assistant of bunbun . i want to say bunbun loves you very much. ")

       elif 'quit' in query:
           print("Quitting...Thanks for your time...")
           exit()
              
