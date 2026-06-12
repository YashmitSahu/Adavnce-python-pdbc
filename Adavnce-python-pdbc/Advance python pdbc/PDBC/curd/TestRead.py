import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
cursor = connection.cursor()
sql = "select * from user"
cursor.execute(sql)
result = cursor.fetchall()
for data in result:
    print(data[0],data[1],data[2])
connection.close()
print("Data Read Successfully")
