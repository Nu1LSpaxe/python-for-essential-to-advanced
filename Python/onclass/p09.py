import sqlite3
import json

with open('data.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()

for item in json_data:
    name = item['姓名']
    student_id = item['學號']
    age = item['年齡']
    gender = item['性別']
    school = item['學校']
    department = item['科系']

    cursor.execute("INSERT INTO Student (StudentID, Name, Age, Gender, School, Department) VALUES (?, ?, ?, ?, ?, ?)",
                   (student_id, name, age, gender, school, department))

conn.commit()
conn.close()
