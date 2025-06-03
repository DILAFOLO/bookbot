import sys

from stats import get_num_words
from stats import get_num_car
from stats import get_sorted_char
def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1] 
    book_text = get_book_text(book_path) 
    num_words = get_num_words(book_text)
    num_car = get_num_car(book_text)
    sorted_char = get_sorted_char(num_car)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")



def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

main()

