import pymysql


def testUpdate1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advancepython')
    cursor = connection.cursor()
    sql = "update user set name = 'Rehmana' where id =2"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data updated successfully')

testUpdate1()


