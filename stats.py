def count_words(book):
    book = book.split()
    word_count = 0
    for work in book:
        word_count += 1
    return word_count
def sort_on(items):
    return items["num"]

def count_characters(book):
    book = book.lower()
    #book = book.split()
    character_dic = {}
    for letter in book:
        if letter in character_dic:
            character_dic[letter] += 1
        else:
            character_dic[letter] = 1


    return character_dic

def dic_list(dic):
    result = []

    for k,v in dic.items():
        result.append({"char": k, "num": v})

    result.sort(reverse=True, key=sort_on)
    return result