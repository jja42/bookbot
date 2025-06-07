from stats import get_text_words, get_text_characters, get_sorted_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    contents = get_book_text(path)
    #print(contents)
    word_count = get_text_words(contents)
    character_count = get_text_characters(contents)
    sorted_count = get_sorted_characters(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    for dict in sorted_count:
        character = dict["key"]
        if(character.isalpha()):
            count = dict["value"]
            print(f"{character}: {count}")



main()