import json

from bible_helper.parser_strategy.FileParser import FileParser


class CsvParser(FileParser):

    def parse(self, filepath):
        book = 0

        content = {}
        with open(filepath, encoding='utf-8') as json_file:
            bible = json.load(json_file)
            for index, item in enumerate(bible):
                chapter = item["chapter_num"]
                verse = item["position"]
                verse_content = item["text"]

                if verse == 0:
                    continue

                if chapter == 1 and verse == 1:
                    book += 1

                if book not in content:
                    content[book] = {}
                if chapter not in content[book]:
                    content[book][chapter] = {}

                content[book][chapter][verse] = verse_content

        return content
