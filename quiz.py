

# This file is provided to you as a starting point for the "quiz.py" program of the Project
# of Programming Principles in Semester 1, 2024.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis of your work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the necessary module(s).
import tkinter, tkinter.messagebox, random, json


class ProgramGUI:
#define the constructure .
    def __init__(self):
        pass
        try:
            file = open('data.txt', 'r')
            self.data = json.load(file)
            file.close()
        except FileNotFoundError:
            tkinter.messagebox.showerror('Missing file')
            return
        except ValueError:
            tkinter.messagebox.showerror('Invalid file')
            return

#If the question list in the file is less than 5 .
        if len(self.data) < 5:
            tkinter.messagebox.showerror('Insufficient number of questions')
            return

# Generate attributes .

        self.current_question_number = 0
        self.questions = random.sample(self.data, 5)
        self.correct_number_answers = 0
        self.question_difficulty = ['easy', 'medium', 'hard']
        self.total_score = 0
        
        self.main = tkinter.Tk()
        self.main.title('Trivia Game Quiz')
        self.main.geometry('450x200')

        # create a frame named "question".
        self.question_frame = tkinter.Frame(self.main)

        # Creating widgets to display the question number,question and the difficulty .

        self.progress_message = tkinter.Label(self.question_frame, text='')
        self.question_message = tkinter.Label(self.question_frame, text='')
        self.difficulty_message = tkinter.Label(self.question_frame, text='', fg='blue',pady=5)
        
        # Packing the widgets . 

        self.progress_message.pack()
        self.question_message.pack(fill='x')
        self.difficulty_message.pack()

        # Creating widgets of submit button and the entry tab to prompt the user for input .

        self.answer_entry = tkinter.Entry(self.question_frame, width=35)
        self.submit_button = tkinter.Button(self.question_frame, text='Submit Answer', command=self.check_answer)

        # Packing the widgets .

        self.answer_entry.pack(side='left')
        self.submit_button.pack(side='left')
        
        # Packing the frame.
        self.question_frame.pack()

        
        self.show_question()
        tkinter.mainloop()

    def show_question(self):
        # This method is responsible for displaying the current question and some other messages in the GUI.
        # See Point 1 of the "Methods in the GUI class of quiz.py" section of the assignment brief.
        pass
        self.answer_entry.delete(0, tkinter.END)
        self.answer_entry.focus_set()

        current_question = self.questions[self.current_question_number]

        progress_message = f"Question {self.current_question_number + 1} of 5"
        self.progress_message.configure(text=progress_message)

        self.question_message.configure(text=current_question['question'])

        difficulty_message = f"This one's an {self.question_difficulty[current_question['difficulty'] - 1]} question!"
        self.difficulty_message.configure(text=difficulty_message)
     
        
    def check_answer(self):   
        # This method is responsible for checking if the user's answer is correct and recording that information in "data.txt".
        # See Point 2 of the "Methods in the GUI class of quiz.py" section of the assignment brief.
        pass
        submit_answer = self.answer_entry.get().strip().lower()
        
        #If  a answer is not entered.
        if not submit_answer:
            tkinter.messagebox.showerror('Error', 'You have not entered an answer.')
            return
        
        current_question = self.questions[self.current_question_number]
        correct_answers = current_question['answers']  

        #If the answer submitted is correct .    
        if submit_answer in correct_answers:
            self.correct_number_answers += 1
            self.total_score += current_question['difficulty']
            tkinter.messagebox.showinfo('Correct!', 'You are correct!')
            current_question['correct'] = current_question.get('correct', 0) + 1   #Increment the correct times for the question by 1.
        else:
            tkinter.messagebox.showerror('Incorrect!', 'Sorry, that was incorrect!')
            current_question['incorrect'] = current_question.get('incorrect', 0) + 1  #Increment the incorrect times  for the question in the data.txt file by 1.
 
        
 
        # Changing the incorrect and correct data in the json file data.txt
        file=open('data.txt','w')
        json.dump(self.data,file)
        file.close()

        if self.current_question_number==4 :
           # To calculate the maximum score of the game . 
            self.max_score = sum(question['difficulty'] for question in self.questions )
  
            # Displaying game over message with the score of the user.
            tkinter.messagebox.showinfo('Game Over', f"Game Over! Your score:  {self.total_score} out of {self.max_score}") 
            self.main.destroy()

        else:
            self.current_question_number +=1
            self.show_question()

# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()


# If you have been paid to write this program, please delete this comment.
