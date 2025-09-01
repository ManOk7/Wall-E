import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import cv2

#Intializing audio drivers to change the volume if needed 
devices = AudioUtilities.GetSpeakers() 
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

#Setting up the voice of assistant
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

CREDS = {'email' : 'MANAKKUSHWAHA_014907@shift1.onmicrosoft.com','passwd':'141f48ba-09b3-47a2-8ecf-'}

def join():
    global driver
    driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://teams.microsoft.com")
    time.sleep(2)
    emailField = driver.find_element_by_xpath('//*[@id="i0116"]')
    emailField.click()
    emailField.send_keys(CREDS['email'])
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    time.sleep(2)
    passwordField = driver.find_element_by_xpath('//*[@id="i0118"]')
    passwordField.click()
    passwordField.send_keys(CREDS['passwd'])
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click() #Sign in button
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click() #remember login
    time.sleep(7)
    teams1 = driver.find_element_by_xpath('//*[@id="app-bar-2a84919f-59d8-4441-a975-2a8c2643b741"]')
    teams1.click()
    time.sleep(2)
    teams2 = driver.find_element_by_xpath('//*[@id="favorite-teams-panel"]/div/div[1]/div[2]/div[2]/div/ng-include/div/div')
    teams2.click()

def joinbtn():
            try:
                cls=driver.find_element_by_xpath('//*[@id="m1644901618078"]/calling-join-button/button')
                cls.click()
                time.sleep(5)
                webcam = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
                if(webcam.get_attribute('title')=='Turn camera off'):
                    webcam.click()
                time.sleep(1)

                microphone = driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]')
                if(microphone.get_attribute('title')=='Mute microphone'):
                    microphone.click()

                time.sleep(1)
                joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
                joinnowbtn.click()
            except:
                speak("Sir it seems there no class today")


def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour <= 12:
        speak("Good Morning")
    elif hour <= 16:
        speak("Good Afternoon")
    elif hour < 23:
        speak("Good Evening")
    speak("How can i help you")   
    
def takeCommand():  
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:   
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
    
if __name__=="__main__":    
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'tell me about yourself' in query:
            print("i am Walll E and i am your virtual assistant")
            speak("i am Walll E and i am your virtual assistant")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

        elif 'join english' in query:
            speak("joining english class")
            join()
            time.sleep(2)
            english = driver.find_element_by_xpath('//*[@id="channel-19:2a314cb476074a0494d67b0f68cacb52@thread.tacv2"]/a/div[1]')
            english.click()
            time.sleep(1) 
            joinbtn()
                
        elif 'join maths' in query:
            speak("joining maths class")
            join()
            time.sleep(2)
            english = driver.find_element_by_xpath('//*[@id="channel-19:6e570121e6684599ae97b285a6d229f4@thread.tacv2"]/a/div[1]/span')
            english.click()
            time.sleep(1)
            joinbtn()    

        elif 'what is your name' in query:
            print("My name is Wall E ")
            speak("My name is Wall E ")

        elif 'open kv noida' in query:
            webbrowser.open("noida.kvs.ac.in")
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open chrome' in query:
            path1="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path1)

        elif 'decrease volume' in query or 'decrease the volume' in query:
            print('Decreasing Volume')
            speak('Decreasing Volume')
            y=volume.GetMasterVolumeLevel()
            if y <= -49.61552047729492:
                pass
            else:
                volume.SetMasterVolumeLevel(y-5, None)
        elif 'increase volume' in query or 'increase the volume' in query:
            print('Increasing Volume')
            speak('Increasing Volume')
            y=volume.GetMasterVolumeLevel()
            if y >= -4.912779808044434:
                pass
            elif y <= -23.654823303222656:
                volume.SetMasterVolumeLevel(y+15, None)
            else:
                volume.SetMasterVolumeLevel(y+5, None)

        elif 'mute' in query:
            print('muting volmune')
            speak('muting volmune')
            volume.SetMasterVolumeLevel(-65.25, None)

        elif 'start webcam' in query or 'start the webcam' in query:
            print('starting webcam')
            speak('starting webcam')
            cap = cv2.VideoCapture(0)
            ptime = 0
            ctime = 0

            while True:
                success, img = cap.read()
                imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                ctime = time.time()
                fps = 1/(ctime-ptime)
                ptime = ctime
                cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

                cv2.imshow("Image",img)
                cv2.waitKey(1)

        elif 'who developed' in query:
            print("The Development of this project is done by Manak kushwaha")
            speak("The Development of this project is done by Manak kushwaha")

        elif 'who created' in query:
            print("The Development of this project is done by Manak kushwaha")
            speak("The Development of this project is done by Manak kushwaha")

        elif 'stop' in query:
            break
            
        

    
  
   
    
        
            
            
        

            
