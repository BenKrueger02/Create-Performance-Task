from Tkinter import *

master = Tk()

title_screen = Canvas(master, width=800, height=800, bg='#6960EC')
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


def Finished_command():
    call_flashcards()
    flash_title()
    flash_sequence()

b=0

def return_word(hello):
    global word_input
    global def_input
    global definition
    global Flash_num
    global b
    b=b+1
    if len(term_list) ==0:
        flash_num_label_term = Label(master_flash_input, text='You have 1 flashcard', font=('Bodoni', 25, 'bold'), fg='black', bg='white')
        flash_num_label_term.pack()
        flash_num_label_term.place(x=300, y=500)
    else:
        flash_num_label_term = Label(master_flash_input, text='You have ' + (str(len(term_list)+1)) + ' flashcards', font=('Bodoni', 25, 'bold'), fg='black',bg='white')
        flash_num_label_term.pack()
        flash_num_label_term.place(x=300, y=500)
    word_input = word.get()
    def_input = definition.get()
    word.delete(0, 'end')
    definition.delete(0, 'end')
    term_list.append(word_input)
    definition_list.append(def_input)
    print('hello')
    print(term_list)
    print(definition_list)
    Flash_num = word_count



def OK_command():
    global word_count
    global term_list
    global definition_list
    global word_input
    global word
    global definition
    global def_input

    word_count = flash_num_slider.get()
    print(word_count)
    term_list = []
    definition_list = []

    for x in range(0, word_count):
        word_input = ''
        def_input = ''
        word = Entry(master_flash_input)
        word.pack()
        word.place(x=325, y=300)


        definition = Entry(master_flash_input)
        definition.pack()
        definition.place(x=325, y=400)
        definition.bind('<Return>', return_word)


        instruction_label_enter = Label(master_flash_input, text="Enter the term, then the definiton, then click enter.\n Once you have entered all your flashcards\n click finished.",font=('Bodoni', 25, 'bold'), fg='black', bg='white')
        instruction_label_enter.pack()
        instruction_label_enter.place(x=100, y=50)

        instruction_label_term = Label(master_flash_input,text="Term:",font=('Bodoni', 25, 'bold'), fg='black', bg='white')
        instruction_label_term.pack()
        instruction_label_term.place(x=250, y=295)

        instruction_label_definition = Label(master_flash_input, text="Defintion:", font=('Bodoni', 25, 'bold'), fg='black',bg='white')
        instruction_label_definition.pack()
        instruction_label_definition.place(x=200, y=395)

        OK_button.destroy()
        flash_num_slider.destroy()
        instruction_label.destroy()

    Finished_button = Button(master_flash_input, text="Finished", font=('Bodoni', 25, 'bold'), fg='black', bg='White',command=Finished_command)
    Finished_button.pack()
    Finished_button.place(x=350, y=750)



def create_flashcards():
    global master_flash_input
    global flashcard_input
    global flash_num_slider
    global OK_button
    global instruction_label
    master_flash_input = Tk()
    flashcard_input = Canvas(master_flash_input, width=800, height=800, bg='white')
    flashcard_input.pack()
    instruction_label = Label(master_flash_input, text="Enter the amount of flashcards\n you wish to make!",font=('Bodoni', 25, 'bold'), fg='black', bg='white')
    instruction_label.pack()
    instruction_label.place(x=250, y=50)
    flash_num_slider = 0
    flash_num_slider = Scale(master_flash_input, from_=0, to=50, length=360, tickinterval=10, font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
    flash_num_slider.pack()
    flash_num_slider.place(x=250, y=150)
    OK_button = Button(master_flash_input, text="OK", font=('Bodoni', 25, 'bold'), fg='black', bg='White',command=OK_command)
    OK_button.pack()
    OK_button.place(x=400, y=750)





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
    next_button = Button(master_2, text="Next", font=('Bodoni', 25, 'bold'), fg='black', bg='White', command= next_command)
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
    slider_button_math = Scale(master_3,from_=0, to=110, length = 360, tickinterval = 10, font=('Bodoni', 10, 'bold'), orient = HORIZONTAL)
    slider_button_math.pack()
    slider_button_math.place(x=425, y=height)

    height = height + 110
    slider_button_Language_arts = Scale(master_3, from_=0, to=110, length=360, tickinterval=10, font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
    slider_button_Language_arts.pack()
    slider_button_Language_arts.place(x=425, y=height)

    height = height + 110
    slider_button_science = Scale(master_3, from_=0, to=110, length=360, tickinterval=10, font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
    slider_button_science.pack()
    slider_button_science.place(x=425, y=height)

    height = height + 110
    slider_button_history = Scale(master_3, from_=0, to=110, length=360, tickinterval=10, font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
    slider_button_history.pack()
    slider_button_history.place(x=425, y=height)

    height = height + 110
    slider_button_language = Scale(master_3, from_=0, to=110, length=360, tickinterval=10, font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
    slider_button_language.pack()
    slider_button_language.place(x=425, y=height)

    height = height + 110
    slider_button_other = Scale(master_3, from_=0, to=110, length=360, tickinterval=10, font=('Bodoni', 10, 'bold'), orient=HORIZONTAL)
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
    global time_clock_label_1
    global time_clock_label_2
    global hour1
    global minute1
    global hour2
    global minute2
    global minute_string
    global minute_string_two
    global height
    global minute_string_zero
    height = 110
    minute_string = ''
    minute_string_two = ''
    if minute < 10:
        minute_string_zero = str('0' + str(minute))
        time_clock_label = Label(master_4, text=('Start at: ' + str(hour) + ':' + str(minute_string_zero)), font=('Bodoni', 25, 'bold'), fg='black',bg='white')
        time_clock_label.pack()
        time_clock_label.place(x=550, y=110)
    else:
        time_clock_label = Label(master_4, text=('Start at: ' + str(hour) + ':' + str(minute)),font=('Bodoni', 25, 'bold'), fg='black', bg='white')
        time_clock_label.pack()
        time_clock_label.place(x=550, y=110)
    time_hour = time_for_subjects[0] / 60
    time_minute = time_for_subjects[0] % 60
    hour1 = hour + time_hour
    minute1 = minute + time_minute
    if minute1 >= 60:
        hour1 = hour1 + 1
        minute1 = minute1 - 60
    if minute1 < 10:
        minute_string = str('0' + str(minute1))
        time_clock_label = Label(master_4, text=('Start at: ' + str(hour1) + ':' + str(minute_string)), font=('Bodoni', 25, 'bold'), fg='black', bg='white')
        time_clock_label.pack()
        time_clock_label.place(x=550, y=220)
    else:
        print(str(hour1) + ':'+str(minute1)+' minute1')
        time_clock_label = Label(master_4, text=('Start at: ' + str(hour1) + ':'+str(minute1)), font=('Bodoni', 25, 'bold'), fg='black',bg='white')
        time_clock_label.pack()
        time_clock_label.place(x=550, y=220)

    height=330
    for j in range(1, len(time_for_subjects)-1):

        hour2= time_for_subjects[j]/60
        minute2 = time_for_subjects[j] %60
        print('Hour one is ' + str(hour1))
        print('Hour two is ' + str(hour2))
        hour2 = hour1+hour2
        minute2 = minute2+minute1
        if minute2 >= 60:
            hour2=hour2+1
            minute2 = minute2-60
        if minute2 < 10:
            minute_string_two = ('0' + str(minute2))
            print(str(hour2) + ':' + minute_string_two+ ' minute string 2')
            print(str(hour2) + ':' + str(minute2) + ' minute 2')
            time_clock_label = Label(master_4, text=('Start at: ' + str(hour2) + ':' + str(minute_string_two)),font=('Bodoni', 25, 'bold'), fg='black', bg='white')
            time_clock_label.pack()
            time_clock_label.place(x=550, y=height)
        else:
            print(str(hour2) + ':' + str(minute2)+ ' minute 2')
            time_clock_label = Label(master_4, text=('Start at: ' + str(hour2) + ':' + str(minute2)), font=('Bodoni', 25, 'bold'), fg='black', bg='white')
            time_clock_label.pack()
            time_clock_label.place(x=550, y=height)
            hour1 = hour2
            minute1 = minute2
            height = height+110

    height = 0
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


Title_main = Label(master, text='Homework Planner', font = ('Bodoni', 60, 'bold'), fg='#5CB3FF', bg='#6960EC')
Title_main.pack()
Title_main.place(x=150, y=100)


flashcard_button = Button(master, text="Flashcards", font = ('Bodoni', 25, 'bold'), fg='black', bg='#6960EC', command=create_flashcards)
flashcard_button.pack()
flashcard_button.place(x=320, y=300)

planner_button = Button(master, text="Planner", font = ('Bodoni', 25, 'bold'   ), fg='black', bg='#6960EC', command = call_planner)
planner_button.pack()
planner_button.place(x=340, y=400)



Coders_label = Label(master, text='By: \n Ben Krueger and \n Aidan MacDonell', font = ('Bodoni', 35, 'bold'), fg='#5CB3FF', bg='#6960EC')
Coders_label.pack()
Coders_label.place(x=250, y=500)











mainloop()