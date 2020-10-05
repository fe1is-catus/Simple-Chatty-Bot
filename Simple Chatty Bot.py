#Simple Chatty Bot

#Stage 1/5: Hello! What’s your name?

print(f'''
Hello! My name is Chatty.
I was created in 05/10/20.
''')

#Stage 2/5: What's my name?

print(f'''
Hello! My name is Chatty.
I was created in 05/10/20.
''')

your_name = input("Please, remind me your name. ")

print(f'What a great name you have, {your_name}!')

#Stage 3/5: How old are you?

print(f'''
Hello! My name is Chatty.
I was created in 05/10/20.
''')

your_name = input("Please, remind me your name. ")

print(f'What a great name you have, {your_name}!')

print('''Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.''')

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {your_age}; that's a good time to start programming!")

#Stage 4/5: Let’s count!

print(f'''
Hello! My name is Chatty.
I was created in 05/10/20.
''')

your_name = input("Please, remind me your name. ")

print(f'What a great name you have, {your_name}!')

print('''Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.''')

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {your_age}; that's a good time to start programming!")

print('Now I will prove to you that I can count to any number you want.')

number_count = int(input())

for number in range(number_count + 1):
    print(number, "!")

print('Completed, have a nice day!')

#Stage 5/5: The student and the teacher

def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    
    print('''
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.
    ''')
    answer = input()
    
    if answer != "2":
       print("Please, try again.")
    else:
        print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Chatty', '2020')
remind_name()
guess_age()
count()
test()
end()

