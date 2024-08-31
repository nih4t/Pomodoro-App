from tkinter import *
import math
import tkinter.messagebox

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier new"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ""
# Timer Reset

def reset_timer():
    start_button.config(state="normal")
    reset_button.config(state="disabled")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0
    global marks
    marks = ""


# Timer Mechanism

def start_timer():
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
        tkinter.messagebox.showinfo(title="Break", message="Long break!")
        window.focus_force()
    elif reps % 2 == 0:
        window.focus_force()
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
        tkinter.messagebox.showinfo(title="Break", message="Short break!")
        window.focus_force()

    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)
        tkinter.messagebox.showinfo(title="Work", message="Start working~")
        window.focus_force()


# Count Down Mechanism
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global marks
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_mark.config(text=marks)



# UI Setup

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill= "white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)


label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
label.grid(column=1,row=0)

start_button = Button(text="Start", width=8, command=start_timer, state="normal")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=8, command=reset_timer, state="disabled")
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=16)
check_mark.grid(column=1, row=3)

window.mainloop()