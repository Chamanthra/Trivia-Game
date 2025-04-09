##Trivia Game

## Overview

This project consists of two Python programs that together form a Quiz Management System:
1. **admin.py** - A command-line interface for quiz administrators to manage questions
2. **quiz.py** - A GUI-based quiz application for users to take quizzes

The system allows administrators to create, view, search, and delete quiz questions, while users can take randomized quizzes and get scored based on their performance.

## Features

### Admin Program (admin.py)
- **Add questions**: Create new quiz questions with multiple valid answers and difficulty levels
- **List questions**: View all questions with truncated previews
- **Search questions**: Find questions containing specific terms
- **View details**: See full question text, answers, difficulty, and answer statistics
- **Delete questions**: Remove questions from the quiz pool
- **Data persistence**: All changes are saved to `data.txt` in JSON format

### Quiz Program (quiz.py)
- **Randomized quiz**: Selects 5 random questions from the pool
- **Difficulty scoring**: Questions are worth different points based on difficulty
- **Answer validation**: Checks user answers against all valid answers
- **Progress tracking**: Shows current question number and difficulty
- **Score calculation**: Tracks correct answers and calculates final score

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- json module (included with Python)

## Installation

1. Clone or download the repository
2. Ensure both `admin.py` and `quiz.py` are in the same directory
3. Run the programs from the command line:
   - `python admin.py` for the admin interface
   - `python quiz.py` for the quiz interface

## Usage

### Admin Interface
1. Run `admin.py`
2. Choose from the following options:
   - `a` - Add a new question
   - `l` - List all questions
   - `s` - Search questions
   - `v` - View question details
   - `d` - Delete a question
   - `q` - Quit the program

### Quiz Interface
1. Run `quiz.py`
2. The program will automatically:
   - Load questions from `data.txt`
   - Select 5 random questions
   - Present them one by one in a GUI window
3. Type your answer in the text box and click "Submit Answer"
4. After 5 questions, your final score will be displayed

## Data Format

Questions are stored in `data.txt` in JSON format with the following structure:
```json
[
    {
        "question": "Sample question text",
        "answers": ["answer1", "answer2"],
        "difficulty": 1,
        "correct": 0,
        "incorrect": 0
    }
]
