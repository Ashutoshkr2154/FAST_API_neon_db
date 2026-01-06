from fastapi import FastAPI 
from pydantic import BaseModel 
import psycopg2 
from psycopg2.extras import RealDictCursor

app = FastAPI()

## Pip install psycopg2-binary 

db_url = "postgresql://neondb_owner:npg_8ZDzeFfEyvq9@ep-royal-dawn-ad1zvpr0-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

class Students(BaseModel):
    id : int 
    name : str 
    age : int 

def get_connection_url(): 
    conn = psycopg2.connect(db_url , cursor_factory = RealDictCursor)
    return conn

def save_student_to_file(data:Stdents):
    with open("students.txt" , "a" ) as f : 
        f.write(f"{data.id} , {data.name} , {data.age}\n")

@app.post("/students")
def create_student(stud:Students):
    save_student_to_file(stud)
    return {"message":"student data saved successfully!"}


@app.post("/students/db/insert")
def store_student_in_db(student: Students):
    conn = get_connection_url()
    cursor = conn.cursor() 
    insert_query= "INSERT INFO student (id , name , age) VALUES (%s , %s , %s)"
    cursor.execute(insert_query, (student.id , student.name , student.age))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message" : "Student data inserted into database successfully"}