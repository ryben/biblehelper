import json
import os
import sqlite3


# Define a class to represent a row from the 'bible' table
class BibleEntry:
    def __init__(self, id, book, chapter, verse, text):
        self.id = id
        self.book = book
        self.chapter = chapter
        self.verse = verse
        self.text = text


# Define a class to represent a row from the 'bible' table
class BookEntry:
    def __init__(self, id, name, language_id):
        self.id = id
        self.name = name
        self.language_id = language_id


def extract_bible_to_json():
    # Connect to your SQLite database
    conn = sqlite3.connect('bible.sqlite')  # Replace 'your_database.db' with your database file
    cursor = conn.cursor()

    # Query to select the top 5 rows, sorted by a column (e.g., 'verse')
    cursor.execute("SELECT id, book_id, chapter, verse, eng_niv FROM BIBLE")
    rows = cursor.fetchall()

    # Convert each row into a BibleEntry object
    bible_entries = [BibleEntry(*row) for row in rows]

    content = {}
    # Example: Print each entry's verse
    for entry in bible_entries:
        if entry.book not in content:
            content[entry.book] = {}
        if entry.chapter not in content[entry.book]:
            content[entry.book][entry.chapter] = {}

        content[entry.book][entry.chapter][entry.verse] = entry.text

    # Close the connection
    conn.close()

    return content


def extract_books_to_json():
    # Connect to your SQLite database
    conn = sqlite3.connect('bible.sqlite')  # Replace 'your_database.db' with your database file
    cursor = conn.cursor()

    # Query to select the top 5 rows, sorted by a column (e.g., 'verse')
    cursor.execute("SELECT id, name, language_id FROM BOOK WHERE language_id = 2")
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


# UTILS
def write_to_file(filename, content):
    f = open(filename, "w", encoding='utf-8')
    f.write(content)
    f.close()


#######
#
#
# # Read Whole Bible JSON then segregate per book
# def slice_per_book(whole_bible_json, output_folder):
#     with open(whole_bible_json) as json_file:
#         bible = json.load(json_file)
#         for book in bible.keys():
#             write_to_file(output_folder + "/" + book + ".json", json.dumps(bible[book], separators=(',', ':')))


# # Read Whole Bible JSON then segregate per book
def slice_per_book(bible, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for book in bible.keys():
        write_to_file(f"{output_folder}/{book}.json", json.dumps(bible[book], separators=(',', ':')))


bible_structured_json = extract_bible_to_json()
slice_per_book(bible_structured_json, "output")

books_list = extract_books_to_json()
books_json = json.dumps(books_list, indent=4, separators=(',', ':'))
write_to_file("output/books.json", books_json)
