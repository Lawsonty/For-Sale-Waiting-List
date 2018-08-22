import sqlite3
import time


class DBM:
    def __init__(self):
        self.conn = sqlite3.connect('movies.db')
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS movies
                     ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS customers
                     ( phone text PRIMARY KEY,
                       name TEXT NOT NULL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS list
                     ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                       MovieID INT NOT NULL,
                       CustomerID INT NOT NULL,
                       Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                       CONSTRAINT fk_movie
                         FOREIGN KEY (MovieID)
                         REFERENCES movies(id)
                         ON DELETE CASCADE
                       CONSTRAINT fk_customer
                         FOREIGN KEY (CustomerID)
                         REFERENCES customers(phone)
                         ON DELETE CASCADE
                     )''')
        self.conn.commit()

    def addMovie(self, title):
        c = self.conn.cursor()
        c.execute('''INSERT INTO movies (title)
                     VALUES (?)''', (title,))
        self.conn.commit()

    def pullMovie(self, title, copies):
        c = self.conn.cursor()
        res = c.execute('''
                     SELECT
                       list.id
                     FROM customers
                     INNER JOIN list ON list.customerID = customers.phone
                     INNER JOIN movies on movies.id = list.MovieID
                     WHERE movies.title = ?
                     ORDER BY list.Time
                     Limit ?
                     ''', (title, copies)).fetchall()
        print(res)
        res = tuple(item for sublist in res for item in sublist)
        q = 'DELETE FROM list WHERE id IN (' \
            + ', '.join(["?"] * len(res)) + ')'
        c.execute(q, res)
        self.conn.commit()

    def pullMovies(self, pairs):
        for pair in pairs:
            self.pullMovie(pair[0], pair[1])

    def delMovie(self, title):
        c = self.conn.cursor()
        c.execute('''DELETE FROM movies WHERE title=?''', (title,))
        self.conn.commit()

    def addCustomer(self, name, number):
        c = self.conn.cursor()
        if not c.execute('''SELECT * FROM customers WHERE phone=?''',
                         (number,)).fetchone():
            c.execute('''INSERT INTO customers (name, phone)
                     VALUES (?, ?)''', (name, number))
        else:
            return False
        self.conn.commit()
        return True

    def delCustomer(self, name, number):
        c = self.conn.cursor()
        c.execute('''DELETE FROM customers WHERE name=? AND phone=?''',
                  (name, number))
        self.conn.commit()

    def addCustomertoMovie(self, number, movie):
        c = self.conn.cursor()
        c.execute('''INSERT INTO list(MovieID, CustomerID)
                     VALUES (
                     (SELECT id FROM movies WHERE title=? LIMIT 1), ?)''',
                  (movie, number))
        self.conn.commit()


if __name__ == '__main__':
    dbm = DBM()
    dbm.addMovie("Saw IV")
    print(dbm.conn.cursor().execute("SELECT * FROM movies").fetchall())
    # dbm.delMovie("Saw IV")
    # print(dbm.conn.cursor().execute("SELECT * FROM movies").fetchall())
    dbm.addCustomer("Johnny Franko", 5034051367)
    dbm.addCustomer("Franko", 5034051360)
    print(dbm.conn.cursor().execute("SELECT * FROM customers").fetchall())
    # dbm.delCustomer("Johnny Franko", 5034051367)
    # print(dbm.conn.cursor().execute("SELECT * FROM customers").fetchall())
    dbm.addCustomertoMovie(5034051367, 'Saw IV')
    time.sleep(1)
    dbm.addCustomertoMovie(5034051360, 'Saw IV')
    print(dbm.conn.cursor().execute("SELECT * FROM list").fetchall())
    dbm.pullMovie("Saw IV", 1)
    print(dbm.conn.cursor().execute("SELECT * FROM list").fetchall())
