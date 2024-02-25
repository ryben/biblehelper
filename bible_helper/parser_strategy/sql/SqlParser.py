import sqlite3

from bible_helper.parser_strategy.FileParser import FileParser
from bible_helper.parser_strategy.sql.SqlObjects import BibleEntry, BookEntry


class SqlParser(FileParser):
    def __init__(self, table_name, column_names):
        self.table_name = table_name
        self.column_names = column_names

    def parse(self, filepath):
        # Connect to your SQLite database
        conn = sqlite3.connect(filepath)  # Replace 'your_database.db' with your database file
        cursor = conn.cursor()

        # Query to select the top 5 rows, sorted by a column (e.g., 'verse')
        query = f"SELECT {','.join(self.column_names)} FROM {self.table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Convert each row into a BibleEntry object
        bible_entries = [BibleEntry(*row) for row in rows]

        content = {}
        for entry in bible_entries:
            if entry.book not in content:
                content[entry.book] = {}
            if entry.chapter not in content[entry.book]:
                content[entry.book][entry.chapter] = {}

            content[entry.book][entry.chapter][entry.verse] = entry.text

        # Close the connection
        conn.close()

        return content

    def extract_books_to_json(self):
        # Connect to your SQLite database
        conn = sqlite3.connect('bible.sqlite')  # Replace 'your_database.db' with your database file
        cursor = conn.cursor()

        # Query to select the top 5 rows, sorted by a column (e.g., 'verse')
        cursor.execute("SELECT id, name FROM BOOK WHERE language_id = 2")
        rows = cursor.fetchall()

        # Convert each row into a BibleEntry object
        book_entries = [BookEntry(*row) for row in rows]

        books_list = []
        # Example: Print each entry's verse
        for entry in book_entries:
            books_list.append(entry.name)

        # Close the connection
        conn.close()

        return books_list
