def count_words(string: str) -> int:
    return len(string.split())


def count_chars(string:str) -> dict:
    counter = {}
    for c in string:
        char = c.lower()
        counter[char] = counter.get(char, 0) + 1

    return counter


def sort_counter_dict(unsorted_counter: dict) -> list:
    sorted_counter_list = [{"char": char, "count": count} for char, count in unsorted_counter.items()]
    sorted_counter_list.sort(reverse=True, key=lambda x: x["count"])

    return sorted_counter_list

