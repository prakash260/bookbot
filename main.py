import collections

def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    file_lower = text.lower()
    dict_val = count_characters(file_lower)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    for key, value in dict_val:
        if not key.isalpha():
            continue
        print("The {key} character was found {value} times".format(key=key, value=value))
    print("--- End report of books/frankenstein.txt ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    counter = dict(collections.Counter(text))
    sorted_counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    return sorted_counter
    
    


if __name__ == '__main__':
    # main("./books/frankenstein.txt")
    main()