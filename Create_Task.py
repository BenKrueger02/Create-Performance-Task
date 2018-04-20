from Tkinter import *
import time
master = Tk()

title_screen = Canvas(master, width=800, height=800, bg='green')
title_screen.pack()

global x
x = 0


global next_button
next_button = True

def questions():
    global word_count
    global term_list
    global definition_list
    word_count = input('How many flashcards would you like to make?')
    term_list = []
    definition_list = []
    for x in range(0,word_count):
        word=input('What is the word you would like?')
        definition=input('What is the definition of the word you chose?')
        term_list.append(word)
        definition_list.append(definition)
    print('Return back to the other window.')
    print(term_list)
    print(definition_list)


def next_command():
    global x
    global next_button
    next_button = True
    x=x+1
    if x>=len(term_list):
        print("Sorry, you ain't got no more flashcards.")
        x=x-1
    else:
        Word.destroy()
        flash_title()
        flash_sequence()

def flip_command():
    global next_button
    if next_button == True:
        next_button = False
        Word.destroy()


        flash_title()
        flash_sequence()
    else:
        next_button = True
        Word.destroy()
        flash_title()
        flash_sequence()

def flash_sequence():
    flash_buttons()

    if next_button == True:
        global Word
        Word = Label(flashcard_canvas, text=term_list[x], font=('Bodoni', 50, 'bold'), fg='black', bg='white')
        Word.pack()
        Word.place(x=210, y=400)
        flash_buttons()
    else:
        Word = Label(flashcard_canvas, text=definition_list[x], font=('Bodoni', 50, 'bold'), fg='black', bg='white')
        Word.pack()
        Word.place(x=210, y=400)
        flash_buttons()





next_true = False

def flash_buttons():
    global master_2
    next_button = Button(master_2, text="next", font=('Bodoni', 25, 'bold'), fg='black', bg='White', command= next_command)
    next_button.pack()
    next_button.place(x=710, y=750)
    flip_button = Button(master_2, text="Flip", font=('Bodoni', 25, 'bold'), fg='black', bg='White', command = flip_command)
    flip_button.pack()
    flip_button.place(x=10, y=750)



def call_flashcards():
    global master_2
    global flashcard_canvas
    master_2 = Tk()
    flashcard_canvas = Canvas(master_2, width=800, height=800, bg='white')
    flashcard_canvas.pack()
    questions()
    flash_title()
    flash_sequence()


def flash_title():
    Title_flash = Label(master_2, text='Flash Time', font=('Bodoni', 50, 'bold'), fg='blue', bg='white')
    Title_flash.pack()
    Title_flash.place(x=275, y=100)

def planner_title():
    Title_planner = Label(master_3, text='How much time will\n you spend on each subject?', font=('Bodoni', 35, 'bold'), fg='black', bg='white')
    Title_planner.pack()
    Title_planner.place(x=160, y=10)

def done_button():
    done_button = Button(master_3, text="Done", font=('Bodoni', 25, 'bold'), fg='black', bg='White')
    done_button.pack()
    done_button.place(x=362.5, y=750)

def button_creator_subject(subject_list):
    height = 0
    global subject_button
    for i in subject_list:
        height = height + 110
        subject_button = Checkbutton(master_3, text=i, font=('Bodoni', 50, 'bold'))
        subject_button.pack()
        subject_button.place(x=15, y=height)

def slider_creator_time():
    height = 0
    global slider_button
    for i in range(0,6):
        height = height + 110
        slider_button = Scale(master_3,from_=0, to=120, length = 360, tickinterval = 10, font=('Bodoni', 10, 'bold'), orient = HORIZONTAL)
        slider_button.pack()
        slider_button.place(x=425, y=height)

        slider.get(i)


def selection_screen():
    global subject_list
    subject_list = ['Math','Language Arts', 'Science', 'History', 'Language','Other' ]
    button_creator_subject(subject_list)
    slider_creator_time()
    planner_title()
    done_button()




def call_planner():
    global master_3
    global planner_canvas
    master_3= Tk()
    planner_canvas = Canvas(master_3, width=800, height=800, bg='white')
    planner_canvas.pack()
    selection_screen()


Title_main = Label(master, text='Homework Planner', font = ('Bodoni', 60, 'bold'), fg='blue', bg='green')
Title_main.pack()
Title_main.place(x=255, y=100)


flashcard_button = Button(master, text="Flashcards", font = ('Bodoni', 25, 'bold'), fg='black', bg='green', command=call_flashcards)
flashcard_button.pack()
flashcard_button.place(x=320, y=300)

planner_button = Button(master, text="Planner", font = ('Bodoni', 25, 'bold'   ), fg='black', bg='green', command = call_planner)
planner_button.pack()
planner_button.place(x=340, y=400)













mainloop()