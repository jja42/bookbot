def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_text_words(text):
    words = text.split()
    return len(words)


def main():
    path = "./books/frankenstein.txt"
    contents = get_book_text(path)
    #print(contents)
    word_count = get_text_words(contents)
    print(f"{word_count} words found in the document")



main()