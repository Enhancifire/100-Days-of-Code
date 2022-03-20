import os
from tkinter import *
import time
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✓"
reps = 0
tickm = TICK
my_timer = NONE

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(my_timer)
    global reps, tickm
    reps = 0
    tickm = TICK
    TIMER.config(text="TIMER", fg=GREEN)
    tickmark.config(text=tickm)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():

    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        countdown(long_break_sec)
        TIMER.config(text="LONG BREAK", fg=PINK)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        TIMER.config(text="SHORT BREAK", fg=RED)

    else:
        countdown(work_sec)
        if reps % 2 == 1 and reps != 1:
            global tickm
            tickm += TICK
            tickmark.config(text=tickm)
            TIMER.config(text="TIMER")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        sec = "00"

    elif count_sec > 0 and count_sec < 10:
        sec = f"0{count_sec}"

    else:
        sec = count_sec

    if count_min == 0:
        min = "00"

    elif count_min > 0 and count_min < 10:
        min = f"0{count_min}"

    else:
        min = count_min

    rem_time = f"{min}:{sec}"

    canvas.itemconfig(timer_text, text=rem_time)
    if count > 0:
        global my_timer
        my_timer = window.after(1000, countdown, count - 1)

    else:
        start()
cases = int(input())

caseList = [int(input()) for _ in range(0, cases)]
caseList = [((case - 6) // 7) + 1 for case in caseList]
for case in caseList:
    print(case)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


# Timer Title
TIMER = Label(text="TIMER", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
TIMER.grid(column=1, row=0)


# Start Button
start_but = Button(text="Start", command=start)
start_but.grid(column=0, row=2)

reset_but = Button(text="Reset", command=reset)
reset_but.grid(column=2, row=2)

# Tick Section

tickmark = Label(text=tickm, font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
tickmark.grid(column=1, row=3)

# Canvas Section
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file=os.path.join("Day 26","tomato.png"))
tomato_img = canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))


canvas.grid(column=1, row=1)


window.mainloop()
