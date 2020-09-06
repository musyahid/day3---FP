import requests, json

response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

def getUser(id):
    return list(filter(lambda a: a['id'] == id, users))

for post in posts:
    post['user'] = getUser(post['userId'])
    print(json.dumps(post, indent=1))
