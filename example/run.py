import json

from bible_helper import Util
from bible_helper.BibleBookSqlParser import BibleBookSqlParser
from bible_helper.BibleDataProcessor import BibleDataProcessor
from bible_helper.parser_strategy.CsvParser import CsvParser
from bible_helper.parser_strategy.sql.SqlParser import SqlParser

input_filepath = "data/bible.sqlite"
output_folder = "output"

# Process bible data
if input_filepath.lower().endswith(".sqlite"):
    parser = SqlParser("BIBLE", ['book_id', 'chapter', 'verse', 'eng_niv'])
elif input_filepath.lower().endswith(".csv"):
    parser = CsvParser()
else:
    raise ValueError("Unsupported input file type")

processor = BibleDataProcessor(parser)
processor.process(input_filepath, output_folder)

# Process book names
bookParser = BibleBookSqlParser(input_filepath)
books_list = bookParser.parse("SELECT name FROM BOOK WHERE language_id = 2")
books_json = json.dumps(books_list, indent=4, separators=(',', ':'))
Util.write_to_file("output/books.json", books_json)
