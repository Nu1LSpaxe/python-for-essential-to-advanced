"""
caching_sha2_password: https://www.jianshu.com/p/a97be774fae5
"""

import mysql.connector

con = mysql.connector.connect(
    user="root",
    password="DYN@book_3nGryCa7#23221",
    host="127.0.0.1",
    database="class",
    auth_plugin='mysql_native_password'
)

cursor = con.cursor()
# cursor.execute("")
# con.commit()
con.close()
