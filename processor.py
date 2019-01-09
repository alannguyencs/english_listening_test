import codecs

def remove_non_alpha_characters(text):
    return ''.join(c for c in text if (c.isalpha() or c.isdigit()))


def parse_data_file(file_path):
    reader = codecs.open(file_path, 'r', 'utf8')
    content = list()

    for line in reader.readlines():
        # string.strip() is a function which remove whitespace and newline characters from string
        line = line.strip()

        if len(line) == 0:
            continue

        raw_words = line.split()
        words = [remove_non_alpha_characters(word).lower() for word in raw_words]

        content += words

    return content

