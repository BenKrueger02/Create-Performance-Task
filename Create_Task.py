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

def selection_screen():
    global subject_list
    subject_list = ['Math','Language Arts','Science', 'History', 'Language','Other' ]
    global Math
    global Math_Checkbutton
    Math = True
    Math_Checkbutton = Checkbutton(master_3, text = "Math Homework", variable = Math )
    Math_Checkbutton.pack()
    Math_Checkbutton.place()


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
