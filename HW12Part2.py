#Ian Scroggs
#Python HW12 Part 2: Big Data

import sqlite3
import pandas as pd

def main():

    connection = sqlite3.connect('books.db')

    #Part A
    print("Part A")
    print(pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection))

    #Part B
    print("Part B")
    print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))

    #Part C
    print("Part C")
    print(pd.read_sql("""SELECT title, copyright, titles.isbn FROM titles INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn ORDER BY title ASC """, connection).head())

    #Part D
    print("Part D")
    cursor = connection.cursor()
    cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Ian', 'Scroggs')""")
    print(pd.read_sql('SELECT * FROM authors', connection))

    #Part E
    print("Part E")
    cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright) VALUES ('1234567890', 'Homework Book', '1', '2021')""")
    cursor.execute("""INSERT INTO author_ISBN (id, isbn) VALUES ('6','1234567890')""")
    print(pd.read_sql('SELECT * FROM titles', connection))
    print(pd.read_sql('SELECT * FROM author_ISBN', connection))




main()
