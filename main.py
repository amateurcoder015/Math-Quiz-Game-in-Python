import random 
import time
OPERATORS = ['+', '-', '*', '/']



def question_easy():
    begin = input('would you like to begin playing (y/n)?')
    if begin == 'y':
        start_time = time.time()
        for _ in range(0,10):
            number1 = random.randint(1,10)
            number2 = random.randint(1,10)
            op = random.choice(OPERATORS)
            ans = eval(str(number1)+ op + str(number2))
            while True:
                user_ans = input("question#"+str(_+1)+": "+ str(number1)+ op + str(number2) + " = ")
                if str(user_ans)==str(round(ans,ndigits=1)) or str(user_ans)==str(round(ans)):
                    print("Correct!")
                    break
        end_time = time.time()
        total_time = end_time - start_time
#         f = open("pb_math.txt", "a")
#         f.write('''1000
# 1000
# 1000
# 1000''')
#         f.close()

        with open('pb_math.txt', 'r') as f:
            lines = f.readlines()
        if float(lines[0]) >total_time:
            with open('pb_math.txt', 'w') as f:
                lines[0]= f.write(str(total_time))


        print(round(total_time,ndigits=2), 'your personal best time for this mode is ', lines[0])
        
    else:
        print("I pray that you dont fail your math test")


def question_intermediate():
    begin = input('would you like to begin playing (y/n)?')
    if begin == 'y': 
        start_time = time.time()
        for _ in range(0,10):
            number1 = random.randint(10,20)
            number2 = random.randint(10,20)
            op = random.choice(OPERATORS)
            ans = eval(str(number1)+ op + str(number2))
            while True:
                user_ans = input("question#"+str(_+1)+": "+ str(number1)+ op + str(number2) + " = ")
                if str(user_ans)==str(round(ans,ndigits=1)) or str(user_ans)==str(round(ans)):
                    print("Correct!")
                    break
        end_time = time.time()
        total_time = end_time - start_time

        with open('pb_math.txt', 'r') as f:
            lines = f.readlines()
            print(lines)
        if float(lines[0]) >total_time:
            with open('pb_math.txt', 'w') as f:
                lines[0]= f.write(str(total_time))
        print(round(total_time,ndigits=2), 'your personal best time for this mode is ', lines[1])

    else:
        print("I pray that you dont fail your math test")

def question_hard():
    begin = input('would you like to begin playing (y/n)?')
    if begin == 'y':
        start_time = time.time() 
        for _ in range(20,50):
            number1 = random.randint(20,50)
            number2 = random.randint(20,50)
            op = random.choice(OPERATORS)
            ans = eval(str(number1)+ op + str(number2))
            while True:
                user_ans = input("question#"+str(_+1)+": "+ str(number1)+ op + str(number2) + " = ")
                if str(user_ans)==str(round(ans,ndigits=1)) or str(user_ans)==str(round(ans)):
                    print("Correct!")
                    break
        end_time = time.time()
        total_time = end_time - start_time
        with open('pb_math.txt', 'r') as f:
            lines = f.readlines()
            print(lines)
        if float(lines[0]) >total_time:
            with open('pb_math.txt', 'w') as f:
                lines[0]= f.write(str(total_time))
        print(round(total_time,ndigits=2), 'your personal best time for this mode is ', lines[2])
    else:
        print("I pray that you dont fail your math test")



def question_hell():
    begin = input('would you like to begin playing (y/n)?')
    if begin == 'y':
        start_time = time.time() 
        for _ in range(0,10):
            number1 = random.randint(50,100)
            number2 = random.randint(50,100)
            op = random.choice(OPERATORS)
            ans = eval(str(number1)+ op + str(number2))
            while True:
                user_ans = input("question#"+str(_+1)+": "+ str(number1)+ op + str(number2) + " = ")
                if str(user_ans)==str(round(ans,ndigits=1)) or str(user_ans)==str(round(ans)):
                    print("Correct!")
                    break
        end_time = time.time()
        total_time = end_time - start_time

        with open('pb_math.txt', 'r') as f:
            lines = f.readlines()
            print(lines)
        if float(lines[0]) >total_time:
            with open('pb_math.txt', 'w') as f:
                lines[0]= f.write(str(total_time))

        print(round(total_time,ndigits=2), 'your personal best time for this mode is ', lines[3])
    else:
        print("I pray that you dont fail your math test")


def play_game():
    print('''Welcome to the Math Quiz! You will be asked 10 questions, you cannot move to the next question before answering the previous one correctly.
You can give your answer as a rounded whole digit number or an answer upto the first decimal point''')
    while True:
        difficulty = int(input('''we have 4 difficulty levels 
1. Easy
2. intermediate
3. hard
4. hell
what level of difficulty would you like to play on press the corresponding number: '''))
        if difficulty == 1:
            question_easy()
            break
            
        elif difficulty == 2:
            question_intermediate()
            break
        
        elif difficulty == 3:
            question_hard()
            break
        
        elif difficulty == 4:
            question_hell()
            break
        
        else:
            print("Invalid option, please try again")
            continue
            
play_game()
