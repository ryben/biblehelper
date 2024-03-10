def write_to_file(filename, content):
    with open(filename, "w", encoding='utf-8') as f:
        f.write(content)
