def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = count_words(text)
    char_map = count_characters(text)
    sorted_char_map = get_sorted(char_map)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for item in sorted_char_map:
        print(f"The '{item[0]}' character was found {item[1]} times")
    print("--- End report ---")

def get_book_text(book_path):
    with open(book_path) as b:
        return b.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    char_map = {}
    for c in text:
        if c.lower().isalpha():
            if c.lower() in char_map:
                char_map[c.lower()] += 1
            else:
                char_map[c.lower()] = 1

    return char_map 

def get_value(item):
    return item[1]

def get_sorted(dictionary):
    return sorted(dictionary.items(), key=get_value, reverse=True)

if __name__ == '__main__':
    main()
