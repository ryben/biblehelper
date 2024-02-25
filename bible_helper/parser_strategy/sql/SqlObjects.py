
# Define a class to represent a row from the 'bible' table
class BibleEntry:
    def __init__(self, book, chapter, verse, text):
        self.book = book
        self.chapter = chapter
        self.verse = verse
        self.text = text


# Define a class to represent a row from the 'bible' table
class BookEntry:
    def __init__(self, name, language_id):
        self.name = name
        self.language_id = language_id
