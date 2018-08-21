import sqlite3


conn = sqlite3.connect('imdb.db')
c = conn.cursor()
c.execute('''CREATE TABLE movies
             (id int primary key, titleType text, primaryTitle text,
             originalTitle text, startYear int, endYear int,
             runTimeMinutes int, genres text)''')

with open("title.basics.tsv") as f:
    id = 1
    firstline = True
    for line in f:
        if firstline:
            firstline = False
            continue
        text = line.split('\t')
        c.execute('''INSERT INTO movies VALUES (?, ?, ?, ?, ?,
                     ?, ?, ?)''', (id, text[1], text[2], text[3],
                                   text[5], text[6], text[7], text[8]))
        id += 1
conn.commit()
conn.close()
