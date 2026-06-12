import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
cursor = connection.cursor()
sql = "INSERT INTO user VALUES (6, 'RAJ', 70000)"
cursor.execute(sql)
connection.commit()
connection.close()
print("Data Inserted Successfully")