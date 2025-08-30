from pydantic import BaseModel

class Student(BaseModel):

    name: str


new_student= {"name": "Amit"}

student= Student(**new_student)

print(student)