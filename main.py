def main():
    text = get_book_text("books/frankenstein.txt")
    char_map = count_characters(text)
    for c, count in char_map.items():
        print(c, count)

def get_book_text(book_path):
    with open(book_path) as b:
        return b.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    char_map = {}
    for c in text:
        if c.lower() in char_map:
            char_map[c.lower()] += 1
        else:
            char_map[c.lower()] = 1

    return char_map 

if __name__ == '__main__':
    main()
