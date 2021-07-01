import json

BIBLE_JSON = "source/Ang Dating Biblia.json"

# UTILS
def write_to_file(filename, content):
    f = open(filename, "a")
    f.write(content)
    f.close()
#######



# Read Whole Bible JSON then segregate per book
def slice_per_book(whole_bible_json, output_folder):
    with open(whole_bible_json) as json_file:
        bible = json.load(json_file)
        for book in bible.keys():
            write_to_file(output_folder + "/" + book + ".json", json.dumps(bible[book], separators=(',', ':')))




slice_per_book(BIBLE_JSON, 'output')