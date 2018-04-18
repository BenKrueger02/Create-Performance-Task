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
    if x>=len(flashcard_list_term):
        print("Sorry, you ain't got no more flashcards.")
        x=x-1
    else:
        Word.destroy()
        flashcards()
        flash_sequence()

def flip_command():
    global next_button
    if next_button == True:
        next_button = False
        Word.destroy()
        flashcards()
        flash_sequence()
    else:
        next_button = True
        Word.destroy()
        flashcards()
        flash_sequence()

def flash_sequence():
    flash_buttons()

    if next_button == True:
        global Word
        Word = Label(flashcard_screen, text=flashcard_list_term[x], font=('Bodoni', 50, 'bold'), fg='black', bg='white')
        Word.pack()
        Word.place(x=360, y=400)
        flash_buttons()
    else:
        Word = Label(flashcard_screen, text=flashcard_list_definition[x], font=('Bodoni', 50, 'bold'), fg='black', bg='white')
        Word.pack()
        Word.place(x=360, y=400)
        flash_buttons()




# def flip_flashcard():
#     if flip_word == flashcard_list_term[0]:
#         flip_word = flashcard_list_definition[0]
#     else:
#         flip_word = flashcard_list_term[0]
#     flash_sequence()

next_true = False

def flash_buttons():
    global flashscreen
    next = Button(flashscreen, text="Next", font=('Bodoni', 25, 'bold'), fg='black', bg='White', command= next_command)
    next.pack()
    next.place(x=710, y=750)
    flip = Button(flashscreen, text="Flip", font=('Bodoni', 25, 'bold'), fg='black', bg='White', command = flip_command)
    flip.pack()
    flip.place(x=10, y=750)



def call_flashcards():
    global flashscreen
    global flashcard_screen
    flashscreen = Tk()
    flashcard_screen = Canvas(flashscreen, width=800, height=800, bg='white')
    flashcard_screen.pack()
    questions()
    flashcards()
    flash_sequence()


def flashcards():
    Title_flash = Label(flashscreen, text='Flash Time', font=('Bodoni', 50, 'bold'), fg='blue', bg='white')
    Title_flash.pack()
    Title_flash.place(x=275, y=100)

def call_planner():
    master = Tk()
    planner_screen = Canvas(master, width=800, height=800, bg='white')
    planner_screen.pack()


Title = Label(master, text='Flash Time', font = ('Bodoni', 60, 'bold'), fg='blue', bg='green')
Title.pack()
Title.place(x=255, y=100)


flash_card = Button(master, text="Flashcards", font = ('Bodoni', 25, 'bold'), fg='black', bg='green', command=call_flashcards)
flash_card.pack()
flash_card.place(x=320, y=300)

planner = Button(master, text="Planner", font = ('Bodoni', 25, 'bold'   ), fg='black', bg='green', command = call_planner)
planner.pack()
planner.place(x=340, y=400)













mainloop()
