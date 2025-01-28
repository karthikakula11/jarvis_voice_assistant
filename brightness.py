import subprocess
import pyttsx3 as pyt
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyt.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        listener.pause_threshold = 1
        voice = listener.listen(source, timeout=15, phrase_time_limit=5)
    
    try:
        print("Recognizing...")
        query = listener.recognize_google(voice, language="en-in")
        query = query.lower()
        print(f"user said: {query}")
    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        return "none"
    return query

def run_powershell_command(cmd):
    try:
        completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True, check=True)
        return completed.stdout
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return e.stderr

def set_brightness(brightness_percentage):
    if 0 <= brightness_percentage <= 100:
        command = f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, {brightness_percentage})"
        result = run_powershell_command(command)
        speak(f"Brightness set to {brightness_percentage} percent")
    else:
        speak("Please provide a valid brightness percentage between 0 and 100")

def handle_query(query):
    if "set brightness" in query or "set brightness percentage" in query:
        print("How much brightness percentage should I set?")
        speak("How much brightness percentage should I set?")
        take_brightness = takecommand()

        try:
            brightness_percentage = int(take_brightness)
            set_brightness(brightness_percentage)
        except ValueError:
            speak("Please provide a valid number for brightness")
    else:
        speak("Command not recognized. Please try again.")

# Simulate user input for testing
if __name__ == '__main__':
    query = takecommand()  # Normally, you'd get this from actual user input
    handle_query(query)
