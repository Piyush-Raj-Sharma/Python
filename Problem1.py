
# print(''' 
# Hello from first.py
# This is a simple Python script that prints a greeting message.  
# It is part of a larger project that demonstrates basic Python functionality.
# ''') # triple single quotes for multi-line strings


import pyttsx3 # pyttsx3 is a text-to-speech conversion library in Python
# pip install pyttsx3 to install the library
engine = pyttsx3.init()
engine.say("Hello from first.py")
engine.runAndWait()