import mysql.connector as mysql

db = mysql.connect(
host='db-mysql-fra1-43438-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='user1',
    passwd='1Password1',
    database='QAP'

)

cursor = db.cursor(dictionary=True)
cursor.execute('select * from students')
result = cursor.fetchall()
for student in result:
    print(student['name'])

query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values = ('Vasya', 'Pupkin')
cursor.execute(query, values)
db.commit()


db.close()