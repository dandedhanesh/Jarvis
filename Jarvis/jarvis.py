import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import wikipedia
import random
import keyboard
import smtplib

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    # It takes microphone input and return that as string
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening....")
        
        audio = r.listen(source)
        
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        r.pause_threshold = 0.5
        r.energy_threshold = 1000
        print(f"User said: {query}\n")  
        return query      
    except Exception as e:
        print("Say that again Please")
        return "None"
            
            
def sendEmail(to,content):
    server=smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your-email','password')
    server.sendmail('your-email',to,content)
    server.close()                 
    
        
    
def wishme():
    time=int(datetime.datetime.now().hour)
    if time>=0 and time<=12:
        speak("Good morning sir I am your assistant , how can i help you ")

    elif time>=12 and time<=18 :
        speak("Good afternoon sir I am your assistant , how can i help you ")     
        
    else:
         speak("Good Evening sir I am your assistant , how can i help you ")

# def close(query):
#     speak('ok sir wait a second')
#     if 'close youtube' in query:
#         os.system("TASKKILL/F/in chrome.exe")
#     elif 'chrome' in query:
#         os.startfile("TASKKILL/F/in chrome.exe") 
    
if __name__== "__main__":
        wishme()
        
        while(True):
            query = takeCommand().lower()
            # query = input("Input please : ")
            # print(query)
            if 'wikipedia' in query:
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=3)
                speak("Accoding to Wikipedia") 
                print(results)
                speak(results)       
            
            if 'open chrome' in query:
             chrome_dir= 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome'
             speak('here you go to the chrome\n')
             os.startfile(os.path.join(chrome_dir))
             
            if 'close tab' in query:
                keyboard.press_and_release("ctrl+w")
            
            if 'open new tab' in query:
                keyboard.press_and_release("ctrl+t")
                
            if 'open previous tab' in query:
                keyboard.press_and_release("ctrl+shift+t")    
            
            if 'open new window in query' in query:
                keyboard.press_and_release("ctrl+n") 
                
            if 'type in web' in query:
                speak("Ready to write sir")
                query1 = takeCommand().lower()
                keyboard.press_and_release("ctrl+a")
                keyboard.press_and_release("backspace")
                for i in query1: 
                   keyboard.press_and_release(i) 
                # keyboard.press_and_release("enter")      
            if 'type' in query:
                speak("Ready to write sir")
                query1 = takeCommand().lower()
                for i in query1: 
                   keyboard.press_and_release(i) 
                # keyboard.press_and_release("enter")   
                
            if 'enter' in query:
                keyboard.press_and_release("enter")       
            
            if 'open incognito' in query:
                keyboard.press_and_release("ctrl+shift+n")        
             
            if 'open youtube' in query:
                webbrowser.open("www.youtube.com")
                
            if 'open google' in query:
                webbrowser.open("www.google.com") 
            
            if 'open stack overflow' in query:
                webbrowser.open("www.stackoverflow.com")                 
                
            if 'open spotify' in query:
                 os.system("Spotify")    
            if 'open file explorer' in query:
                 os.system("File Explorer")    
                 
            if 'open code' in query:
                  code_dir = 'C:\\Users\\dande\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code'
                  os.startfile(os.path.join(code_dir))     
                  
            if 'play songs' in query:
                songs_dir = 'C:\\Users\\dande\\OneDrive\\Documents\\Projects\\Web\\Spotify\\songs'      
                songs = os.listdir(songs_dir)
                r = random.randint(0,len(songs)-1)
                os.startfile(os.path.join(songs_dir,songs[r]))  
                
            if 'open instagram' in query:
                instagram_dir ='C:\\Users\\dande\\OneDrive\\Documents\\Apps Shortcuts\\Instagram.lnk'
                os.startfile(instagram_dir)
            
           # if 'open facebook' in query:
    
                
            # if 'open mail' in query:
            #     mail_dir = ''
            #     os.startfile(os.path.join(mail_dir))       
                
            if 'open zoom' in query:
                zoom_dir = 'C:\\Users\\dande\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom\\Zoom'  
                os.startfile(os.path.join(zoom_dir))      
            
            if 'time' in query:
                strTime =  datetime.datetime.now().strftime("%H:%M:%S")   
                speak(f"The time is {strTime}")
                
            if 'send email' in query:
                 try:
                #    speak("To whom would you like to send")
                   to : "reciever-email"
                   speak("What should i send")
                   content:takeCommand()
                   sendEmail(to,content)
                   speak("sent successfully")
                 except Exception as e :
                     speak("Sorry sir I couldn't send")  
                        
            if 'sleep' in query:
                speak("On your order sir")
                break            