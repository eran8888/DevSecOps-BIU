'''name = input('please enter your name: ')
age = input('please enter your age: ')

print ('Hi', name, 'you are', age, 'years old')'''
from typing import List, Any

'''children_no = input('please enter your children number: ')
pizza_sli = input ('how many pizza slices you ordered? ')

children_no = int(children_no)
pizza_sli = int(pizza_sli)

print ( type (children_no))

print('Each children will have :', int(pizza_sli // children_no), 'and left is: ', int(pizza_sli % children_no))'''

'''list1 = (2, 5, 7, 9)
print (type (list1))

list2 = [2, 5, 7, 9]
print (type(list2))

list3 = {2, 4, 6, 7, 7, 8, 1}
print (list3)'''

'''grades = [99, 100, 14, 55, 69]
print(grades)

grades.append(84)
print(grades)

grades.insert(1, 55)
print(grades)'''


names = []
# in1 = input('Enter 1st names:')
# names.append(in1)
# in1 = input('Enter 1st names:')
# names.append(in1)
# in1 = input('Enter 1st names:')
# names.append(in1)
# in1 = input('Enter 1st names:')
# names.append(in1)

for item in range(4):
    in1 = input(f'Enter 1st names {item+1} :')
    names.append(in1)
    print(in1.upper())

for item in names:
    print(item.upper())


