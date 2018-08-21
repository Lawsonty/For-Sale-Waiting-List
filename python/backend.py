import sqlite3


class DBM:
    def __init__(self):
        self.conn = sqlite3.connect('movies.db')
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY
                     AUTOINCREMENT, title TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS  customers(id INTEGER
                     , name TEXT NOT NULL, phone NOT NULL,
                     PRIMARY KEY(name, phone))''')
        self.conn.commit()

    def addMovie(self, title):
        c = self.conn.cursor()
        c.execute('''INSERT INTO movies (title)
                     VALUES (?)''', (title,))
        self.conn.commit()

    def pullMovie(self, title, copies):
        pass

    def delMovie(self, title):
        c = self.conn.cursor()
        c.execute('''DELETE FROM movies WHERE title=?''', (title,))
        self.conn.commit()

    def addCustomer(self, name, number):
        pass


if __name__ == '__main__':
    dbm = DBM()
    dbm.addMovie("Saw IV")
    dbm.addMovie("Saw V")
    print(dbm.conn.cursor().execute("SELECT * FROM movies").fetchall())
    dbm.delMovie("Saw IV")
    print(dbm.conn.cursor().execute("SELECT * FROM movies").fetchall())
