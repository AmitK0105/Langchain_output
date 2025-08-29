from typing import TypedDict

class person(TypedDict):
    name: str
    age : int

new_person : person={"name":"Amit", "age": 39}

print(new_person)