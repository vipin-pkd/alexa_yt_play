import speech_recognition as sr
import pyttsx3
import pywhatkit 

listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty("voice", voice[2].id)
engine.say('hey, I am your alexa')
engine.say('how can i help you , master ' )
engine.runAndWait()


def take_command():
    try:
        
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command
def run_alexa():
    command= take_command()
    print(command)
    
    if "play" in command:
        song=command.replace('play','')
        engine.say('playing'+song)
        pywhatkit.playonyt(song)               
