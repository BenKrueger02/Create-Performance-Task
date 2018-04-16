from Tkinter import *
import time
master = Tk()

title_screen = Canvas(master, width=800, height=800, bg='green')
title_screen.pack()



def questions():
    global word_count
    global flashcard_list_term
    global flashcard_list_definition
    word_count = input('How many flashcards would you like to make?')
    flashcard_list_term = []
    flashcard_list_definition = []
    for x in range(0,word_count):
        word=input('What is the word you would like?')
        definition=input('What is the definition of the word you chose?')
        flashcard_list_term.append(word)
        flashcard_list_definition.append(definition)
    print('Return back to the other window.')
    print(flashcard_list_term)
    print(flashcard_list_definition)


def next_command():
    global next_true
    next_true = True


def flash_sequence():
    global flip_word
    flip_word = flashcard_list_term[0]
    Word = Label(flashscreen, text=flip_word, font=('Bodoni', 80, 'bold'), fg='black', bg='white')
    Word.pack()
    Word.place(x=360, y=400)

def flip_flashcard():
    if flip_word == flashcard_list_term[0]:
        flip_word = flashcard_list_definition[0]
    else:
        flip_word = flashcard_list_term[0]
    flash_sequence()

next_true = False

def flash_buttons():
    global flashscreen
    next = Button(flashscreen, text="Next", font=('Bodoni', 25, 'bold'), fg='black', bg='White', command= next_command)
    next.pack()
    next.place(x=710, y=750)
    flip = Button(flashscreen, text="Flip", font=('Bodoni', 25, 'bold'), fg='black', bg='White', command= flip_flashcard)
    flip.pack()
    flip.place(x=10, y=750)



def call_flashcards():
    global flashscreen
    flashscreen = Tk()
    flashcard_screen = Canvas(flashscreen, width=800, height=800, bg='white')
    flashcard_screen.pack()
    questions()
    flashcards()
    flash_sequence()
    flash_buttons()

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