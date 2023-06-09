import sqlite3

conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM Student ORDER BY Age DESC LIMIT 5')
max_age_students = cursor.fetchall()
print("年齡最大的5個學生：")
for student in max_age_students:
    print(student)

cursor.execute('SELECT Department, COUNT(*) FROM Student GROUP BY Department')
department_counts = cursor.fetchall()
print("每個系的同學數量：")
for department in department_counts:
    print(f"科系: {department[0]}, 同学数量: {department[1]}")

cursor.execute('SELECT Department, AVG(Age) FROM Student GROUP BY Department')
department_avg_age = cursor.fetchall()
print("每個系的平均年齡：")
for department in department_avg_age:
    print(f"科系: {department[0]}, 平均年龄: {department[1]}")

cursor.execute('SELECT COUNT(*) FROM Student WHERE Department = "資訊管理"')
count = cursor.fetchone()[0]
print(f"資管系同學數量： {count}")

conn.close()
