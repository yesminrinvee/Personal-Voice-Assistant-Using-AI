import sys
import webbrowser

import speech_recognition as sr
import pyttsx3
# import pyjokes
import os
import datetime
# import wikipedia
import multiprocessing
import playsound
from gtts import gTTS


def talk(words):
    if words != '':
        tts = gTTS(words, lang='en')
        filename = 'voice.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

