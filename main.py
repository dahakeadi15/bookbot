def get_book_text(file_path: str) -> str:
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()

    return file_contents


def count_words(string: str) -> int:
    return len(string.split())

def main():
    book_contents = get_book_text("./books/frankenstein.txt")
    num_words = count_words(book_contents)
    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()
