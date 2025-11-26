import sys
from stats import *

def get_book_text(bookpath):
    with open(bookpath) as b:
        return b.read()
    
def print_report(path, count, list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for c in list:
        if c['char'].isalpha():
            print(f"{c['char']}: {c['num']}")
    


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    char_count_sorted = char_dict_sort(char_count)
    print(char_count_sorted)
    print_report(book_path, word_count, char_count_sorted)


main()