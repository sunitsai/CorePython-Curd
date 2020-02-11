import pymysql

def createConn():
    return pymysql.connect(host="localhost",database="sunit",user="root",password="xbyte",port=3306)


def createTable():
    conn = createConn()
    cursor = conn.cursor()
    cursor.execute("create table emp(name varchar(50),address varchar(50),city varchar(50), state varchar(50))")
    conn.commit()
    print("Table Create...")
    conn.close()

def insertdata(name,address,city,state):
    conn = createConn()
    cursor = conn.cursor()
    args = (name,address,city,state)
    query = ("insert into emp (name,address,city,state)values(%s,%s,%s,%s)")
    cursor.execute(query,args)
    conn.commit()

    print("Data inserted ....")
    conn.close()


def getAll():
    conn = createConn()
    cursor = conn.cursor()
    cursor.execute("select * from emp")
    res = cursor.fetchall()
    for i in res:
        print(i)


def UpdateData(name,address,city,state):
    conn = createConn()
    cursor = conn.cursor()
    args = (name,address,city,state)
    query = "update emp set address=%s,city=%s,state=%s where name=%s"
    cursor.execute(query,args)
    conn.commit()
    print("Updated..")
    conn.close()
    

def deleteData(name):
    conn = createConn()
    cursor = conn.cursor()
    args = (name)
    query = "delete from emp where name=%s"
    cursor.execute(query,args)
    conn.commit()
    conn.close()

# createTable()


# n = input("Name :")
# a = input("Address :")
# c = input("City :")
# s = input("State :")




# insertdata(n,a,c,s)

# UpdateData(n,a,c,s)

getAll()

# deleteData(n)