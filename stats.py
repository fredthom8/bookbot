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
        
