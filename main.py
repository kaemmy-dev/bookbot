from collections import defaultdict


def main():
    book_path = "books/frankenstein.txt"
    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found.")
        return

    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    """Returns the number of words in the given text."""
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    """Converts the character dictionary to a sorted list of dicts."""
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    """Returns a dictionary with the count of each character in the text."""
    chars = defaultdict(int)
    for c in text:
        lowered = c.lower()
        chars[lowered] += 1
    return chars


def get_book_text(path):
    """Reads and returns the content of the file at the given path."""
    with open(path, encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    main()