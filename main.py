from stats import count_words

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_contents)
    print(f"{num_words} words found in the document")

main()
