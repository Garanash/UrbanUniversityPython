from pydantic import BaseModel
# from typing import List, Set, Tuple, Dict

# class User(BaseModel):
class Office():
    office_name: str

class User():
    id: int
    username: str
    age: int
    office: Office
    lst: list[int] = []

users = []
# user1 = User(id = 1, username = 'User1', age = 10)
# user2 = User(id = 2, username = 'User2', age = 20)
user1 = User()
user1.id = 1
user1.username = 'User1'
user1.age = 10
user1.office = Office()
user1.office.office_name = 'Office 1'
user1.lst.append(1)

user2 = User()
user2.id = 2
user2.username = 'User2'
user2.age = 20
user2.office = Office()
user2.office.office_name = 'Office 2'
user2.lst.append(2)

users.append(user1)
users.append(user2)


for user in users:
    print(user.id, user.username, user.age, user.office.office_name, User.office.office_name, user.lst)