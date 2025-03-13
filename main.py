from stats import count_of_words_in_text as count_words
from stats import count_characters
import stats
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_content = f.read()
        return file_content
    # do something with f (the file) here

def get_file_path_from_cli():
    filepath = []
    filepath = sys.argv
    if len(filepath) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return filepath


def main():
    filepath_from_cli = get_file_path_from_cli()
    filepath = f"./{filepath_from_cli[1]}"
    file_content = get_book_text(filepath)
    number_of_words = count_words(file_content)
    number_of_characters = count_characters(file_content)
    sorted_alphabet = stats.sorted_by_alphabetical_order(number_of_characters)
    print(f'''
        ============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {number_of_words} total words
--------- Character Count -------
{sorted_alphabet}
============= END ===============
          ''')


main()