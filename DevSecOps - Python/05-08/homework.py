#EX3
'''
numbers = [] # blank list
for i in range(5, 15):
    numbers.append(i)

print(numbers)
'''
# or
'''
r = range(1,15,1)
list_of_numbers = list(r)

print(type(list_of_numbers))

print(list_of_numbers)
'''

# or
'''
numbers = list(range(1, 15))
print(numbers)
'''
#lists

board = [['1','2','3'],
         ['4','5','6'],
         ['7','8','9']]

board[2][1] # will choose the second raw and then will choose the number 8 because it is in the 1 position (0 based)