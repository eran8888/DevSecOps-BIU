# Write a Python program that takes a
# text file as input and returns the number
# of words of a given text file
# etgar: Some words can be separated by a comma with no space

filename = input('please enter a file name / path  ')

file = open(filename,'r')

content = file.read() # returns the file content

file.close()

content = content.rstrip() ## trims blanks input on the right
content.replace((',', ' ')) ## etgar solution
content.replace('\n',' ')

print (len(content.split(' ')))