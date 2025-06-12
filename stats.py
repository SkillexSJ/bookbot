def count_word(text):
    word = text.split()
    return len(word)

def count_char(text):
    word = text.lower()
    char_count = {}

    for i in word:
        if i in char_count:
            char_count[i]+=1

        else:
            char_count[i] = 1 

    return char_count


def sort_it(dict):
    char_list = [{"char": char, "num": count} for char, count in dict.items()]
    char_list.sort(key=lambda x: x["num"] , reverse=True)

    return char_list

