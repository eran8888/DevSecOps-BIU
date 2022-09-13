# EX1 - Please remove the ''' to run the code

# write a python code that receive from the user a number
# and sum the digits of this number and then print the answer

'''
x = int(input('Enter a number: ')) #54622
newx = 0
ahadot = 0
new_ahadot = 0

for i in range(100000):
    if x == 0:
        break
    ahadot = x % 10 # 2, 2, 6, 4, 5
    # newx *= 10  # 0,
    # newx += ahadot # 2
    x = x // 10 # 5462, 546, 54, 5, 0
    new_ahadot = new_ahadot + ahadot

print('The sum of this number is: ', new_ahadot)
'''

# EX2 - Please remove the ''' to run the code

# write a python code that receive a username from the user
# and run in a loop checks of the letter is a,b,c,o
# it will convert them to upper case all the other letter should be in a lower case
# if the name included space ‘ ‘ break the loop

'''
username = input('Enter username: ')

username.lower()
username = username.lower()
username_length = len(username)
new_name = ''

for i in range(username_length):
    if username[i] == ' ':
        break
    # You can put:
    # if username[i] == 'a' or username[i] == 'b' or username[i] == 'c' or username[i] == 'o'
    #but it is better to shorten the code and write it like that:

    if username[i] in 'abco':     # or ['a', 'b', 'c', 'o']
        new_name += username[i].upper()
    else:
        new_name += username[i]

print(new_name)
'''

# EX3 - Please remove the ''' to run the code

# write a python code that receives 7 numbers from the user and prints the average of those numbers (user for loop )

'''
number = 0

for i in range(7):
    in1 = int(input(f'Enter number {i + 1}: '))
    number += in1

avg = number // 7
print(avg)
'''