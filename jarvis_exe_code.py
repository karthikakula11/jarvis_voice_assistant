from re import S
import pyttsx3 as pyt
import speech_recognition as sr
import datetime
import os
import cv2
import random
import pyautogui
# from welcome_backsir import *  # welcomeback sir animation  code
from requests import get
import requests
from bs4 import BeautifulSoup
import wikipedia
import webbrowser
from pydub import AudioSegment
from pydub.playback import play
import urllib.request
import time
import numpy as np
import subprocess
# from jarvis_intro import *
import winshell # used to clean recycle bin
import sys
import cv2
import speedtest
import numpy as np
import ctypes# to turn the screenoff and on
import win32api, win32con #to turn the screen off and on
# import ffpyplayer
# #ffpyplayer for playing audio
# from ffpyplayer.player import MediaPlayer
import pywhatkit

engine = pyt.init("sapi5")
voices = engine.getProperty("voices")  # voices is a variable
# print(voices)
'''
voice[0] and voice[3]=david voice
voice[1]= microsoft mark voice(better one)'
voice[2] and voice[4]=zira voice'''
engine.setProperty("voice", voices[
    1].id)  # 1st parameter lo voices ani pedthe male voice ye osthadi everytime change it to voice and voices[should be 1 for female 0 for male]
engine.setProperty("rate", 160)  # 2nd parameter sets speed of voice

chose = 0  # for music


# converts text to speech
def speak(audio):
    engine.say(audio)  # says the given audio
    engine.runAndWait()


    # takecommand takes voiceinput from user and converts it to text and displays it on screen (required module=speechrecognition)
def takecommand():
    listener = sr.Recognizer()
    # microphone is source for voice
    with sr.Microphone() as source:
        print("Listening.....")
        listener.pause_threshold = 1
        startsound=AudioSegment.from_wav("start up sound.wav")
        play(startsound)
        voice = listener.listen(source, timeout=15,
                                        phrase_time_limit=5)  # listens user voice from source(microphone)
        # if you dont speak or microphone is off for sometime(5) jarvis will automatically terminate
        endsound=AudioSegment.from_wav("end up sound.wav")
        play(endsound)

    try:
        print("Recognizing...")
        query = listener.recognize_google(voice, language="en-in")  # lang=english-india
        # string madyala variable name iyaniki format strings vadtham

        query = query.lower()  # converts user input to small letters
        print(f"user said:{query}")  # prints what user said

    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        return "none"
    return query

    # to wish
def wishme():
    hour = int(datetime.datetime.now().hour)
    # print(hour)

    if hour >= 0 and hour < 12:
        print("good morning")
        speak("good morning ")
    elif hour >= 12 and hour < 18:
        print("good afternoon")
        speak("good afternoon")
    else:
        print("good evening")
        speak("good evening")
    print("i am jarvis,how can i help you")
    speak("i am jarvis,how can i help you")

if __name__=="__main__":

    while True:
        # userinput will be stored in query var
            query = takecommand()
            query = query.replace("jarvis", "")
            # when ever a person says jarvis how are you this code will help the interpretor to avoid jarvis and listen the words after jarvis word
            # for example if i dont write this code and say jarvis open command prompt then it wont open and says sorry sir i didnt understand
            # with the above code the interpretor will take the open command prompt and and avoid jarvis in beginning

            if "introduce yourself" in query or "tell me about yourself" in query or "jarvis introduce yourself" in query:
                speak("hello,i am jarvis")
        
                # video_path="D:\Jarvis project\jarvis introduction.mp4"
                # def PlayVideo(video_path):
                #     video=cv2.VideoCapture(video_path)
                #     player = MediaPlayer(video_path)
                #     while True:
                #         grabbed, frame=video.read()
                #         audio_frame, val = player.get_frame()
                #         if not grabbed:
                #             print("End of video")
                #             break
                #         if cv2.waitKey(35) & 0xFF == ord("q"):
                #             break

                #             # 0xFF==ord("q") press q to quit from video

                #         cv2.imshow("Video", frame)
                #         if val != 'eof' and audio_frame is not None:
                #             #audio
                #             img, t = audio_frame
                #     video.release()
                #     cv2.destroyAllWindows()
                # PlayVideo(video_path)
            
            elif "clean recycle bin" in query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

            elif "turn off the screen" in query or "turn the screen off" in query or "turn of my screen" in query:
                ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)

            elif "turn on the screen" in query or "turn the screen on" in query or "turn on my screen" in query:
                ctypes.windll.user32.SendMessageW(65535, 274, 61808, -1)
                x, y = (0,0)#mouse
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)#mouse will move and prevent from turning off the screen again

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
                speak("opening camera")
                print("press q to close camera")
                speak("press q to close camera")
                cap = cv2.VideoCapture(0)
                while True:
                    #
                    ret, img = cap.read()
                    cv2.imshow("webcam", img)
                    k = cv2.waitKey(50)
                    if k == ord("q") or k == ord("Q"):  # press q to close camera
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif "close camera" in query:
                pyautogui.hotkey("q")
            
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
                print(info)
                speak(info)


            elif "what is the time" in query or "time" in query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print('Current time is ' + time)
                speak('Current time is ' + time)


            elif "what " in query \
                or "how" in query or "which" in query or "write" in query or "do you" in query:
                import openai
                import speech_recognition as sr
                import pyttsx3

                # OpenAI API key
                openai.api_key = "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"
                #"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"
                #" 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"
                    

                    # Try to recognize the audio
                    

                    # Use OpenAI to create a response
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=query,
                    temperature=0.7,
                    max_tokens=300
                    )

                    # Get the response text
                response_text = str(response['choices'][0]['text']).strip('\n\n')
                print(response_text)

                # Speak the response
                engine.say(response_text)
                engine.runAndWait()
                print()

                

                


            elif "what is the time" in query or "time" in query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print('Current time is ' + time)
                speak('Current time is ' + time)

            elif "change voice to female" in query or "female voice" in query or "change to female voice" in query or "I want female voice"in query:
                engine.setProperty("voice", voices[2].id)  # 1st parameter lo voices ani pedthe male voice ye osthadi everytime change it to voice and voices[should be 1 for female 0 for male]
                engine.setProperty("rate", 175)
                print("From now I will respond to you in female voice")
                speak("From now I will respond to you in female voice")

            elif "change voice to male" in query in query or "male voice " in query or "change to male voice" in query or "I want male voice "in query:
                engine.setProperty("voice", voices[1].id)  # 1st parameter lo voices ani pedthe male voice ye osthadi everytime change it to voice and voices[should be 1 for female 0 for male]
                engine.setProperty("rate", 160)
                print("From now I will respond to you in male voice")
                speak("From now I will respond to you in male voice")

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

            elif "send whatsapp message" in query or "send whatsapp message" in query or \
                            " i want to send a message in whatsapp" in query or "send a whatsapp message" in query \
                            or "whatsaap message" in query:

                contacts = {"mother": "+9196522 61371","mom": "+9196522 61371", "sister": "+919666678143", "teja reddy": "+918499086087",
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
                        time.sleep(4)
                        pyautogui.hotkey("alt","tab")
                        msgloop = False

                    else:
                        speak("please enter from available contacts")
                        msgloop = False
        # set brightness percentage 
            elif "set brighntess level " in query or "set brightness" in query or "set brightness percentage" in query:
                def run(cmd):
                 completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
                 return completed

                if __name__ == '__main__':
                    print("how much brightness percentage should i set ?")
                    speak("how much brightness percentage should i set ?")
                    take_brightness=takecommand()
                    command = "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1," + take_brightness + ")"
                    hello_command = f"Write-Host {command}"
                    hello_info = run(hello_command)
                    speak(f"{take_brightness} brightness percentage set")


    #<--------------------------------LIVE SKETCH USING JARVIS---fac----------------------->
            elif "draw a sketch of me" in query or "draw a live sketch of me" in query or "draw a picture of me" in query or "draw a live sketch" in query:
                    print("Sure, please give me 5 to 10 seconds to draw your sketch" )
                    speak("Sure, please give me 5 to 10 seconds to draw your sketch" )
                    print("to exit from the live sketch diagram press q")
                    speak("to exit from the live sketch diagram press q")
                

                    camera = cv2.VideoCapture(0)

                    while True:
                        ret, frame = camera.read()
                        if ret == False:
                            break
                        # getting width and height of image
                        height, width, _ = frame.shape

                        # creating copy of image using resize function
                        resziedImage = cv2.resize(frame, (width, height),
                                                interpolation=cv2.INTER_AREA)

                        # creating 3X3 kernel, inorder to sharpen the image /frame
                        #kinda unna code thoni manam picture ni sharpen chestanam clarity purpose
                        kernel = np.array([[-1, -1, -1],
                                        [-1, 9, -1],
                                        [-1, -1, -1]])
                        # Appling kernel on the frame using filter2D function .
                        sharpenImage = cv2.filter2D(resziedImage, -1, kernel)

                        # converting image into Grayscale image.
                        gray = cv2.cvtColor(sharpenImage, cv2.COLOR_BGR2GRAY)

                        # creating inverse of sharpen image .
                        inverseImage = 255-gray

                        # applying Gussain Blur on the image .
                        bluredImage = cv2.GaussianBlur(inverseImage, (15, 15), 0, 0)

                        # create a pencilSketch using divide function on opencv .
                        pencilSketch = cv2.divide(gray, 255-bluredImage, scale=256)

                        # show the frame on the screen .
                        #cv.imshow('Sharpen Image', sharpenImage)
                        cv2.imshow("pencilSketch", pencilSketch)

                        cv2.imshow("frame", frame)
                        key = cv2.waitKey(1)
                        if key == ord('q') or key== ord('Q'):
                            break

                    cv2.destroyAllWindows()
                    camera.release()
                    print("You might think the live sketch diagram is not that great. The problem is the laptop camera comes with only 1 megapixel resolution, I cant do anything about it")
                    speak("You might think the live sketch diagram is not that great. The problem is the laptop camera comes with only 1 megapixel resolution, I cant do anything about it")


    # <-----------------playing audio and fun using jarvis------------------------>
            elif "i love you" in query or "friday i love you" in query:
                romeo = AudioSegment.from_wav("nuvemaina romeo.wav")
                play(romeo)
                # from romeodilogue import *

            elif "he died loving but I am not his type" in query or "he died loving" in query:
                cp = AudioSegment.from_wav("chala shekal unnay ra neelo.wav")
                play(cp)
                #from chala_shekal_unnay import *

            elif "jarvis do you love me" in query or "do you love me" in query:
                fs = AudioSegment.from_wav("I Just Want Flirtationship.wav")
                play(fs)
                # from I_just_want_flirtationship import *

            elif "propose me" in query or "propose this lady" in query or "propose this girl" in query or "propose girl" in query or "this girl" in query:
                pd = AudioSegment.from_wav("Malli Malli Idhi Rani Roju.wav")
                play(pd)
                # from propose_dialogue import *

            elif "propose him" in query or "propose this guy" in query:
                mca = AudioSegment.from_wav("mca proposal scene.wav")
                play(mca)
                # from mca_proposal_scene import *

            elif "idiot" in query or "stupid" in query or "waste fellow" in query or "psycho" in query:
                brahmi1 = AudioSegment.from_wav("yendi bro antha mata annav(720P_HD).wav")
                play(brahmi1)
                # from yendi_bro_anthamataannav import *


            elif "i have a pimple" in query or "she has a pimple" in query:
                sp=AudioSegment.from_wav("andamaina premarani.wav")
                play(sp)


            elif "jarvis she loves you" in query or "love you" in query or "she loves you" in query:
                # from devudu_unnadra import *
                karthi1 = AudioSegment.from_wav("Devudu unnadra.wav")
                play(karthi1)

            elif "but as a friend" in query:
                karthi2 = AudioSegment.from_wav("Devudu ledra.wav")
                play(karthi2)

            elif "why should anyone love you" in query or "jarvis why should anyone love you" in query or "jarvis why should i love you" in query:

                orange = AudioSegment.from_wav("nijayithi unnodini.wav")
                play(orange)

            elif "bye jarvis" in query or "bye" in query or "goodbye" in query or "jarvis bye" in query:
                husharu1 = AudioSegment.from_wav("Undiporadhey song.wav")
                play(husharu1)
                # from undiporadhe import *

            elif "jarvis sing a song for me" in query or "jarvis sing a song" in query or "sing a song" in query:
                husharu2 = AudioSegment.from_wav("vere janmantu naake nduku le.wav")
                play(husharu2)
                # from verejanmantu import *



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

            elif "music" in query or "hit some music" in query or "play music" in query:
                chose=0
                print("playing music")
                speak("playing music")
                music_dir_path = "D:\\music"
                songs = os.listdir(music_dir_path)  # converting songs into list
                d = random.choice(songs)  # chooses random music
                os.startfile(os.path.join(music_dir_path, songs[1]))  # plays random music
                chose +=2

            elif "next" in query or "i don't like this " in query \
                            or "next song" in query:
                music_dir_path = "D:\\music"
                songs = os.listdir(music_dir_path)  # converting songs into list
                length = len(songs)
                chose += 2
                if chose >= length:
                    print("no more music to next")
                    speak("no more music to next")
                    print("i'm playing music from starting")
                    speak("i'm playing music from starting")
                    chose = 0
                    os.startfile(os.path.join(music_dir_path, songs[chose]))
                else:
                    os.startfile(os.path.join(music_dir_path, songs[chose]))
                    chose += 2
            
                '''if sir ask why jarvis cant play before files explain in this way manam play or next anna prathi sari oka kotha file ni 
                    open chesi play chesthandi before kuda work avvali ante motham folder ni select chesi play midha click chesthe work aithadi
                    manam windows lo oka file open chesnappudu before song button kodthe same song malla play aithadi
                    next song aane option asal undane undadh'''


            #this code is to play before songs only but wont work(check above statement)
            #this before button will work but u have to comment the random(music) line even though the before button work 
            #it will play some random song becuz chose= value change skips 5 songs every time becyz we kept chose=5
            elif "before song" in query or "repeat" in query or "repeat the song" in query:
                music_dir_path = "D:\\music"
                songs = os.listdir(music_dir_path)  # converting songs into list
                length = len(songs)
                chose += 2
                if chose >= length:
                    print("no more music to next")
                    speak("no more music to next")
                    print("i'm playing music from starting")
                    speak("i'm playing music from starting")
                    chose = 0
                    os.startfile(os.path.join(music_dir_path, songs[chose]))
                else:
                    os.startfile(os.path.join(music_dir_path, songs[chose]))
                    chose -= 1


            elif 'stop' in query or "stop the music" in query or "quit music" in query or "stop music" in query:
                speak('okay')
                print("okay!Now i Stop the music")
                speak("now i stop music")
                # we are writing different music players name hear becuz one one person will have their own wish music players
                # the following codes will work for music players
                os.system('taskkill /F /FI "WINDOWTITLE eq Movies & Tv" ')
                os.system('taskkill /F /FI "WINDOWTITLE eq Groove Music" ')
                os.system('taskkill /F /FI "WINDOWTITLE eq Media Player" ')
                os.system('taskkill /F /FI "WINDOWTITLE eq Windows Media Player" ')
                # os.system('taskkill /F /FI "WINDOWTITLE eq VLC media player" ')




            






            # # <----------------IP ADDRESS(using request module)---------------------->
            # elif "ip address " in query or "what is my ip address" in query or "my ip address" in query:

            #     ip = get("https://api.ipify.org").text  # website gives ip address we are converting it into text
            #     print(f"your ip address is: {ip} ")
            #     speak(f"your ip address is: {ip} ")

            



            


        
    # <-----------------------playing in youtube using pywhatkit------------------------>
            elif "play" in query:
                query = query.replace('play', '')  # empty string replaces play
                # if i say play saranga dariya then system takes only saranga dariya.''(in this empty string saranga dariya will be stored)
                print("Playing" + query)
                speak("Playing" + query)
                pywhatkit.playonyt(query)#yt=youtube
                import time
                # time.sleep(5)# waiting for 3 seconds so that webpage loads and then press f
                time.sleep(30)#waiting for 10 seconds so that no disturbance caused to user
            
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
                time.sleep(2)
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


    #<----------------------------------------------ACCESSING MOBILE CAMERA---------------------------------------------------------->
            elif "open mobile camera" in query or "access mobile camera" in query:
                speak("okay")
                speak("press q to exit from mobile camera")
                # the url will change sometimes check the url in ipwebcam app in mobile
                url = "http://26.118.103.157:8080/shot.jpg"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8)
                    img = cv2.imdecode(img_arr, -1)
                    cv2.imshow("webcam", img)
                    q = cv2.waitKey(1)
                    if q == ord("q") or q== ord("Q"):
                        break
                cv2.destroyAllWindows()






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
