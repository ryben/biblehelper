import sqlite3

from bible_helper.parser_strategy.sql.SqlObjects import BibleEntry, BookEntry


class BibleBookSqlParser:
    def __init__(self, sql_filepath):
        self.sql_filepath = sql_filepath

    def parse(self, query):
        # Connect to your SQLite database
        conn = sqlite3.connect(self.sql_filepath)
        cursor = conn.cursor()

        # Query to select the top 5 rows, sorted by a column (e.g., 'verse')
        cursor.execute(query)  # "SELECT id, name FROM BOOK WHERE language_id = 2"
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
