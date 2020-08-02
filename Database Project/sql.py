import sqlite3
tableName="myTable.db"

def createTable():
    connection = sqlite3.connect(tableName)
    cursor = connection.cursor()
    with open('QUERIES.sql') as f:
        print("Wait While forming the table structure......")
        print("Reading Queries....")
        queries=f.read()
        print(queries)
        print("Executing Queries....")
        cur1=cursor.executescript(queries)
        cursor.fetchall()
        print("Table structure formed")
        cursor.close()
        connection.close()

def enterData():
    connection = sqlite3.connect(tableName)
    cursor = connection.cursor()
    with open('STRUCTURE.sql') as f:
        print("Wait data insertion will take time.....")
        print("Reading data...")
        queries=f.read()
        print(queries)
        print('Inserting data..')
        cur2=cursor.executescript(queries)
        cursor.fetchall()
        print("Insertion finished")
        cursor.close()
        connection.close()

createTable()
enterData()