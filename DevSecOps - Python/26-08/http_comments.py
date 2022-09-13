import requests

class Comment:
    def __init__(self,dict):
        self.__dict__ = dict

response = requests.get('https://jsonplaceholder.typicode.com/comments/')

if response.ok:
    comments = response.json() # list of dictionaries
    print(comments[3]['body']) # will return the content in the 4th (remember! - zero based) comment where the JSON key is 'body' in the website
    # but this can be a place for errors because if there is in the website list in lists then it can return values which I didn't request.
    # So, the best thing is to create VAR in class that will pull the dict list from the website and return the values as I want. See class above:

    comment1 = comments[0] # dict
    comment1_obj = Comment(comment1)
    print(comment1_obj.body) # will print the 1st comment in 'body'

