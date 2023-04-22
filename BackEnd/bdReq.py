import sqlite3


def createConnection():
    con = sqlite3.connect("file.db")
    return con


def updateTable(connection):
    dropTable(connection)
    createTable(connection)
    values = [["kit1.webp"], ["kit2.jpg"], ["kit3.webp"]]
    insertFileNames(connection, values)



def closeConnection(connection):
    connection.close()


def initCursor(connection):
    return connection.cursor()


def createTable(connection):
    cur = initCursor(connection)
    cur.execute('''CREATE TABLE fileNames(
    fileName TEXT NOT NULL
    );''')
    connection.commit()
    cur.close()


def dropTable(connection):
    cur = initCursor(connection)
    cur.execute('''DROP TABLE fileNames''')
    connection.commit()
    cur.close()


def insertFileNames(connection, values):
    cur = initCursor(connection)
    cur.executemany('''INSERT INTO fileNames VALUES (?);''', values)
    connection.commit()
    cur.close()


def showAllFileNames(connection):
    cur = initCursor(connection)
    cur.execute('''SELECT * FROM fileNames''')
    data = cur.fetchall()
    connection.commit()
    cur.close()
    return data




con = createConnection()
#updateTable(con)
print(showAllFileNames(con))
closeConnection(con)


