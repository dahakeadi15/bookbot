def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    report = get_report(text)
    print(report)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())


def get_character_count(text):
    chars = {}

    for char in text:
        lower_c = char.lower()
        if lower_c in chars:
            chars[lower_c] += 1
        else:
            chars[lower_c] = 1

    chars = {
        key: value
        for value, key in sorted([(chars[c], c) for c in chars], reverse=True)
    }

    return chars


def get_report(text):
    report = ""

    # start building the report
    # first line
    report += "--- Begin report of books/frankenstein.txt ---\n"

    # get the word count and include it in the report
    num_words = get_word_count(text)
    report += f"{num_words} words found in the document\n\n"

    # get count of all characters and include the ones from the alphabet it in the report
    num_chars = get_character_count(text)
    for c in num_chars:
        if c.isalpha():
            report += f"The '{c}' character was found {num_chars[c]} times\n"

    # end of report
    report += "--- End report ---"

    return report


main()
