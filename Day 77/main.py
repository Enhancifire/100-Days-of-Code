import random
import time
from tkinter import Tk, Label, messagebox, Button

win = Tk()
win.geometry("1920x1080")

words_list = [
        "add", "idea", "tell", "play", "sometimes", "there", "night", "answer", "our", "along", "cut", "went", "mean", "than", "watch", "in", "large", "war", "every", "can", "also", "how", "feet", "off", "how", "old", "her", "little", "new", "he", "war", "children", "from", "found", "get", "put", "eat", "form", "get", "tree", "let", "little", "much", "be", "black", "after", "stop", "his", "part", "and", "again", "learn", "white", "group", "learn", "can", "even", "here", "every", "when", "end", "something", "list", "upon", "which", "play", "before", "here", "down", "many", "another", "get", "could", "grow", "really", "does", "big", "learn", "children", "side", "been", "your", "long", "call", "what", "very", "year", "eye", "one", "cut",
        "next", "look", "animal", "without", "out", "after", "form", "now", "began", "before", "small", "still", "begin", "live", "leave", "other", "different", "number", "city", "go", "keep", "write", "near", "set", "with", "more", "fire", "will", "three", "close", "food", "live", "I", "are", "page", "make", "land", "something", "run", "spell", "I", "much", "want", "along", "eat", "get", "some", "way", "its", "on", "down", "such", "was", "our", "different", "line", "food", "let", "ask", "small", "no", "school", "at", "form", "went", "give", "idea", "come", "have", "keep", "year", "really", "on", "ask", "three", "how", "are", "children", "hard", "say", "second", "later", "air", "day", "call", "own", "about", "learn", "under", "go",
        ]

def create_list():
    sentence = [random.choice(words_list) for _ in range(0, 30)]

    sent = " ".join(sentence)
    return sent

def startTimer():
    print("Started")
    for i in range(30, 0, -1):
        print(f"{i} Started")
        timeLabel.config(text= f"{i}")
        time.sleep(1)


timeLabel = Label(text= "Time", font= ("Arial", 20))
timeLabel.grid(column = 1, row = 0)

startButton = Button(
        text = "Start Timer",
        command = startTimer
       )
startButton.grid(column= 1, row = 1)

win.mainloop()
