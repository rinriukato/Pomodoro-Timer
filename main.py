from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMAGE_FILEPATH = "tomato.png"
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224
CENTER_X = CANVAS_WIDTH / 2
CENTER_Y = CANVAS_HEIGHT / 2
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)

    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"0:00")
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_secs)
        timer_label.config(text="Work Time!", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break Time!", fg=RED)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Short Break Time!", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer

    if count >= 0:
        minutes = floor(count / 60)
        seconds = count % 60
        if seconds < 10:
            seconds = f"0{seconds}"

        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # Add a checkmark for every 2 reps (Completed a work session)
        if reps % 2 == 0:
            checks = ""
            for x in range(floor(reps / 2)):
                checks += "✓"
            check_mark.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=1)

canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file=IMAGE_FILEPATH)
canvas.create_image(CENTER_X, CENTER_Y, image=tomato_image)  # X,Y ARE POSITIONAL ARGS ONLY
canvas.grid(column=1, row=2)
timer_text = canvas.create_text(CENTER_X, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), command=reset_timer)
reset_button.grid(column=2, row=3)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=4)


window.mainloop()
