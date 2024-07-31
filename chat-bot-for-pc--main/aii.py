from logging import exception
from time import strftime
from unicodedata import name
from urllib import response
from winreg import QueryInfoKey, QueryValue
from winsound import PlaySound
import pyttsx3
import speech_recognition as sr
import datetime
from torch import true_divide
import wikipedia
import webbrowser
import os
import smtplib
from random import choice
import pyjokes
import requests
import pywhatkit as kit
import subprocess
import subprocess as sp
import python_weather
import winshell
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import keyboard

from click_photo import click


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def backspace():
    keyboard.press('alt')
    keyboard.press('f4')
    keyboard.release('f4')
    keyboard.release('alt')


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

        speak("wake up sir ,  we are in loanala , ")
        speak("the room temperture is good ")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        speak("sir , we are in lonavala now ")
        speak("the temperture is good ")
    else:
        speak("Good Evening!")
        speak("sir , we are in lonavala now ")
        speak("the temperture is good ")


def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def open_camera():

    sp.run('start microsoft.windows.camera:', shell=True)


def open_cmd():

    os.system('start cmd')


def shut_down():

    os.system("shutdown /s /t 1")


def alrm():
    speak("enter the time")
    speak("ok , sir let me set the time for you ")
    speak("sir , please can you enter the time for me , beacause sometimes i listen wrong time ,  its helps you to set correct time  ")
    time = input("enter the time")
    speak("thats great , sir thats the sufficient for us ")
    speak(
        f"you can chill ,  till {time} , i will imform you after the  time over ")

    while True:
        time_ac = datetime.datetime.now()
        now = time_ac.strftime("%H:%M:%S:")

        if now == time:
            speak("time to wake up sir !")
            PlaySound('Toofan - KGF Chapter 2.mp3')
            speak("alarm closed !")
        elif now > time:
            break


def open_mypc():

    os.system("explorer.exe  file:")


def open_drive_d():
    os.startfile("D:")


def open_drive_c():
    os.startfile("C:")
# def close():
    # os.close()


def restart():
    os.system("shutdown /r /t 1")


# def sleep():
#     os.system("shutdown -1")
if __name__ == "__main__":
    wishMe()
    speak("if  you want something  .")
    speak("i am here for you")
    while True:
        
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif  "ok" in query or "the bookmarks bar" in query:
            from functions import open_booksmarks_bar
            open_booksmarks_bar()
    
        elif"hello" in query:
            speak("hello  dear , how are you ")
        elif"on youtube" in query:
            Query = query.replace("search on youtube", "")
            query = Query.replace("play", "")
            from you_tube_search import you_youtube_src
            you_youtube_src(query)
        elif"where i am now" in query:
            speak("sir , we are in lonavala  ")

        elif"alarm" in query:
            alrm()

        elif"shut down" in query or "poweroff" in query or "shutdown" in query or "poweroff" in query:
            speak("ok sir , i am here for you always, if you need me , just call me , but for now i am turning off")
            speak("take care sir ....")
            shut_down()

        elif "cmd" in query:
            speak("ok , sir let me open the command prompt")
            open_cmd()
            speak("sir , here i open the command prompt")
            speak("its done  sir ")
        elif "open the camera" in query:
            speak("ok i can do it  for you , sir  ")
            speak("give me a second")
            open_camera()
        elif"scan" in query:
            speak("ok sir , i think you have some problem whith your system")
            speak("wait sir let me scan ")
            from functions import scan
            scan()

        elif"stop" in query:
            speak("ok sir , if you feel like you are safe then i will stop the scan")
            speak("i am going to stop the scan")
            from functions import stop_scan
            stop_scan()
            speak("scan is stop sir can i delete this tab ")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'restart' in query:
            speak(
                "sir , i think you have some problems whith your system , ok let me restart the system")
            restart()
        elif 'fine' in query or "good" in query:

            speak("It's good to know that your fine")
        elif 'turn on bluetooth' in query or 'turn off bluetooth' in query:
            from bluetooth import blue
            speak("ok sir , let me do it")
            blue()
            speak("i did it,sir")
        elif"bluetooth on" in query or "hide this" in query:
            speak("ok sir ")
            keyboard.press_and_release('windows+a')
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak("fury")

        elif "take a break" in query:
            break
            # print("My friends call me fury ")
        elif "click" in query:
            from click_photo import click
            speak("ok , smile sir ")
            click()
            speak("i clicked picture sir ")
        elif "in system" in query:
            pass
        elif "who made you" in query or "created you" in query:
            speak("I have been created for pbl .")
            speak("i am created by group1 of s2 batch ")

        elif "who i am" in query:
            speak("If you talk then definitely you are human.")

        elif 'empty the recycle bin' in query:
            speak("ok sir if there is no important file in recycle bin")
            speak('i will recycle the recycle bin ')
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("boom!")
            speak("Recycle Bin Recycled")
        elif "open my pc" in query:
            speak("wait a second sir , here i open the my pc ")
            open_mypc()
            speak("do you want open any disk")
        elif "open the d" in query:
            speak("opening disc d")
            open_drive_d()
        elif "delete" in query:
            speak("ok , let me clear this folder")
            backspace()
            speak("its done")
        elif "open start" in query:
            speak("ok sir , i will do it for you")
            from open_start_butten import start_start
            start_start()
            speak("here is your start menu")
        elif"close start" in query:
            speak("sure sir")
            from open_start_butten import close_start
            close_start()

        elif"open the c" in query or "open the si" in query:
            speak("opening disc c")
            open_drive_c()
        elif "why you came to world" in query:
            speak("Thanks to sushant. further It's a secret")
        elif 'search' in query:
            speak(f"let me see what i find for {query}. wait a second sir ")
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)
            speak(f"this is i know about  {query}")
        elif 'who are you' in query:
            speak("hello  , i am fury , i am artificial intelligence ")
        elif 'open pdf' in query:
            speak("ok , i will do that for you")
            speak("opening pdf")
            power = r"C:\Users\hp\Desktop\dbms2.pdf"
            os.startfile(power)
            speak("done ")
        elif 'open youtube' in query:
            speak("ok , sir  i can do it for you  ")

            webbrowser.open("youtube.com")
            speak(" here i open the youtube")
        elif 'open google' in query:
            speak("ok,  i will do that for you , sir ")
            webbrowser.open("google.com")
            speak("done sir , the google is ready , for use ")
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("get it sir , here i open the stakoverflow")
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'songs' in query:
            speak("get it sir , enjoy the songs")
            music_dir = 'C:\\Users\\hp\\Downloads\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        # elif "sleep" in query:
            # speak("ok sir , i think you have some other work , ok till you come back , i will sleep")
            # speak("byeee.. sir. take care")
            # sleep()
        elif "notepad" in query:
            note = r"C:\Windows\notepad.exe"
            speak("ok i am opening the notepad")
            os.startfile(note)
            speak("sir ,  notepad is ready to use")
        # elif 'type' in query or 'typing' in query:
        #     speak("tell me what can i write")
        #     wrt = takeCommand()
        #     print(wrt)
        #     f = open("notepad.txt", 'w')
            # speak(f.write(wrt))
        # elif 'close tab' in query:
            # os.system("taskkill /f /im")
        elif "open messages" in query or "open the messages" in query:
            speak("ok sir i can open the whatsapp for you ")
            from open_watsap import open_wt
            open_wt()
            speak("here i open the whatsapp sir ")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif query == 'hello fury':
            speak("hello sir hoew are you")
        elif 'email to sushant' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kokatesushantsk@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend  sushant. I am not able to send this email")
# hello