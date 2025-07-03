import sys
from stats import count_words, count_chars, sort_counter_dict


def get_book_text(file_path: str) -> str:
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()

    return file_contents


def main():
    inputs = sys.argv

    if len(inputs) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = inputs[1]

    book_contents = get_book_text(file_path)
    num_words = count_words(book_contents)
    char_count = count_chars(book_contents)

    # Print Report
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {file_path}...")
    print("---------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sort_counter_dict(char_count):
        if char["char"].isalpha():
            print(f"{char['char']}: {char['count']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
