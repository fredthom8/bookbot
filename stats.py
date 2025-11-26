def sort_on(items):
    return items["num"]

def get_word_count(text):
    text = text.split()
    return len(text)

def get_char_count(text):
    char_count = {}
    for c in text:
        c = c.lower()
        if c in char_count:
            char_count[c]+=1
        else:
            char_count[c]=1
    return char_count
        
def char_dict_sort(char_dict):
    char_dict_list = []
    for key in char_dict:
        char_dict_list.append({"char":key, "num":char_dict[key]})
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list