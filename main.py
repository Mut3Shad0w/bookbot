from stats import count_words, count_characters, dic_list
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    if len(sys.argv) <2 or len(sys.argv) >2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    location = sys.argv
    book_contents = get_book_text(location[-1])
    num_words = count_words(book_contents)
    num_letter = dic_list(count_characters(book_contents))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in num_letter:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()
