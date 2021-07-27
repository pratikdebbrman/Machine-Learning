#   C:\Users\user\AppData\Local\Programs\Python\Python36\Scripts
#   In the above path install the packages i have tried in python3.7 it does worked bcz speech_recognition doest work in 3.6 or higher versions
#   type cd C:\Users\user\AppData\Local\Programs\Python\Python36\Scripts in cmd
#   then pip install SpeechRecognition
#   then pip install PyAudio

import webbrowser
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say what you want to search on goggle")
    audio = r.listen(source,timeout=5,phrase_time_limit=5)
try:
    print("Opening " + r.recognize_google(audio))
    lib = r.recognize_google(audio)
    url = "https://www.google.co.in/search?q=" +(str(lib))
    webbrowser.open_new(url)
except sr.UnknownValueError:
    print("Your audio is not clear")
