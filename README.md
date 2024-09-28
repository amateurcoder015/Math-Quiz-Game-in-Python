# Math-Quiz-Game-in-Python

Overview
This Python project is a simple Math Quiz Game that challenges the player with randomly generated arithmetic problems of varying difficulty levels. Players can choose from four difficulty levels (Easy, Intermediate, Hard, and Hell), and the game tracks their personal best completion times for each mode. The player's goal is to answer 10 questions correctly, and the game provides feedback on whether the answer is correct or not.

Features
Four difficulty levels:
Easy (numbers between 1-10)
Intermediate (numbers between 10-20)
Hard (numbers between 20-50)
Hell (numbers between 50-100)
Randomized questions: The game generates random math questions involving addition, subtraction, multiplication, and division.
Answer validation: Players must provide the correct answer before moving to the next question. Answers can be given either as a whole number or rounded to one decimal place.
Time tracking: The game records the time taken to complete all 10 questions, and it saves the player's personal best time for each difficulty level in a text file (pb_math.txt).
Persistent high score: The personal best times for each difficulty level are saved in a text file and compared against the player's latest performance.

How it Works
Game Start: The player is prompted to choose a difficulty level. Once selected, the game starts, and a timer begins to track the player's total time.
Question Generation: The game presents a series of 10 math questions, where each question consists of a randomly chosen operator (+, -, *, /) and two randomly generated numbers depending on the difficulty level.
Answer Input: The player must input the correct answer. If the answer is correct, the game moves to the next question. If incorrect, the player is prompted to try again.
Personal Best Tracking: After completing all 10 questions, the total time is calculated. The game compares this time with the personal best stored in the text file. If the new time is faster, it updates the personal best.
Modes: Each difficulty mode has its own set of personal best times tracked in the file.
