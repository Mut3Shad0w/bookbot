def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(book):
    book = book.split()
    word_count = 0
    for work in book:
        word_count += 1
    return word_count

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_contents)
    print(f"{num_words} words found in the document")

main()