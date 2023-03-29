import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the engine
engine = pyttsx3.init()

# Define a function to speak


def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize speech


def recognize_speech():
    with sr.Microphone() as source:
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        print("Speak now...")
        audio = r.listen(source)
        try:
            # Use Google Speech Recognition to transcribe audio
            text = r.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

# Define your assistant's commands


def process_command(command):
    if "hello" in command.lower():
        speak("Hello! How can I help you?")
    elif "how are you" in command.lower():
        speak("I'm doing well, thank you for asking!")
    elif "what time is it" in command.lower():
        speak("It's currently [insert current time here].")
    elif "stop" in command.lower():
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")


# Start the assistant
speak("Hello! How can I help you?")
while True:
    command = recognize_speech()
    process_command(command)
