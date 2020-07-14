import sqlite3

conn = sqlite3.connect('./world.db')

cur = conn.cursor()

res = cur.execute('''
SELECT CountryCode, COUNT(CountryCode) AS a
FROM City
GROUP BY CountryCode
ORDER BY a DESC
''').fetchall()

print(res)
