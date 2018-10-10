import requests
import json

def get_header():
    f = open(".auth", "r")
    key = f.read()
    return {"x-auth-token": key}

def fetch_profiles():
    url = "https://api.gotinder.com/v2/recs/core?locale=en"
    header = get_header()
    response = requests.get(url, headers=header)
    return json.loads(response.text)['data']['results']

HEADER = get_header()

class User(object):
    def __init__(self, j):
        self.id = j['user']['_id']
        self.bio = j['user']['bio']
        self.name = j['user']['name']
        self.birth_date = j['user']['birth_date']
    
    def like(self):
        res = requests.post("https://api.gotinder.com/like/"+self.id, headers=HEADER)
        return res


users = []
for p in fetch_profiles():
    users.append(User(p))

print(users)
u = users[0]

print(u.name, u.bio, u.id)
res = u.like()
print(res)
print(res.text)