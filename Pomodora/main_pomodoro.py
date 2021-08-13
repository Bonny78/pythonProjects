import math
import tkinter
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)  # after_cancel stops the timer
    #change timer label to Timer
    timer_label.config(text="Timer")
    #reseting the timer_text
    canvas.itemconfig(timer_text, text="00:00")  #for canvas use canvas.itemconfig
    #reset check mark
    mark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec =LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps %2 ==0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps %2 ==1:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:  # Dynamic Typing used
        count_sec= "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=F"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)  #this sets the timer
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        mark_label.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# create canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# add image
tomato_img = PhotoImage(file="tomato.png")  # class comes from tkinter, a way to read through a file
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# create Timer label
timer_label = tkinter.Label(text="Timer", font=("Arial", 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# create check mark label
mark_label = tkinter.Label(font=("Arial", 15, "bold"), fg=GREEN)
mark_label.grid(column=1, row=3)

# start button
start_button = Button(text="start", command=start_timer)
start_button.grid(column=0, row=2)

# reset Button
reset_button = Button(text="reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
