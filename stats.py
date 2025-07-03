def count_words(string: str) -> int:
    return len(string.split())


def count_chars(string:str) -> dict:
    counter = {}
    for c in string:
        char = c.lower()
        counter[char] = counter.get(char, 0) + 1

    return counter

print(count_chars("hello there"))
