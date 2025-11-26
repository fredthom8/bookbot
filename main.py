from stats import *

def get_book_text(bookpath):
    with open(bookpath) as b:
        return b.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"Found {word_count} total words")
    char_count = get_char_count(text)
    print(char_count)

main()