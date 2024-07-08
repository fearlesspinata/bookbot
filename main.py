def main():
    text = get_book_text("books/frankenstein.txt")
    print(count_words(text))

def get_book_text(book_path):
    with open(book_path) as b:
        return b.read()

def count_words(text):
    return len(text.split())

if __name__ == '__main__':
    main()
