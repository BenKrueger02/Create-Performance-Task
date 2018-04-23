from Tkinter import *
import time
master = Tk()

title_screen = Canvas(master, width=800, height=800, bg='green')
title_screen.pack()

global x
x = 0


global next_button
next_button = True


math = False
la = False
science = False
history = False
language = False
other = False

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

def done_command():
    global hour
    global minute
    global schedule_canvas
    global master_4
    master_4 = Tk()
    hour = input('Enter the hour you want to start:')
    if (0 >= hour) or (hour > 12) or (type(hour) != int):
        print('Invalid input. Try again.')
        done_command()
    minute = input('Enter the minute you want to start as a two digit number:')
    if (0 > minute) or (minute > 59) or (type(minute) != int):
        print('Invalid input. Try again.')
        done_command()
    else:
        if minute <10:
            print (str(hour) + ':0' + str(minute))
        else:
            print (str(hour) + ':' + str(minute))
    schedule_canvas = Canvas(master_4, width=800, height=800, bg='white')
    schedule_canvas.pack()
    create_schedule()
    create_planner(subjects_with_hw)
    clock_time(time_for_subjects)



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
    done_button = Button(master_3, text="Done", font=('Bodoni', 25, 'bold'), fg='black', bg='White', command = done_command)
    done_button.pack()
    done_button.place(x=362.5, y=750)


def label_creator_subject(subject_list):
     height = 0
     global subject_label
     for i in subject_list:
         height = height + 110
         subject_label = Label(master_3, text=i, font=('Bodoni', 25, 'bold'), fg = 'black', bg = 'white')
         subject_label.pack()
         subject_label.place(x=15, y=height)

def slider_creator_time():
    height = 0
    global slider_button_math
    global slider_button_Language_arts
    global slider_button_science
    global slider_button_history
    global slider_button_language
    global slider_button_other

    height = height + 110
    slider_button_math = Scale(master_3,from_=0, to=120, length = 360, tickinterval = 10, font=('Bodoni', 10, 'bold'), orient = HORIZONTAL)
    slider_button_math.pack()
    slider_button_math.place(x=425, y=height)

    height = height + 110
    slider_button_Language_arts = Scale(master_3, from_=0, to=120, length=360, tickinterval=10, font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
    slider_button_Language_arts.pack()
    slider_button_Language_arts.place(x=425, y=height)

    height = height + 110
    slider_button_science = Scale(master_3, from_=0, to=120, length=360, tickinterval=10, font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
    slider_button_science.pack()
    slider_button_science.place(x=425, y=height)

    height = height + 110
    slider_button_history = Scale(master_3, from_=0, to=120, length=360, tickinterval=10, font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
    slider_button_history.pack()
    slider_button_history.place(x=425, y=height)

    height = height + 110
    slider_button_language = Scale(master_3, from_=0, to=120, length=360, tickinterval=10, font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
    slider_button_language.pack()
    slider_button_language.place(x=425, y=height)

    height = height + 110
    slider_button_other = Scale(master_3, from_=0, to=120, length=360, tickinterval=10, font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
    slider_button_other.pack()
    slider_button_other.place(x=425, y=height)

def create_schedule():
    global subjects_with_hw
    global time_for_subjects
    subjects_with_hw = []
    time_for_subjects = []
    if slider_button_math.get() > 0:
        print('You have ' + str(slider_button_math.get()) + ' minutes of Math.')
        subjects_with_hw.append('Math')
        time_for_subjects.append(slider_button_math.get())
    if slider_button_Language_arts.get() > 0:
        print('You have ' + str(slider_button_Language_arts.get()) + ' minutes of Language Arts.')
        subjects_with_hw.append('Language Arts')
        time_for_subjects.append(slider_button_Language_arts.get())
    if slider_button_science.get() > 0:
        print('You have ' + str(slider_button_science.get()) + ' minutes of Science.')
        subjects_with_hw.append('Science')
        time_for_subjects.append(slider_button_science.get())
    if slider_button_history.get() > 0:
        print('You have ' + str(slider_button_history.get()) + ' minutes of History.')
        subjects_with_hw.append('History')
        time_for_subjects.append(slider_button_history.get())
    if slider_button_language.get() > 0:
        print('You have ' + str(slider_button_language.get()) + ' minutes of Language.')
        subjects_with_hw.append('Language')
        time_for_subjects.append(slider_button_language.get())
    if slider_button_other.get() > 0:
        print('You have ' + str(slider_button_other.get()) + ' minutes of Somthing else.')
        subjects_with_hw.append('Other')
        time_for_subjects.append(slider_button_other.get())

    print(subjects_with_hw)
    print(time_for_subjects)

def clock_time(time_for_subjects):
    global time
    global time_label
    global time_hour
    global time_minute
    global time_clock_label
    height = 0
    time_clock_label = Label(master_4, text=hour + minute, font=('Bodoni', 25, 'bold'), fg='black', bg='white')
    time_clock_label.pack()
    time_clock_label.place(x=400, y=110)

  #  for x in range(0, len(time_for_subjects)):
   #     time_hour = time_for_subjects[x]/60
    #    time_minute = time_for_subjects[x]%60


    for i in range(0,len(time_for_subjects)):
        height = height +110
        time = time_for_subjects[i]
        time_label = Label(master_4, text=(str(time) + ' minutes'), font=('Bodoni', 25, 'bold'), fg='black', bg='white')
        time_label.pack()
        time_label.place(x=350, y=height)


def selection_screen():
    global subject_list
    global call_back_list
    subject_list = ['Math','Language Arts', 'Science', 'History', 'Language','Other']
    label_creator_subject(subject_list)
    slider_creator_time()
    planner_title()
    done_button()

def create_planner(subjects_with_hw):
    planner_label = Label(master_4, text='Schedule', font=('Bodoni', 60, 'bold'), fg='black', bg='white')
    planner_label.pack()
    planner_label.place(x=255, y = 10)
    height = 0
    for x in subjects_with_hw:
        height = height + 110
        schedule_label = Label(master_4, text=x, font=('Bodoni', 25, 'bold'), fg='black', bg='white')
        schedule_label.pack()
        schedule_label.place(x=15, y=height)


def call_planner():
    global master_3
    global planner_canvas
    global math_time
    master_3 = Tk()
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
