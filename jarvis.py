import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', 'spanish')


def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('Saludos')


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="es-ES")
            command = command.lower()
            
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    
            
    except:
        pass # Do nothing when exception happens
    
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'pon' in command: #play
        song = command.replace('pon', '')
        talk('reproduciendo ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime().now.strftime('%H:%M')
        talk('Son las ' + time)

run_jarvis()


