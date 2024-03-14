from tkinter import *
import random

BACKGROUND_COLOR = '#EBE3D5'
FONT = 'Courier'
window = Tk()
window.minsize(height=300, width=1000)
window.config(pady=50, padx=100, background=BACKGROUND_COLOR)
window.resizable(height=False, width=False)
window.title('Typing Speed Tester')
time = 60


def update_text_field(event):
    global testing_paragraph, word_count
    entry_texts = type_entry.get(1.0, "end-1c")
    entry_words = entry_texts.split()
    para = testing_paragraph.strip().split()
    word_count = 0
    for word in entry_words:
        if word in para:
            para = [('-' * len(w)) if w == word else w for w in para]
            word_count += 1
    updated_para = " ".join(para)
    paragraph.delete("1.0", END)
    paragraph.insert(END, updated_para)


def show_count():
    global word_count
    try:
        label.config(text=f'Your typing Speed is {word_count} WPM!\n {motivation_select}', bg='#EED3D9')
    except NameError:
        label.config(text='AFK?!\n Try Again!', bg='#C9D7DD')
    word_count = 0


def reset_entry_text():
    type_entry.delete("1.0", END)


def reset():
    global time
    reset_entry_text()
    label.config(text='Start typing clicking start button', bg='#9DBC98')
    paragraph.delete("1.0", END)
    type_entry.unbind("<Key>")
    try:
        window.after_cancel(timer_id)
    except NameError:
        label.config(text='Start typing clicking start button', bg='#9DBC98')
    canvas.itemconfig(canvas_time, text='00:00', fill='#BF3131')
    time = 60


def start():
    global testing_paragraph, motivation_select
    motivation = ['Keep Practicing 💪', 'Well Done 😎', 'You Can Do Better 😎', 'Do Not Give Up 💪']
    motivation_select = random.choice(motivation)
    paragraph.delete("1.0", END)

    filename = f'text{random.randint(1, 5)}.txt'
    with open(filename) as test:
        testing_paragraph = test.read()
    type_entry.bind("<Key>", update_text_field)
    reset_entry_text()
    label.config(text='...', bg='#9DBC98')
    paragraph.insert(END, testing_paragraph)
    timer()


def timer():
    global time, timer_id
    if time >= 0:

        timer_id = window.after(1000, timer)
        canvas.itemconfig(canvas_time, text=f'00:{time:02}', fill='green')
        time -= 1
    else:
        canvas.itemconfig(canvas_time, text='00:00', fill='#BF3131')
        window.after_cancel(timer_id)
        show_count()
        reset_entry_text()
        time = 60


quote = Label(text="Strengthen your hands like Popeye's by practicing typing consistently!", font=(FONT, 14, 'bold'))
quote.grid(row=0, column=2)

canvas = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file='canvas_photo.png')
canvas.create_image(100, 130, image=image)
canvas_time = canvas.create_text(100, 45, text='00:00', fill='#BF3131', font=(FONT, 30, 'bold'))
canvas.grid(row=1, column=2)

paragraph = Text(window, wrap=WORD, height=5, width=90, background='#DED0B6', font=(FONT, 11, 'bold'))
paragraph.insert("1.0", 'Your paragraph will appear here...')
paragraph.grid(column=2, row=2)

type_entry = Text(window, wrap=WORD, height=5, width=90, background='#F3EEEA')
type_entry.insert('1.0', "Start typing here...")
type_entry.grid(column=2, row=4)

label = Label(text='Start typing clicking start button', font=(FONT, 14, 'bold'), bg='#9DBC98')
label.grid(column=2, row=3)

start_button = Button(text='Start', command=start, bg='#9DBC98', highlightthickness=0)
start_button.grid(column=1, row=4)

reset_button = Button(text='Reset', command=reset, bg='#C9D7DD', highlightthickness=0)
reset_button.grid(column=3, row=4)


window.mainloop()
