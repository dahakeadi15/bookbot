def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_word_count(text)
    print(num_words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())


main()
