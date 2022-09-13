'''
name = 'Ron'

while name != 'admin':
        name = input('please enter your name: ')
        print('not admin')

age = 0

while age <= 0:
    age = int(input('please enter your age: '))

'''

# write a program that receives from the user inputs (int) until the sum of all the number is greater than 100 and
# then print the sum

'''

sum = 0

while sum < 100:
    number = int(input('Enter a number: '))
    sum += number

print(sum)

'''

# Two numbers are entered through the keyboard. Write a program to find the value of one number raised
# to the power of another

'''

number = int(input('What is the number you want to multiply? ')) #2
times = int(input('How many times to multiply it? '))
counter = 1
new_number = number # 2

while counter < times:
    new_number *= number # 4
    counter += 1 # 1

print(new_number)

'''

# write a program that does "Atzeret"

'''
number = int(input('What is the number to do Atzeret? '))
new_number = number
times = 1

while times <= number:
    new_number *= (number - 1)
    number -= 1
    times += 1

print(new_number)
'''

