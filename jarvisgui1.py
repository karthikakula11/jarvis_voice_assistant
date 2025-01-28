import os# os ki sambandinchina tasks like opening notepad or playing music os lo unna edaina application aopen cheyadaniki or access cheyadaniki vadtham
import tkinter as tk# tkinter thoni ui develop cheyachu python lo
from tkinter import messagebox#
from PIL import Image, ImageTk, ImageSequence # start and quit button pil thone chesam
import threading# multiple tasks okesari run cheyadaniki vadtham
import datetime# to know date and time
import ctypes# turn on off screen ki
import cv2# camera ki sambandinchina vati kosam cv2
import numpy as np# numpy arrays laga
import subprocess# battery brighness kosam
from ffpyplayer.player import MediaPlayer# music play kosam
from re import S
import pyttsx3 as pyt #matladindi speech to text and text to speehch chesthadi compiler ki
import speech_recognition as sr # matladindi vinanaiki 
import datetime
import random# random songs play cheyaniki
import pyautogui# alt+tab lantikeyboard shortcuts kosam
from requests import get#avsrm ledhu
import requests#avsrm ledhu code lo dhiniki m pani ledhu
import wikipedia#wikipedia search kosam
import webbrowser#to open matter inn web browser
from pydub import AudioSegment# to play start and end sound
from pydub.playback import play
import urllib.request
import time
# from jarvis_intro import *
import winshell # used to clean recycle bin
import sys
import cv2
import numpy as np
import ctypes# to turn the screenoff and on
import win32api, win32con #to turn the screen off and on

import pywhatkit # whatsapp msg kosam ee module
from bs4 import BeautifulSoup

# Initialize text-to-speech engine
engine = pyt.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
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

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis, how can i help you")

def open_camera():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        speak("Error: Could not open camera")
        print("Error: Could not open camera")
        return

    while True:
        ret, frame = camera.read()
        if not ret:
            speak("Error: Could not capture a frame")
            print("Error: Could not capture a frame")
            break
        
        cv2.imshow("Camera", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


def draw_sketch():
    print("Sure, please give me 5 to 10 seconds to draw your sketch")
    speak("Sure, please give me 5 to 10 seconds to draw your sketch")
    print("To exit from the live sketch diagram press 'q'")
    speak("To exit from the live sketch diagram press 'q'")

    camera = cv2.VideoCapture(0)
    
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Failed to capture image from camera.")
            break

        # Getting width and height of image
        height, width, _ = frame.shape

        # Creating copy of image using resize function
        resized_image = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

        # Creating 3x3 kernel to sharpen the image
        kernel = np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]])
        sharpened_image = cv2.filter2D(resized_image, -1, kernel)

        # Converting image into grayscale
        gray = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2GRAY)

        # Creating inverse of sharpened image
        inverse_image = 255 - gray

        # Applying Gaussian blur to the image
        blurred_image = cv2.GaussianBlur(inverse_image, (15, 15), 0, 0)

        # Creating pencil sketch using divide function
        pencil_sketch = cv2.divide(gray, 255 - blurred_image, scale=256)

        # Displaying the sketches and original frame
        cv2.imshow("Pencil Sketch", pencil_sketch)
        cv2.imshow("Frame", frame)

        # Exit if 'q' is pressed
        key = cv2.waitKey(1)
        if key == ord('q') or key == ord('Q'):
            break

    # Clean up
    cv2.destroyAllWindows()
    camera.release()
    print("You might think the live sketch diagram is not that great. The problem is the laptop camera comes with only 1-megapixel resolution; I can't do anything about it.")
    speak("You might think the live sketch diagram is not that great. The problem is the laptop camera comes with only 1-megapixel resolution; I can't do anything about it.")





def run_jarvis():
    # Declare global variables if you need to modify them
    import os
    global chose
    chose = 0

    wishme()



    while True:
            query = takecommand()
            query = query.replace("jarvis", "")
        
            if "introduce yourself" in query or "tell me about yourself" in query or "jarvis introduce yourself" in query:
                speak("hello, I am jarvis")
            
            elif "clean recycle bin" in query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
            
            elif "turn off the screen" in query or "turn the screen off" in query or "turn of my screen" in query:
                ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)
            
            elif "turn on the screen" in query or "turn the screen on" in query or "turn on my screen" in query:
                ctypes.windll.user32.SendMessageW(65535, 274, 61808, -1)
            
            elif "music" in query or "hit some music" in query or "play music" in query:
                print("playing music")
                speak("playing music")
                music_dir_path = "D:\\music"
                try:
                    songs = os.listdir(music_dir_path)
                    d = random.choice(songs)
                    os.startfile(os.path.join(music_dir_path, d))
                    chose += 1
                except Exception as e:
                    print(f"Error playing music: {e}")
                    speak("Error playing music")

            elif "next" in query or "i don't like this" in query or "next song" in query:
                music_dir_path = "D:\\music"
                try:
                    songs = os.listdir(music_dir_path)
                    length = len(songs)
                    if chose >= length:
                        print("no more music to next")
                        speak("no more music to next")
                        chose = 0
                    os.startfile(os.path.join(music_dir_path, songs[chose]))
                    chose += 1
                except Exception as e:
                    print(f"Error playing next song: {e}")
                    speak("Error playing next song")

            elif "before song" in query or "repeat" in query or "repeat the song" in query or "previous  song" in query:
                music_dir_path = "D:\\music"
                try:
                    songs = os.listdir(music_dir_path)
                    length = len(songs)
                    if chose < 0:
                        print("no more music to go back")
                        speak("no more music to go back")
                        chose = 0
                    os.startfile(os.path.join(music_dir_path, songs[chose]))
                    chose -= 1
                except Exception as e:
                    print(f"Error playing previous song: {e}")
                    speak("Error playing previous song")
            
            elif 'stop' in query or "stop the music" in query or "quit music" in query or "stop music" in query:
                speak('okay')
                print("okay! Now I stop the music")
                speak("now I stop music")
                try:
                    os.system('taskkill /F /FI "WINDOWTITLE eq Movies & TV" ')
                    os.system('taskkill /F /FI "WINDOWTITLE eq Groove Music" ')
                    os.system('taskkill /F /FI "WINDOWTITLE eq Media Player" ')
                    os.system('taskkill /F /FI "WINDOWTITLE eq Windows Media Player" ')
                except Exception as e:
                    print(f"Error stopping music: {e}")
                    speak("Error stopping music")

            
            elif "mute volume" in query or "mute the volume" in query:
                    from pynput.keyboard import Key,Controller  
                    keyboard = Controller()
                    for j in range(50):
                        keyboard.press(Key.media_volume_down) 
                        keyboard.release(Key.media_volume_down)
            
            elif "unmute volume" in query or "unmute the volume" in query:
                from pynput.keyboard import Key,Controller  
                keyboard = Controller()
                for j in range(50):
                    keyboard.press(Key.media_volume_up) 
                    keyboard.release(Key.media_volume_up)

        # <----------------setting volume to specific number---------------------------->
            
            elif "set volume to " in query or "set volume " in query: 
                query = query.replace("set volume to ", "")#the query should be as it is the spaces should also be their to  replace perfectly
                query = query.replace("set volume ", "")
                from pynput.keyboard import Key,Controller  
                keyboard = Controller()

                # range(1)= decreases or increases 2 percent volume (multiple of 2) range(50) means volume becomes 100

                for j in range(50):
                    keyboard.press(Key.media_volume_up) 
                    keyboard.release(Key.media_volume_up)
                #volume ni first 100 chesthanam tarwata dhanni set chesetappudu decrease chesthanam in this way we get accurate results in volume
                volrange=0
                # volume=self.takecommand()

                if query=="100" or query=="hundred" or query=="200":
                    volrange=50
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_up)
                        keyboard.release(Key.media_volume_up)

                elif query =="90" or query=="ninety":
                    volrange=5 #5x2=10, 100-10 =90
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

                elif query =="80" or query=="eighty":
                    volrange=10  #10x2=20, 100-20 =80
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

                elif query =="70" or query=="seventy":
                    volrange=15
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)
                
                elif query =="60" or query=="sixty":
                    volrange=20
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

                elif query =="50" or query=="fifty":
                    volrange=25
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)
                
                elif query =="40" or query=="fourty" or query=="forty":
                    volrange=30
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

                elif query =="30" or query=="thirty":
                    volrange=35
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

                elif query =="20" or query=="twenty":
                    volrange=40
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)
                
                elif query =="10" or query=="ten":
                    volrange=45
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

                elif query =="0" or query=="zero":
                    volrange=50
                    for i in range(volrange):
                        keyboard.press(Key.media_volume_down)
                        keyboard.release(Key.media_volume_down)

        

            elif "how are you" in query:
                speak("I'm great thanks for asking")
            
            elif "hai" in query or "hello" in query:
                speak("Hi,How may i help you")
            
            elif 'your name' in query:
                speak("My name is jarvis")

            elif 'university name' in query:
                speak("you are studing in Chaitanya Deemed To Be University, with BSC Computer Science with cognitive system") 

            elif 'your age' in query:
                speak("I am very young that u")
            elif 'are you single' in query:
                speak('No, I am in a relationship with wifi')
            
            elif 'joke' in query or "tell me a joke" in query:
                import pyjokes
                speak(pyjokes.get_joke())
                print(pyjokes.get_joke())
            elif 'are you there' in query:
                speak('Yes I am here')
            elif 'thank you' in query:
                speak('I am here to help you..., your welcome')
            elif 'do you ever get tired' in query:
                speak('It would be impossible to tire of our conversation')

            elif "set brightness" in query or "set brightness percentage" in query or "brightness" in query:
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
                speak("How much brightness percentage should I set?")
                take_brightness = takecommand()

                try:
                    brightness_percentage = int(take_brightness)
                    set_brightness(brightness_percentage)
                except ValueError:
                    speak("Please provide a valid number for brightness")

            elif "open notepad" in query or "open Notepad" in query:
                if True:
                    speak("opening notepad")
                    os.system("start notepad")
                else:
                    speak("you dont have notepad in your system so i cannot open notepad")
            elif "close notepad" in query:
                os.system("TASKKILL /F /IM Notepad.exe")

            elif "open command prompt" in query:
                if True:
                    speak("opening command prompt")
                    os.system("start cmd")
                else:
                    speak("sorry you dont have command prompt")

            elif "close command prompt" in query:
                os.system("TASKKILL /F /IM cmd.exe")

            elif "open file explorer" in query:
                speak("opening file explorer")
                os.system("explorer")
            
            elif "take a selfie" in query or "selfie" in query or "take a photo" in query:
                import cv2
                import os
                print("press q to exit from mobile camera")
                speak("press q to exit from mobile camera")

                # Load the current selfie counter from a file, or start from 1 if it doesn't exist
                selfie_counter = 1

                if os.path.exists("selfie_counter.txt"):
                    with open("selfie_counter.txt", "r") as counter_file:
                        try:
                            selfie_counter = int(counter_file.read())
                        except ValueError:
                            print("Error: Could not read the counter from the file. Starting from 1.")

                # Initialize the camera
                camera = cv2.VideoCapture(0)

                # Check if the camera is opened successfully
                if not camera.isOpened():
                    print("Error: Could not open camera")
                    exit()

                # Capture a single frame from the camera
                ret, frame = camera.read()

                # Check if the frame was captured successfully
                if not ret:
                    print("Error: Could not capture a frame")

                # Define the filename with the sequential number
                selfie_filename = f"selfie_{selfie_counter}.jpg"

                # Save the captured frame as a selfie
                cv2.imwrite(selfie_filename, frame)

                # Display the selfie
                cv2.imshow("Selfie", frame)

                # Increment the counter for the next selfie
                selfie_counter += 1

                # Save the updated counter to the file
                with open("selfie_counter.txt", "w") as counter_file:
                    counter_file.write(str(selfie_counter))

                # Wait for a key press and then close the display window
                cv2.waitKey(0)
                cv2.destroyAllWindows()

                # Release the camera
                camera.release()


            elif "open camera" in query:
                print("Opening Camera")
                speak("Opening Camera")
                print("Press Q to close Camera")
                speak("Press Q to close Camera")
                open_camera()

            elif "open camera" in query:
                open_camera()

            # else:
            #     speak("I am not sure how to handle this request.")
            #     print("Unrecognized command")
            
            # elif "open camera" in query:
            #     speak("Opening camera")
            #     print("Press 'q' to close the camera")
            #     speak("Press 'q' to close the camera")
            #     cap = cv2.VideoCapture(0)
            #     while True:
            #         ret, img = cap.read()
            #         if not ret:
            #             speak("Failed to access the camera.")
            #             break
            #         cv2.imshow("Webcam", img)
            #         k = cv2.waitKey(1)  # Update the wait time for responsiveness
            #         if k == ord('q') or k == ord('Q'):
            #             break
            #     cap.release()
            #     cv2.destroyAllWindows()

            # elif "close camera" in query:
            #     speak("Closing camera")
            #     pyautogui.hotkey("q")



            # elif "open camera" in query:
            #     speak("opening camera")
            #     print("press q to close camera")
            #     speak("press q to close camera")
            #     cap = cv2.VideoCapture(0)
            #     while True:
            #         #
            #         ret, img = cap.read()
            #         cv2.imshow("webcam", img)
            #         k = cv2.waitKey(50)
            #         if k == ord("q") or k == ord("Q"):  # press q to close camera
            #             break
            #     cap.release()
            #     cv2.destroyAllWindows()
            # elif "close camera" in query:
            #     pyautogui.hotkey("q")
            
            # <-----------------------------------BATTERY PERCENTAGE(psutil module)------------------------->

            elif "battery percentage" in query or "what is my battery percentage" in query or "battery percentage in my system" in query:
                import psutil

                battery = psutil.sensors_battery()
                percentage = battery.percent
                if percentage >= 75 and percentage <= 100:
                    print(f"our system has {percentage} percent battery left,which is sufficient for about 2 hours at a moderate usage ")
                    speak(f"our system has {percentage} percent battery left,which is sufficient for about 2 hours at a moderate usage ")
                elif percentage >= 30 and percentage < 75:
                    print(f"our system has {percentage} percent battery left,which might give you 60 to 70 minutes at a moderate usage")
                    speak(f"our system has {percentage} percent battery left,which might give you 60 to 70 minutes at a moderate usage")
                elif percentage >= 0 and percentage < 30:
                    print(f"our system has a very crtical battery left, that is {percentage} percent battery,Please pluggin the charger")
                    speak(f"our system has a very crtical battery left, that is {percentage} percent battery,Please pluggin the charger")

            
            # <----------------IP ADDRESS(using request module)---------------------->
            elif "ip address " in query or "what is my ip address" in query or "my ip address" in query:

                ip = get("https://api.ipify.org").text  # website gives ip address we are converting it into text
                print(f"your ip address is: {ip} ")
                speak(f"your ip address is: {ip} ")

            # <----------------------------------------------WEATHER FORECAST USING JAJRVIS----------------------------------------->
            # THERE SHOULD BE "in" COMPULSORY IN  QUERY OTHERWISE THIS CODE WILL NOT WORK
            elif "temperature in" in query or "weather in" in query or "what's the weather in "\
                 in query or "weather at " in query or "what's the weather at" in query\
                    or "what is the weather at" in query or "what is the weather in" in query:
                city = query.split("in", 1)
                city1=query.split("at",1) # at,is or add cheyali ante take another variable and write query.split("is",1)
                soup = BeautifulSoup(requests.get(f"https://www.google.com/search?q=weather+in+{city[1]}").text,
                                    "html.parser")
                region = soup.find("span", class_="BNeawe tAd8D AP7Wnd")
                temp = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
                day = soup.find("div", class_="BNeawe tAd8D AP7Wnd")
                weather = day.text.split("m", 1)
                temperature = temp.text.split("C", 1)
                # Response("Its Currently"+weather[1]+"and"+temperature[0]+"celsius"+"in"+region.text)
                print("Its Currently" + weather[1] + " and " + temperature[0] + "celsius " + "in " + region.text)
                speak("Its Currently" + weather[1] + " and " + temperature[0] + "celsius " + "in " + region.text)

            elif "who" in query or "where " in query or "what is" in query or "how " in query:
                query = query.replace("who", "")
                query = query.replace("what is", "")
                query = query.replace("how", "")
                query = query.replace("where", "")
                info = wikipedia.summary(query, sentences=2)  # read only 3 sentences
                speak("according to wikipedia")
                print(info)
                speak(info)

            elif "todays date" in query or "date" in query:
                now = datetime.now()
                print("todays date:"+ now)
                speak("todays date:"+ now)


            elif "current time" in query or "time" in query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print('Current time is ' + time)
                speak('Current time is ' + time)


            # elif "what " in query \
            #     or "how" in query or "which" in query or "write" in query or "do you" in query:
            #     import openai
            #     import speech_recognition as sr
            #     import pyttsx3

            #     # OpenAI API key
            #     openai.api_key = " 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"
                    

            #         # Try to recognize the audio
                    

            #         # Use OpenAI to create a response
            #     response = openai.Completion.create(
            #         engine="text-davinci-003",
            #         prompt=query,
            #         temperature=0.7,
            #         max_tokens=300
            #         )

            #         # Get the response text
            #     response_text = str(response['choices'][0]['text']).strip('\n\n')
            #     print(response_text)

            #     # Speak the response
            #     engine.say(response_text)
            #     engine.runAndWait()
            #     print()

                
            elif "what is the time" in query or "time" in query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print('Current time is ' + time)
                speak('Current time is ' + time)

            elif "change voice to male" in query or "male voice" in query or "change to male voice" in query or "I want male voice"in query or "voice to male" in query:
                engine.setProperty("voice", voices[0].id)  # 1st parameter lo voices ani pedthe male voice ye osthadi everytime change it to voice and voices[should be 1 for female 0 for male]
                engine.setProperty("rate", 160)
                print("From now I will respond to you in male voice")
                speak("From now I will respond to you in male voice")

            elif "change voice to female" in query in query or "female voice " in query or "change to female voice" in query or "I want female voice "in query:
                engine.setProperty("voice", voices[1].id)  # 1st parameter lo voices ani pedthe male voice ye osthadi everytime change it to voice and voices[should be 1 for female 0 for male]
                engine.setProperty("rate", 160)
                print("From now I will respond to you in female voice")
                speak("From now I will respond to you in female voice")

            #<--------stop or wait jarvis for specific time---------------->
            elif "wait for " in query or "wait for another "in query:
                query=query.replace("wait for ","")
                query=query.replace("wait for another ","")
                import time
                if query=="10 seconds" or query=="ten seconds":
                    import time
                    print("okay,as you wish")
                    speak("okay,as you wish")
                    time.sleep(10)

                elif query=="20 seconds" or query=="twenty seconds":
                    print("okay,as you wish")
                    speak("okay as you wish")
                    time.sleep(20)

                elif query=="30 seconds" or query=="thiry seconds":
                    print("okay,as you wish")
                    speak("okay as you wish")
                    time.sleep(30)
                
                elif query=="40 seconds" or query=="forty seconds" or query=="fourty seconds":
                    print("okay,as you wish")
                    speak("okay as you wish")
                    time.sleep(40)
                
                elif query=="50 seconds" or query=="fifty seconds":
                    print("okay,as you wish")
                    speak("okay as you wish")
                    time.sleep(50)
                
                elif query=="60 seconds" or query=="sixty seconds":
                    print("okay,as you wish")
                    speak("okay as you wish")
                    time.sleep(60)


                # <------------------------------------SENDING WHATSAPP MESSAGE USING JARVIS------------------------------------------------->

            elif "send whatsapp message" in query or \
                            " i want to send a message in whatsapp" in query or "send a whatsapp message" in query \
                            or "whatsaap message" in query:

                contacts = {"kiran":"+917013290865","sai kiran":"+917816044490","faculty":"+918006551437",
                            "rohit":"+919573055820","karthik":"+919346848587","teja":"+919494413114","bunny":"+919959738780","satvik":"+917416710833"
                            }

                names_list = list(contacts.keys())  # converts keys to list
                speak("sure!,whom do you wanna send")
                msgloop = True
                while msgloop:
                    #
                    contact_name = takecommand()  # calling takemethod again to take voice input for this sepecific variable(contact_name)

                    if contact_name in names_list:
                        #
                        number = contacts[contact_name]
                        print(number)
                        print("what message u wanna send")
                        speak("what message u wanna send")
                        msg = takecommand()  # calling takemethod again to take voice input for this sepecific variable(msg)
                        print("your message:", msg)
                        speak("your message will be delivered in 10 to 30 seconds")
                        pywhatkit.sendwhatmsg_instantly(number, msg)  # pywhatkitsends msg instantly
                        print("message delivered")
                        speak("message delivered")
                        import time
                        time.sleep(5)
                        pyautogui.hotkey("alt","tab")
                        msgloop = False

                    else:
                        speak("please enter from available contacts")
                        msgloop = False
        # # set brightness percentage 
        #     elif "set brighntess level " in query or "set brightness" in query or "set brightness percentage" in query:
        #         def run(cmd):
        #          completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        #          return completed

        #         if __name__ == '__main__':
        #             print("how much brightness percentage should i set ?")
        #             speak("how much brightness percentage should i set ?")
        #             take_brightness=takecommand()
        #             command = "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1," + take_brightness + ")"
        #             hello_command = f"Write-Host {command}"
        #             hello_info = run(hello_command)
        #             speak(f"{take_brightness} brightness percentage set")
            
             # <-----------------------playing in youtube using pywhatkit------------------------>
            elif "play" in query:
                query = query.replace('play', '')  # empty string replaces play
                # if i say play saranga dariya then system takes only saranga dariya.''(in this empty string saranga dariya will be stored)
                print("Playing" + query)
                speak("Playing" + query)
                pywhatkit.playonyt(query)#yt=youtube
                import time
                time.sleep(5)# waiting for 3 seconds so that webpage loads and then press f
                #time.sleep(30)#waiting for 10 seconds so that no disturbance caused to user
            
            elif "full screen" in query:
                pyautogui.hotkey("f")
            
            elif "enter" in query or "press enter" in query:
                # Press the Enter key
                pyautogui.keyDown('enter')

                # Release the Enter key
                pyautogui.keyUp('enter')
            
            elif "open chrome" in query or "open browser" in query:
                import subprocess

                # Specify the path to the Chrome executable
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Replace with the actual path to chrome.exe

                # Open Chrome with a specific URL using subprocess
                url = 'https://www.google.com'  # Replace with the URL you want to open
                subprocess.Popen([chrome_path, url])


            
            elif "half screen" in query:
                pyautogui.hotkey("esc")
            
            elif "close youtube" in query:
                pyautogui.hotkey("alt","f4")


            elif "search" in query or "google" in query or "open google and search" in query:
                query = query.replace("search", "")
                query = query.replace("google", "")
                query = query.replace("open google and search", "")
                print("okay,Searching for", query)
                speak("okay searching for" + query)
                pywhatkit.search(query)
                import time
                time.sleep(10)
                pyautogui.hotkey("alt","tab")

                # webbrowser.open("www.youtube.com")


            # elif "open google" in query or "open google and search" in query:
            #     speak("sure,what should i search in google")
            #     cm=takecommand().lower()
            #     webbrowser.open(f"{cm}")

            elif "open facebook" in query:
                webbrowser.open("www.facebook.com")
            
            #for the below code we need import webdrivers 
            # elif "login facebook" in query or "login to facebook" in query:
            #         from selenium import webdriver
            #         import time

            #         # Initialize the web driver
            #         driver = webdriver.Chrome()

            #         # Navigate to Facebook's login page
            #         driver.get("https://www.facebook.com")

            #         # Provide your username and password
            #         username = 7013290865  # Replace with your actual Facebook username
            #         password = "Kiran@965226"  # Replace with your actual Facebook password

            #         # Fill in the login form
            #         driver.find_element_by_id("email").send_keys(username)
            #         driver.find_element_by_id("pass").send_keys(password)

            #         # Submit the form
            #         driver.find_element_by_id("loginbutton").click()

            #         # Let the browser run for a few seconds to complete the login
            #         time.sleep(5)

            #         # Close the browser
            #         driver.quit()






    # <------PYAUTOGUI FEATURES=used to automate python using shortcut keys------->
            elif "open hidden menu" in query:
                # win +X=opens hidden menu
                pyautogui.hotkey("winleft", "x")

            elif "open task manager" in query:
                # Crtl + Shift +Esc=opens task manager
                pyautogui.hotkey("ctrl", "shift", "esc")

            elif "open task view" in query:
                # win +tab=shows running tasks
                pyautogui.hotkey("winleft", "tab")

            elif "shift tab" in query or "switch tab" in query:
                # alt+tab=shifts the tab
                pyautogui.hotkey("alt", "tab")

            elif "take screenshot" in query:
                # win+prtscr
                pyautogui.hotkey("winleft", "prtscr")
                print("screenshot location C:\\Users\\kiran\\OneDrive\\Pictures\\Screenshots")
                speak("okay ,you the screenshot is in the given location")

            elif "take snip" in query:
                pyautogui.hotkey("winleft", "shift", "s")
                speak("please take your snip of your choice")

            elif "close current application" in query:
                pyautogui.hotkey("alt", "f4")
                
            elif "close " in query:
                query=query.replace("close ","")
                pyautogui.hotkey("alt", "f4")

            elif "take me to desktop" in query:
                pyautogui.hotkey("winleft", "d")

            elif "open new virtual desktop" in query:
                pyautogui.hotkey("winleft", "ctrl", 'd')

            elif "open file explorer" in query:
                pyautogui.hotkey("winleft", "e")

            elif "open run dialog box" in query:
                pyautogui.hotkey("winleft", "r")
            
            elif "select the text" in query or "select all" in query:
                pyautogui.hotkey("ctrl", "a")
                speak("selected")

            elif "copy the selected text" in query or "copy" in query:
                pyautogui.hotkey("ctrl", "c")
                speak("copied")

            elif "paste the copied text" in query or "paste" in query:
                pyautogui.hotkey("ctrl", "v")
                speak("pasted")

            elif "type what i say" in query:  # u might get error if you get error comment this code
                pyautogui.hotkey("winleft", "h")
                #time.sleep(5)
            
            elif "pause" in query or "pass" in query or "continue" in query or "clear the text" in query or "clear" in query:
                pyautogui.hotkey("space")

            
            elif "draw a sketch of me" in query or "draw a live sketch of me" in query or "draw a picture of me" in query or "draw a live sketch" in query:
                draw_sketch()

            
    # # <-----------------------------------BATTERY PERCENTAGE(psutil module)------------------------->

    #         elif "battery percentage" in query or "what is my battery percentage" in query or "battery percentage in my system" in query:
    #             import psutil

    #             battery = psutil.sensors_battery()
    #             percentage = battery.percent
    #             if percentage >= 75 and percentage <= 100:
    #                 print(f"our system has {percentage} percent battery left,which is sufficient for about 2 hours at a moderate usage ")
    #                 speak(f"our system has {percentage} percent battery left,which is sufficient for about 2 hours at a moderate usage ")
    #             elif percentage >= 30 and percentage < 75:
    #                 print(f"our system has {percentage} percent battery left,which might give you 60 to 70 minutes at a moderate usage")
    #                 speak(f"our system has {percentage} percent battery left,which might give you 60 to 70 minutes at a moderate usage")
    #             elif percentage >= 0 and percentage < 30:
    #                 print(f"our system has a very crtical battery left, that is {percentage} percent battery,Please pluggin the charger")
    #                 speak(f"our system has a very crtical battery left, that is {percentage} percent battery,Please pluggin the charger")

            elif "jarvis sleep" in query or "bye" in query or "sleep" in query or "close jarvis" in query:
                    speak("bye")
                    # speak("press exit to turn me off")
                    # pyautogui.hotkey("alt","f4")


        #<----------------------------------------DOCTORSTRANGEUSINGJARVIS---------------------------------------------->
            elif "make me doctor strange" in query or "i want to become doctor strange" in query\
                    or "make me doctor strange" in query:
                speak("as you wish")
                speak("but please wait for 10 to 30 seconds to open the camera")
                speak("i will assure you that you will enjoy it")
                print("press q to exit from doctor strange filter")
                speak("press q to exit from doctor strange filter")
                import doctorstrange
                '''Modules to import
                    Opencv
                    Mediapipe
                    Opencv-contrib

                    Type the following command in cmd
                    Pip install opencv-python mediapipe opencv-contrib-python
                    '''


                import cv2
                import mediapipe as mp

                mpHands=mp.solutions.hands #creates solution for hands

                hands=mpHands.Hands()#creating obj for hands

                mpDraw=mp.solutions.drawing_utils #draws lines for each finger

                video=cv2.VideoCapture(0)#0 means default camera attached to laptop

                video.set(3, 1000)
                video.set(4, 780)


                img_1 = cv2.imread('magic_circles/magic_circle_ccw.png', -1)
                img_2 = cv2.imread('magic_circles/magic_circle_cw.png', -1)



                def position_data(lmlist):
                    global wrist, thumb_tip, index_mcp, index_tip, midle_mcp, midle_tip, ring_tip, pinky_tip
                    wrist = (lmlist[0][0], lmlist[0][1])
                    thumb_tip = (lmlist[4][0], lmlist[4][1])
                    index_mcp = (lmlist[5][0], lmlist[5][1])
                    index_tip = (lmlist[8][0], lmlist[8][1])
                    midle_mcp = (lmlist[9][0], lmlist[9][1])
                    midle_tip = (lmlist[12][0], lmlist[12][1])
                    ring_tip  = (lmlist[16][0], lmlist[16][1])
                    pinky_tip = (lmlist[20][0], lmlist[20][1])


                def draw_line(p1, p2, size=5):
                    cv2.line(img, p1, p2, (50,50,255), size)
                    cv2.line(img, p1, p2, (255, 255, 255), round(size / 2))

                def calculate_distance(p1,p2):
                    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
                    lenght = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1.0 / 2)
                    return lenght


                def transparent(targetImg, x, y, size=None):
                    if size is not None:
                        targetImg = cv2.resize(targetImg, size)

                    newFrame = img.copy()
                    b, g, r, a = cv2.split(targetImg)
                    overlay_color = cv2.merge((b, g, r))
                    mask = cv2.medianBlur(a, 1)
                    h, w, _ = overlay_color.shape
                    roi = newFrame[y:y + h, x:x + w]

                    img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))
                    img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)
                    newFrame[y:y + h, x:x + w] = cv2.add(img1_bg, img2_fg)

                    return newFrame
                

                def startdoctorstrange():
                    while True:
                        deg = 0
                        global img
                        ret,img=video.read()

                        img=cv2.flip(img, 1)#by default we get camera left as right and right as left here we are flipping the camera right to right lft to lft

                        rgbimg=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#adding rgb colour
                        result=hands.process(rgbimg)

                        # DRAWING LANDMARKS TO THE HAND (see handmarks.png photo)
                        if result.multi_hand_landmarks:
                            for hand in result.multi_hand_landmarks:
                                lmList=[]
                                for id, lm in enumerate(hand.landmark):
                                    h,w,c=img.shape
                                    coorx, coory=int(lm.x*w), int(lm.y*h)
                                    lmList.append([coorx, coory])
                                    # cv2.circle(img, (coorx, coory),6,(50,50,255), -1)
                                # mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)
                                position_data(lmList)
                                palm = calculate_distance(wrist, index_mcp)
                                distance = calculate_distance(index_tip, pinky_tip)
                                ratio = distance / palm
                                print(ratio)
                                if (1.3>ratio>0.5):
                                    draw_line(wrist, thumb_tip)
                                    draw_line(wrist, index_tip)
                                    draw_line(wrist, midle_tip)
                                    draw_line(wrist, ring_tip)
                                    draw_line(wrist, pinky_tip)
                                    draw_line(thumb_tip, index_tip)
                                    draw_line(thumb_tip, midle_tip)
                                    draw_line(thumb_tip, ring_tip)
                                    draw_line(thumb_tip, pinky_tip)
                                if (ratio > 1.3):
                                        centerx = midle_mcp[0]
                                        centery = midle_mcp[1]
                                        shield_size = 3.0
                                        diameter = round(palm * shield_size)
                                        x1 = round(centerx - (diameter / 2))
                                        y1 = round(centery - (diameter / 2))
                                        h, w, c = img.shape
                                        if x1 < 0:
                                            x1 = 0
                                        elif x1 > w:
                                            x1 = w
                                        if y1 < 0:
                                            y1 = 0
                                        elif y1 > h:
                                            y1 = h
                                        if x1 + diameter > w:
                                            diameter = w - x1
                                        if y1 + diameter > h:
                                            diameter = h - y1
                                        shield_size = diameter, diameter
                                        ang_vel = 2.0
                                        deg = deg + ang_vel
                                        if deg > 360:
                                            deg = 0
                                        hei, wid, col = img_1.shape
                                        cen = (wid // 2, hei // 2)
                                        M1 = cv2.getRotationMatrix2D(cen, round(deg), 1.0)
                                        M2 = cv2.getRotationMatrix2D(cen, round(360 - deg), 1.0)
                                        rotated1 = cv2.warpAffine(img_1, M1, (wid, hei))
                                        rotated2 = cv2.warpAffine(img_2, M2, (wid, hei))
                                        if (diameter != 0):
                                            img = transparent(rotated1, x1, y1, shield_size)
                                            img = transparent(rotated2, x1, y1, shield_size)


                        # print(result)
                        window_name = "doctor strange"
                        cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)  # necessary for full screen
                        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)  # necessary for full screen
                        cv2.imshow(window_name,img)#shows camera name as img

                        # used for camera moment if u keep it 100 or 1000 the camera moment will be very slow for eg if u move ur face it will reflect after 100milliseconds
                        k=cv2.waitKey(1)
                        if k==ord('q'):
                            break
                startdoctorstrange()

                video.release()
                cv2.destroyAllWindows()



                    # to make this work we have to link whatsapp web in microsoft edge to mobile
                    # elif "send WhatsApp message" in query:
                    #     pywhatkit.sendwhatmsg("+919652261371",
                    #                           "hello i am jarvis this message is sent by my boss from pycharms code", 11, 57)



def facerecognition():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
    recognizer.read('trainer/trainer.yml')  # Load trained model
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)  # Initialize Haar Cascade for face detection

    font = cv2.FONT_HERSHEY_SIMPLEX  # Font type

    names = ['', 'kiran', 'sri teja', 'shalini', 'abu', 'pramod']  # Names list; leave first empty because ID starts from 0

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Initialize webcam with cv2.CAP_DSHOW to suppress warnings
    cam.set(3, 640)  # Set video FrameWidth
    cam.set(4, 480)  # Set video FrameHeight

    minW = 0.1 * cam.get(3)  # Minimum width for face detection
    minH = 0.1 * cam.get(4)  # Minimum height for face detection

    while True:
        ret, img = cam.read()  # Read frames from webcam

        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle around face

            id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])  # Predict face ID

            if (accuracy < 100 and accuracy >= 40):  # Check accuracy
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))

                # Play welcome video
                def welcomebacksir(video_path):
                    video = cv2.VideoCapture(video_path)
                    player = MediaPlayer(video_path)
                    window_name = "welcome back sir"
                    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
                    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    while True:
                        grabbed, frame = video.read()
                        audio_frame, val = player.get_frame()
                        if not grabbed:
                            print("End of video")
                            break
                        if cv2.waitKey(22) & 0xFF == ord("q"):
                            break
                        cv2.imshow(window_name, frame)
                        if val != 'eof' and audio_frame is not None:
                            img, t = audio_frame
                    video.release()
                    cv2.destroyAllWindows()
                    
                welcomebacksir("welcomebacksir.mp4")
                
                  # Call video playback function

                cam.release()
                cv2.destroyAllWindows()
                return True  # Face recognized successfully

            else:
                speak("verification unsuccessful")
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        if cv2.waitKey(10) & 0xff == 27:  # Press 'ESC' to exit
            break

    cam.release()
    cv2.destroyAllWindows()
    return False  # Face recognition unsuccessful

def start_jarvis_thread():
    jarvis_thread = threading.Thread(target=run_jarvis)
    jarvis_thread.daemon = True
    jarvis_thread.start()

def animate_gif(frame_index):
    global gif_frames, image_label
    
    # Set the current frame in the label
    frame = gif_frames[frame_index]
    image_label.config(image=frame)
    
    # Update the frame index, cycling through the GIF frames
    frame_index = (frame_index + 1) % len(gif_frames)
    
    # Call this function again after 100 milliseconds (adjust as needed for GIF speed)
    root.after(100, animate_gif, frame_index)

def on_run():
    # Start face recognition
    if facerecognition():
        # Face recognized, start Jarvis and GIF
        start_jarvis_thread()
        animate_gif(0)  # Start the GIF animation
        messagebox.showinfo("Jarvis", "Jarvis is now running.")
    else:
        # Face not recognized
        messagebox.showwarning("Verification", "Face verification unsuccessful.")

def on_exit():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Jarvis Assistant")

# Set the size of the window
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Configure the window background color
root.configure(bg='#2C3E50')

# Load the GIF and extract all frames using ImageSequence
gif_image = Image.open("jarvis.gif")  # Ensure the GIF path is correct
gif_frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif_image)]

# Place the GIF in the window using a label at the top
image_label = tk.Label(root, bg='#2C3E50')
image_label.pack(pady=(20, 10))  # Add padding to the top


        # Load and resize images
start_img = Image.open("Start.png")  # Ensure start.png is the correct path to your start button image
start_img = start_img.resize((150, 150), Image.LANCZOS)  # Resize the image as needed
start_photo = ImageTk.PhotoImage(start_img)

quit_img = Image.open("Quit.png")  # Ensure quit.png is the correct path to your quit button image
quit_img = quit_img.resize((150, 150), Image.LANCZOS)  # Resize the image as needed
quit_photo = ImageTk.PhotoImage(quit_img)

# Create and place the buttons with images instead of text in a frame below the GIF
button_frame = tk.Frame(root, bg='#2C3E50')
button_frame.pack(pady=(10, 20))  # Add padding below the GIF

start_button = tk.Button(button_frame, image=start_photo, command=on_run, bg='#2C3E50', relief=tk.FLAT)
start_button.grid(row=0, column=0, padx=20)

quit_button = tk.Button(button_frame, image=quit_photo, command=on_exit, bg='#2C3E50', relief=tk.FLAT)
quit_button.grid(row=0, column=1, padx=20)

# Run the application
root.mainloop()
