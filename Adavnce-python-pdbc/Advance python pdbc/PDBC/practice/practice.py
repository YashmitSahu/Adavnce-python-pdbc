import pymysql

def testread1():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advancepython')
    cursor =connection.cursor()
    sql = "select * from user"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.commit()
    connection.close()

    print("data read successfully")

testread1()
