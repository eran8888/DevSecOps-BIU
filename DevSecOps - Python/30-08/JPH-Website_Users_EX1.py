# Write a python program that sends a GET request to
# json place holder site / users
#
# Convert all the json's to  POPO and save the users
# id and users names in a new file called names.txt

import requests
import json

class User:
    def __init__(self,dict):
        self.__dict__ = dict
    # POPO - Special class to create a list of users that will receive a JSON list as dict
    # all the values are converted to keys and values  like JSON.
try:
    jph_response = requests.get('https://jsonplaceholder.typicode.com/users/')

except:
    print('something went wrong')

# print(jph_response.text) # will bring the content in a text format. So we need to convert to JSON

list_of_jsons = json.loads(jph_response.text) # str -> JSON

# users_dict = jph_response.json() # this var will receive the content from the jsonplaceholder website as list / dict
#
users_object = []

for u in list_of_jsons:
    temp = User(u)
    users_object.append(temp) # appending the users directly from the class to the users_objects
try:
    with open('names.txt', 'w') as file:
        for temp in users_object:
            file.write(f' id = {temp.id} | name = {temp.name} \n')
except:
    print('There is an error with file')





