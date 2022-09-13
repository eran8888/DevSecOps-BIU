import requests

# resp = requests.get('https://google.com')

# print(resp) # Response [200] > as str
#
# print(resp.text) # page source code

# print(resp.url) # prints the url - good for redirection.

# print(resp.ok) # print true if status is 200 family else false

# print(resp.status_code) # prints the status code (int)

# if 200 <= resp.status_code < 300:
#     print('its working success')
# else:
#     print('Wrong page')

class User:  # we created a class to create a list of users that will receive a JSON list as dict
    def __init__(self,dict):
        self.__dict__ = dict


jph_response = requests.get('https://jsonplaceholder.typicode.com/users/')
if not jph_response.ok:
    exit()

# print(resp.text)

# users = resp.json()
# # print(users[0]['id'])
#
# for u in users:
#     print(u['name'])

users_dict = jph_response.json() # this var will receive the content from the jsonplaceholder website as list / dict

# print(users_dict[0]['name'])

users_object = []

for u in users_dict:
    temp = User(u)
    print(type(temp))
    users_object.append(temp)

for obj in users_object:
    print(obj.name)


