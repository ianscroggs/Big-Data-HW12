#Ian Scroggs
#Python HW12 Part 1(17.2): Big Data

import sqlite3
import pandas as pd
import os.path


def main():

    connection = sqlite3.connect('books.db')

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM titles")
    description = cursor.description
    for i in range(len(cursor.description)):
        print(description[i][0], end="        ")

    print()
    fetchall = (cursor.fetchall())
    for row in fetchall:
        print(row[0], end=" ")
        print(row[1], end=" ")
        print(row[2], end=" ")
        print(row[3])



main()