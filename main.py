import speech_recognition as sr
import pyttsx3 
import webbrowser
import pyaudio
import musicLibrary

recognizer = sr.Recognizer() # Recognizer meri class h


def speak(text):
    engine = pyttsx3.init() # initialize ye sb chrome se liya gya h pyttsx ke syntax se
    engine.say(text)  # pyttsx3 sytax taken from chrome
    engine.runAndWait()

def processcommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open facebook" in c.lower():
      webbrowser.open("https://facebook.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")   
   elif "open chatgpt" in c.lower():
      webbrowser.oper("https://chatgpt.com")
   elif c.lower().startswith("play"):
     songs = c.lower().split(" ")[1]
     link =musicLibrary.music[songs]
     webbrowser.open(link)
if __name__  == "__main__":
  speak("Initializing jarvis....")
# LISTEN FOR THE WAKE WORD JARVIS
  while True:
     r = sr.Recognizer()
     with sr.Microphone() as source:
       

        # recorginising speech using sphinx
        # pip install pocket sphinix

        try :
          print("Listning..")
          audio = r.listen(source,timeout =2 , phrase_time_limit =2 ) # agar 1 sec tak kuch nhi bola to error aaega timeout error
          word = r.recognize_google(audio)
          print(word)
          if (word.lower() == "jarvis"):
             speak("Yah")
      
        # Listen for command
             with sr.Microphone() as source:
               print("Jarvis Active..")
               audio = r.listen(source) 
               comand = r.recognize_google(audio)

               processcommand(comand)

        except Exception as e:
           print("Error ; {0}".format(e))


