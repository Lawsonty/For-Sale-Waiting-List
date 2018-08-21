import sqlite3


class DBM:
    def __init__(self):
        self.conn = sqlite3.connect('movies.db')
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY
                     AUTOINCREMENT, title TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS  customers(id INTEGER PRIMARY
                     KEY AUTOINCREMENT, name TEXT NOT NULL, phone NOT NULL)''')
        self.conn.commit()

    def addMovie(self, title):
        c = self.conn.cursor()
        c.execute('''INSERT INTO movies (title)
                     VALUES (?)''', (title,))
        self.conn.commit()


# class Movies:
#     def __init__(self, conn):
#         self.conn = conn
#         c = conn.cursor()
#         c.execute('''CREATE TABLE IF NOT EXSISTS movies(id INTEGER PRIMARY KEY
#                      AUTOINCREMENT, title TEXT)''')
#         c.execute('''CREATE TABLE IF NOT EXISTS  ''')
#
#     def addMovie(self):
#         pass
#
#
# class Customers:
#     def __init__(self, conn):
#         pass


if __name__ == '__main__':
    dbm = DBM()
    dbm.addMovie("Saw IV")
    print(dbm.conn.cursor().execute("SELECT * FROM movies").fetchall())
