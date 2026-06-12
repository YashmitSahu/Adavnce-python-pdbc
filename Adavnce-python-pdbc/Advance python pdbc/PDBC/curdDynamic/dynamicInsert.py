import  pymysql
def testinsert1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advancepython')
    cursor = connection.cursor()
    sql = "INSERT INTO USER VALUES (%s, %s, %s)"
    data=(3,'Bubby',80000)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data Inserted2 Successfully")


def testInsert2(id, Name, Salary):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advancepython')
    cursor = connection.cursor()
    sql = "INSERT INTO USER VALUES (%s, %s, %s)"
    data = (id, Name, Salary)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted3 successfully')

def testInsert4(data={}):
    id = data['id']
    name = data['Name']
    Salary = data['Salary']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advancepython')
    cursor = connection.cursor()
    sql = "INSERT INTO USER VALUES (%s, %s, %s)"
    data = (id, name, Salary)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted4 successfully')

# testinsert1()
# testInsert2(4,"uday",50000)
testInsert4({'id':5,
             'Name':'Aman',
             'Salary':100000})