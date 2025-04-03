def num_words_in_str(str):
    string_list = str.split()

    return len(string_list)

def count_chars(str):
    char_hash = {}
    str = str.lower()
    for i in range(len(str)):
        if char_hash.get(str[i]):
            char_hash[str[i]] = char_hash[str[i]] + 1
        else:
            char_hash[str[i]] = 1

    return char_hash

def sort_dict(dict):
    new_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)

    return new_dict
