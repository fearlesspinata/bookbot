def main():
    get_book_text("books/frankenstein.txt")

def get_book_text(book_path):
    with open(book_path) as b:
        return b.read()

if __name__ == '__main__':
    main()
