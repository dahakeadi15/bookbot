from stats import count_words, count_chars


def get_book_text(file_path: str) -> str:
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()

    return file_contents


def main():
    book_contents = get_book_text("./books/frankenstein.txt")

    num_words = count_words(book_contents)
    print(f"{num_words} words found in the document")

    char_count = count_chars(book_contents)
    print(char_count)


if __name__ == "__main__":
    main()
