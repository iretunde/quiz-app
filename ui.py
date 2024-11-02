#Final issue - if button is clicked multiple times

from tkinter import *
THEME_COLOR = "#375362"
GREEN = '#00FF00'
RED = '#FF0000'
WHITE = '#FFFFFF'
import html

class QuizInterface:

    def __init__(self, question_list):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20)
        self.window.minsize(width=350, height=480)
        self.score = 0

        self.question_list = question_list

        self.label = Label(text=f'Score: {self.score}', font=('Arial', 12), bg=THEME_COLOR, fg='#FFFFFF')
        self.label.place(x=220, y=30)


        self.canvas = Canvas(width=300, height=250, bg=WHITE)
        self.canvas.place(x=10, y=75)

        self.question_number = 0
        self.question = self.canvas.create_text(140, 50, text=f'{self.add_line_breaks(self.current_question())}', font=('Arial', 8), fill='black')

        self.true_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.right_button)
        self.true_button.place(x=30, y=360)

        self.wrong_image = PhotoImage(file='./images/false.png')
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, command=self.false_button)
        self.wrong_button.place(x=190, y=360)
        self.window.mainloop()


    def current_question(self):
        return html.unescape(self.question_list[self.question_number].text)

    def right_button(self):

        correct_answer = self.question_list[self.question_number].answer
        if correct_answer == 'True':
            self.score += 1
            self.label.config(text=f'Score: {self.score}')
            self.canvas.itemconfig(self.question, text='You were correct!')
            self.canvas.configure(bg=GREEN)

        else:
            self.canvas.itemconfig(self.question, text='You were wrong!')
            self.canvas.configure(bg=RED)


        if self.question_number == len(self.question_list) - 1:
            self.window.after(2000, self.do_something)
            self.window.after(4000, self.next_question)
        else:
            self.question_number += 1
            self.window.after(2000, self.next_question)



    def next_question(self):
        self.canvas.itemconfig(self.question,
                               text=f'{self.add_line_breaks(self.current_question())}')
        self.canvas.config(bg=WHITE)


    def false_button(self):
        correct_answer = self.question_list[self.question_number].answer
        if correct_answer == 'False':
            self.score += 1
            self.label.config(text=f'Score: {self.score}')
            self.canvas.itemconfig(self.question, text='You were correct!')
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.itemconfig(self.question, text='You were wrong!')
            self.canvas.config(bg=RED)

        if self.question_number == len(self.question_list) - 1:
            self.window.after(2000, self.do_something)
            self.window.after(4000, self.next_question)
        else:
            self.question_number += 1
            self.window.after(2000, self.next_question)

    def add_line_breaks(self, text):
        temp_lines = text.split()
        lines = []
        line = ''
        for word in temp_lines:
            if len(line) < 50:
                line += word+' '
            else:
                lines.append(line)
                line = ''
        if len(line) != 0:
            lines.append(line)

        return '\n'.join(lines)

    def do_something(self):
        self.question_number = 0
        self.score = 0
        self.label.config(text=f'Score: {self.score}')
        self.canvas.itemconfig(self.question, text='All the questions are finished.\nThe quiz will restart')
