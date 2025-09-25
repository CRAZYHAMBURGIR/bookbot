def get_num_words(path_to_file):
    num_words = 0
    with open(path_to_file) as f:
        text = f.read()
        words = text.split()
        for words in words:
            num_words += 1
            
    return num_words


def sort_on(d):
    return d["num"]

def individual_count(path_to_file):
    num_all = {}
    is_present = False
    with open(path_to_file) as f:
        text = f.read()
        letters = text.lower()
        for letter in letters:
            is_present = letter in num_all
            if is_present == False:
                num_all[letter] = 1
            elif is_present == True:
                num_all[letter] += 1
    return num_all

def result_print(num_all):
    return

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list