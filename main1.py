from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_TYPE = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
tick_counter = ""
timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# window setup
window = Tk()
window.title("Rob's Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# background setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(103, 120, text="00:00", fill="white", font=(FONT_TYPE, 30, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def stop_timer():
    global tick_counter
    tick_counter = ""
    title_label.config(text="Press Start", fg=GREEN)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(5 * 60)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(25*60)
        title_label.config(text="Start Work", fg=GREEN)
        global tick_counter
        tick_counter +="✔"
        tick.config(text=tick_counter)


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec % 60 < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# Title text - label
title_label = Label(text="Press Start", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_TYPE, 30, "bold"))
title_label.grid(column=1, row=0)

# start button
start_button = Button(text="Start", bg="white", command=start_timer)
start_button.grid(column=0, row=2)

# reset button
reset_button = Button(text="Reset", bg="white", command=stop_timer)
reset_button.grid(column=2, row=2)

# tick counter - label
tick = Label(text=tick_counter, fg=GREEN, bg=YELLOW, font=(FONT_TYPE, 10, "bold"))
tick.grid(column=1, row=2)



window.mainloop()