from typing import TypedDict
from pydantic import BaseModel

class User(TypedDict):
    id: int
    name: str
    email: str

user1 : User = {
    'id': 1,
    'name': 'john_stevenson',
    'email': 'something@nothing.com'
}

user2 : User = {
    'id': 2,
    'name': 'james_dickson',
    'email': 'anything@nothing.com'
}

user3: User = {
    'id': 3,
    'name': 'sean_kingston',
    'email': 'onething@nothing.com'
}

# page 97
class User(BaseModel):
    id: int
    name: str
    email: str

user_data = {
    'id': 4,
    'name': 'kevin_goodman',
    'email': 'goodthing@nothing.com'
}

print(user1)
print(user2)
print(user3)

user4 = User(**user_data)
print(user4)