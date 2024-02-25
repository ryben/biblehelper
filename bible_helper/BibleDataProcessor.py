import json
import os

from bible_helper.parser_strategy.FileParser import FileParser


def write_to_file(filename, content):
    f = open(filename, "w", encoding='utf-8')
    f.write(content)
    f.close()


class BibleDataProcessor:
    parser: FileParser

    def __init__(self, parser: FileParser):
        self.parser = parser

    def process(self, input_file_path, output_folder):
        bible_json = self.parser.parse(input_file_path)
        self.slice_per_book(bible_json, output_folder)

    # Read Whole Bible JSON then segregate per book
    def slice_per_book(self, bible, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for book in bible.keys():
            write_to_file(f"{output_folder}/{book}.json", json.dumps(bible[book], separators=(',', ':')))
