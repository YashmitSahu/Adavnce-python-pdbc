import pymysql


def testread1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "SELECT * FROM EMPLOYEE "
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.commit()
    connection.close()

    print("data Read Successfully")


def testread2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "select * from user"
    cursor.execute(sql)
    data = cursor.fetchall()
    columnName = ('id', 'name', 'Salary')
    for x in data:
        print(x)
        print({columnName[i]: x[i] for i, _ in enumerate(x)})

    connection.close()

def testRead3():
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
        cursor = connection.cursor()

        sql = "select * from user"
        # sql = "select * from user where id = 1"
        # sql = "select * from user where LastName = 'Kumar'"
        # sql = "select * from user where name like 'a%'"
        # sql = "select * from user where Salary = 50000"

        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t')
        connection.commit()
        connection.close()

def testRead4(id, name, salary):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()

    sql = 'select * from user'
    if id != 0:
        sql += " where id = " + str(id)
    if name != '':
        sql += " where name like '" + name + "%'"
    if salary != 0:
        sql += " where salary = " + str(salary)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2])

    connection.commit()
    connection.close()


# testread1()
# testread2()
testRead4(0,'Raj',0)
