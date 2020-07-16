import sqlite3

conn = sqlite3.connect('./problem2.db')

cur = conn.cursor()

res = cur.execute('''
SELECT c.name, c.grade_point, d.credits, c.tot_cred
FROM (SELECT b.name, a.course_id, a.grade_point, b.tot_cred 
FROM takes AS a 
INNER JOIN student AS b ON a.ID = b.ID) AS c
INNER JOIN course AS d ON c.course_id = d.course_id''').fetchall()

name = ''
grade_cred = 0.0
tot_cred = 0.0

for student in res :
    if name == '' :
        name = student[0]
        grade_cred = student[1] * student[2]
        tot_cred = student[3]
        
    elif name == student[0] :
        grade_cred += student[1] * student[2]

    elif name != student[0] :
        print(f'{name} 학생의 학점 평균은 {grade_cred/tot_cred}')
        name = student[0]
        grade_cred = student[1] * student[2]
        tot_cred = student[3]

print(f'{name} 학생의 학점 평균은 {grade_cred/tot_cred}')

conn.close()
