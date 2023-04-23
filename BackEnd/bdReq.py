import sqlite3


def createConnection():
    con = sqlite3.connect("file.db")
    return con


def updateTable():
    dropTable()
    createTable()
    values = [["kit1.webp"], ["kit2.jpg"], ["kit3.webp"]]
    insertFileNames(values)




def closeConnection(connection):
    connection.close()


def initCursor(connection):
    return connection.cursor()


def createTable():
    connection = createConnection()
    cur = initCursor(connection)
    cur.execute('''CREATE TABLE fileNames(
    fileName TEXT NOT NULL
    );''')
    connection.commit()
    cur.close()
    closeConnection(connection)


def dropTable():
    connection = createConnection()
    cur = initCursor(connection)
    cur.execute('''DROP TABLE fileNames''')
    connection.commit()
    cur.close()
    closeConnection(connection)


def insertFileNames(values):
    connection = createConnection()
    cur = initCursor(connection)
    cur.executemany('''INSERT INTO fileNames VALUES (?);''', values)
    connection.commit()
    cur.close()
    closeConnection(connection)


def showAllFileNames():
    connection = createConnection()
    cur = initCursor(connection)
    cur.execute('''SELECT * FROM fileNames''')
    data = cur.fetchall()
    connection.commit()
    cur.close()
    closeConnection(connection)
    return data




con = createConnection()
#updateTable(con)
print(showAllFileNames())
closeConnection(con)


