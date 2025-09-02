from stats import count_words, count_characters

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_contents)
    num_letter = count_characters(book_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"{num_words} words found in the document")
    print("--------- Character Count -------")
    print(f"{num_letter}")


main()
