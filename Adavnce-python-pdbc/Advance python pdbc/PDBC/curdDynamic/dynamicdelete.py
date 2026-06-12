import pymysql



def testDelete():
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advancepython')
    cursor = connection.cursor()
    sql = "delete from user where id = 9"
    cursor.execute(sql)
    connection.commit()
    connection.close()
print("data Delete Successfully")

def testdelete2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advancepython')
    cursor = connection.cursor()
    sql = "delete from user where id= %s"
    data=(2,)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data Delete2 Successfully")

def testdelet3(id):
    connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='advancepython')
    cursor = connection.cursor()
    sql = "delete from user where id = %s"
    data=(id,)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("data delete3 successfully")

#testdelete()
#test delete2()
testdelet3(8)
