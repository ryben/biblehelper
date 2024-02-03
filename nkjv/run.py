import json
import os

BIBLE_JSON = "nkjv.json"


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


def to_structured_json(bible_json_file):
    book = 0

    content = {}
    with open(bible_json_file, encoding='utf-8') as json_file:
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


# # Read Whole Bible JSON then segregate per book
def slice_per_book(bible, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for book in bible.keys():
        write_to_file(f"{output_folder}/{book}.json", json.dumps(bible[book], separators=(',', ':')))


structured_json = to_structured_json(BIBLE_JSON)

slice_per_book(structured_json, "output")

