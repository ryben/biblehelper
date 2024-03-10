import json
import os

from bible_helper import Util
from bible_helper.parser_strategy.FileParser import FileParser


class BibleDataProcessor:
    parser: FileParser

    def __init__(self, parser: FileParser):
        self.parser = parser

    def process(self, input_file_path, output_folder):
        bible_json = self.parser.parse(input_file_path)
        self.slice_per_book(bible_json, output_folder)

    # Read Whole Bible JSON then segregate per book
    def slice_per_book(self, bible_json, output_folder):
        os.makedirs(output_folder, exist_ok=True)

        for book in bible_json.keys():
            output_filepath = os.path.join(output_folder, f"{book}.json")
            Util.write_to_file(output_filepath, json.dumps(bible_json[book], separators=(',', ':')))
