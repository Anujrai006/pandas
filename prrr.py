import pyttsx3
import time
engine=pyttsx3.init()
with open("music.txt","r") as f:
    for line in f:
        line=f.readlines()
        for i in range(len(line)):
            engine.say(line[i])
            engine.runAndWait()
            time.sleep(0.3)