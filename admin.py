# Name:  G.G.A.Chamanthra.C.Gurulumulla
# Student Number:  10664500

# This file is provided to you as a starting point for the "admin.py" program of the Project
# of Programming Principles in Semester 1, 2024.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis of your work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the necessary module(s).
import json
import textwrap


# This function repeatedly prompts for input until an integer between 1 and max_value is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt, max_value):
    while True:
        try:
            number = int(input(prompt))
            if 1 <= number <= max_value:
                return number 
            else:
                print(f"The integer entered is not in the range. Enter a value between 1 and {max_value}")
        except ValueError:
            print('The input you entered is not valid. Integer is required.')


# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    while True:
        text = input(prompt).strip()  
        if text:
            return text 
        else:
            print('Input cannot be empty. Please enter a valid input.')
   

# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data):
        file= open('data.txt', 'w') 
        json.dump(data, file, indent=4)
        file.close()
    

# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.

try:
    file = open('data.txt', 'r') 
    data = json.load(file)
    file.close()
except FileNotFoundError:
    data = []


# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.

print('Welcome to the Quiz Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower() 
        
    if choice == 'a':
        # Add a new question.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        question = input_something('Enter the question: ')
        answers = []
        while True:
            answer = input_something('Enter a valid answer (enter "q" when done): ').lower()
            if answer == 'q':
                break
            else:
                answers.append(answer)
                
        difficulty = input_int('Enter question difficulty (1-3): ', 3)
        print('Question added!')
        new_question = {
            "question": question,
            "answers": answers,
            "difficulty": difficulty,
            "correct": 0,
            "incorrect": 0
        }
        data.append(new_question)
        save_data(data)

    
    elif choice == 'l':
        # List the current questions.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        print('Current questions:')
        #If there is no questions in the file .
        if not data:
            print('No questions saved.')
        else:
            for index, question_data in enumerate(data, start=1):
                truncate_question = textwrap.shorten(question_data['question'], width=50, placeholder='...') # if the question is longer than 50 .
                print(f"{index}) {truncate_question}")


    elif choice == 's':
        # Search the current questions.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        term = input_something('Enter a search term: ')
        #If there is not questions in the file .
        if not data:
            print('No questions saved.')
        else:
            found_term = False
            for index, question_data in enumerate(data, start=1):
                if term.lower() in question_data['question'].lower():
                    truncate_question = textwrap.shorten(question_data['question'], width=50, placeholder='...') # if the question is longer than 50.
                    print(f"{index}) {truncate_question}")
                    found_term = True
            # if the searching term is not found.
            if not found_term:
                print('No result found.')


    elif choice == 'v':
        # View a question.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print('No questions saved.')
        else:
            index = input_int('Question number to view: ', len(data))
            question_data = data[index - 1]
            print('Question:')
            print(question_data['question'])
            if len(question_data['answers']) == 1:
                print('Correct answer:', question_data['answers'][0])
            else:
                print('Valid answers:', ', '.join(question_data['answers'])) # displaying the answers as string separated by ','.
            
            difficulty_labels = ['Easy', 'Medium', 'Hard']
            difficulty_value = question_data['difficulty']
            difficulty_label = difficulty_labels[difficulty_value - 1]

            print(f"Difficulty: {difficulty_value} [{difficulty_label}]")
            print(f"Correctly answered {question_data['correct']} time(s)")
            print(f"Incorrectly answered {question_data['incorrect']} time(s)")


    elif choice == 'd':
        # Delete a question.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print('No questions saved.')
        else:
            index = input_int('Question number to delete: ', len(data))
            del data[index - 1]
            print('Question deleted.')
            save_data(data)

    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        print('Goodbye!')
        break


    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        print('Invalid choice')

# If you have been paid to write this program, please delete this comment.
