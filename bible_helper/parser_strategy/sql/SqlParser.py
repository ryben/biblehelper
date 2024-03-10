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
