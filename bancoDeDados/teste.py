import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''

)

cursor = db.cursor()
cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)