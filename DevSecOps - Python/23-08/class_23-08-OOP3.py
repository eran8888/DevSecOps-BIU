class bit:
    '''this is the superclass'''
    def __init__(self,number):
        self.number = number

    def calc_bits(self):
        return self.number

class byte(bit):
    def __init__(self,number):
        # calling for the "bit" superclass initializer / constructor (__init__) and adding (number)
        # because the superclass receives a number from the user:

        super().__init__(number)

    def calc_bits(self):
        return self.number * 8

class kb(bit):
    def __init__(self,number):
        super().__init__(number)

    def calc_bits(self):
        return self.number * 8 * 1024

class mb(bit):
    def __init__(self,number):
        super().__init__(number)

    def calc_bits(self):
        return self.number * 1024 * 1024 * 8

class gb(bit):
    def __init__(self,number):
        super().__init__(number)

    def calc_bits(self):
        return self.number * 8 * 1024 * 1024 * 1024


# No challenge solution - this is the shortest and efficient solution:

# print('please enter a number and a unit [bit, byte, kb, mb, gb]')
# number = int(input())
# unit = input()

# units = {'bit':bit(number),'byte':byte(number),'kb':kb(number),'mb':mb(number),'gb':gb(number)}
# print(units[unit].calc_bits())


# We could write this if statements to receive the input and get the result,
# However this is very long and not efficient as just to do the above,
# which means that we create a dictionary (JSON) with the keys above and print the key and the calc_bits
# function that calculates the number in bits
#
# if unit == 'bit':
#     my_unit = bit(number)
#
# elif unit == 'byte':
#     my_unit = byte(number)
#
# elif unit == 'kb':
#     my_unit = kb(number)
#
# elif unit == 'mb':
#     my_unit = mb(number)
#
# elif unit == 'gb':
#     my_unit = gb(number)
#
# print(my_unit.calc_bits())


'''Challenge 1 - Log method - Can be used for log files'''
# Save it a file:

file = open('history.txt', 'a') # 'w' will replace the line in the file. To use append just replace with 'a'
print('please enter a number and a unit [bit, byte, kb, mb, gb]')
number = int(input())
unit = input()

file.write(f'the number is {number} {unit}  ')

units = {'bit':bit(number),'byte':byte(number),'kb':kb(number),'mb':mb(number),'gb':gb(number)}

file.write(f'which means {units.get(unit).calc_bits()} bits') # get is used here that if there is an error in the input
# it won't crush the system

file.write('\n') # adds space between lines
file.close()





