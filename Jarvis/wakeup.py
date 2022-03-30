import os
import speech_recognition as sr



def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query




while True:
    query=takecommand()

    if 'wake up' in query:
        os.startfile('C:\\Users\\dande\\OneDrive\\Documents\\Projects\\Python\\Jarvis\\jarvis.py')    
        break;
       