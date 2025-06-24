from stats import *
import sys

def get_book_text(filepath: str) -> str:
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    words_count = count_words(book_text)
    dict_characters = sort_dic(number_of_characters(book_text))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")

    for key, value in dict_characters.items():
        if key.isalpha():
            print(f"{key}: {value}")

    print("============= END ===============")

main()