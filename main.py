def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    book_contents = get_book_text("books/frankenstein.txt")

    print(book_contents)

main()