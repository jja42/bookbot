def get_text_words(text):
    words = text.split()
    return len(words)

def get_text_characters(text):
    char_count = {}
    for i in range(len(text)):
        s = text[i].lower()
        if(s in char_count):
            char_count[s] += 1
        else:
            char_count[s] = 1
    return char_count

def get_sorted_characters(dictionary):
    sorted_list = dictionary_to_list(dictionary)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def dictionary_to_list(dict):
    list = []
    for key in dict:
        new_dict = {}
        new_dict["key"] = key
        new_dict["value"] = dict[key]
        list.append(new_dict)
    return list

def sort_on(dict):
    return dict["value"]