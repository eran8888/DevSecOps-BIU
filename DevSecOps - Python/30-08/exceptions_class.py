'''
x = 3

y = int(input())

try:
    print(x/y)
# I can use "pass" here or:
# except ZeroDivisionError: # will catch the error only if the error is from ZeroDivisionError
except ArithmeticError: # will catch the error only if the error is from ZeroDivisionError type
    print('please enter a positive number next time')
except ValueError: # will handle the error if it's a ValueError type:
    print('please enter a number next time')

    # but I can use the parent class for all Arithmetic errors above which is ArithmeticError.
    # So I don't need to specify "except ZeroDivisionError" and change it to ArithmeticError. See above.

# write a python code that reads from file1.txt in the
# same pwd
# this code should not fall or raise an exception if the file isn't exists
'''

'''
try:
    with open('file1.txt') as file:
        print(file.read())
except:
        print('Something went wrong')
else: # Works only if the try success and didn't go to except. This will ensure other actions in "else" will run.
    # For example: reset a file / web session.
    # So in this use case even if the try will work it will write "Done" and not go to "except"
    print('Done')
finally: # Will work no matter what even if it worked in try or except.
    # this will ensure closing actions running. For example: closing running web session or open file.
    
    print('closed all the loose ends')
'''


# write a python program that receives
# from the user 2 numbers and divide
# them
# the code must handle all the exception
# and if we got a ZeroDivisionError we
# should ask the user to enter anew
# number
# if the code ended with no Errors
# print "hola totakhetooos"
# at the end write  "see you next
# time habibi"

def input_valid_number(): # to ensure that values are numbers and not string.
    # This function only receives 1 number and returns int.
    while True:
        try:
            x = int(input('please enter a number: '))
            if x == 0:
                    raise Exception ('No zero please') # Can use raise for raising an error as I choose.
        except ValueError:
            print('You did not enter a number')
        else: # I need to ensure that I will send back a number
            return x

def div (x, y):
   try:
        return x/y
   except:
        print('You cannot divide in 0')

in1 = input_valid_number()
in2 = input_valid_number()

print(div(in1,in2))

# My solution - doesn't work:
# def divide(x,y):
#         try:
#             return x / y
#         except:
#             print('You are dividing in 0. Choose again')
#
#         else:
#             print('hola totah')
#         finally:
#             print('See you next time habibi')
#
#
# num1 = divide(x=int(input('enter a number: ')))
# num2 = divide(y=int(input('enter a number: ')))
#
# print(divide(num1,num2))
