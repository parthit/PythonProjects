from tkinter import *
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    tick_mark.config(text="")
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Short Break', fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_mins = count // 60
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f'0{count_seconds}'
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_seconds}")
    if count>0:
        global timer
        timer = window.after(10, count_down, count-1)
    else:
        start_timer()
        mark = ""
        word_sessions = math.floor(reps/2)
        for _ in range(word_sessions):
            mark += '✔'
        tick_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('pomodoro')
window.config(padx=100, pady=100, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



timer_label = Label(text='Timer')
timer_label.config(fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text='Start')
start_button.config(bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset')
reset_button.config(bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

tick_mark = Label()
tick_mark.config(fg=GREEN, bg=YELLOW)
tick_mark.grid(column=1, row=3)


window.mainloop()