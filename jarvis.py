import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', 'spanish')


def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('Saludos')


try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language="es-ES")
        command = command.lower()
        
        if 'jarvis' in command:
            talk(command)
            print(command)

        
except:
    pass # Do nothing when exception happens