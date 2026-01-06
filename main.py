from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def test():
    return{"message":"Hello , World!"}

@app.get("/Ashu")
def test1(): 
    return "my name is Ashutosh i learn GenAI . "

students = {1:"akash" , 2: "Ashutosh" , 3:"Sachin"}

@app.get("/students")
def get_student():
    return students 

def student_search(stud_id) : 
    return students.get(stud_id, "student not found")

@app.get("/students/{stud_id")
def student_search(stud_id:int):
    return {"id" :stud_id , "name":students[stud_id]}

@app.get("/add_student")
def add_student(stud_id:int , name:str):
    students[stud_id] = name 
    return students 

@app.post("/add_student_diff")
def add_student_diff(): 
    students['new_id'] = "new_name"
    return students

from pydantic import BaseModel 
class newdata(BaseModel):
    stud_id : int 
    name:str

@app.post("/add_student_new_value")
def add_student_new_value(newdata:newdata ): 
        students[newdata.stud_id] = newdata.name 
        return students