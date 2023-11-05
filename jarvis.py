import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def get_instruction():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
        instruction = recognizer.recognize_google(audio).lower()
        print("You said: " + instruction)
        return instruction
    except sr.WaitTimeoutError:
        print("Timeout waiting for speech input")
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    except sr.RequestError as e:
        print("Error in request to speech recognition service: {0}".format(e))

def execute_instruction(instruction):
    if "open browser" in instruction:
        talk("Opening a web browser")
        webbrowser.open("https://www.google.com")
    elif "open whatsapp" in instruction:
        talk("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com/")
    elif "open youtube" in instruction:
        talk("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'exit' in instruction:
        talk("Goodbye!")
        exit()
    else:
        talk("I'm not sure how to respond to that")

while True:
    instruction = get_instruction()
    execute_instruction(instruction)
