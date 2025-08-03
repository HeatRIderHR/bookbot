def get_num_words(words):
    return len(words)

def get_tcotal_charaters(text):
    lowerText = text.lower()
    charactersDict = {}
    for character in lowerText:
        if character in charactersDict:
            charactersDict[character] += 1
        else:
            charactersDict[character] = 1
    return charactersDict

def sort_on(items):
    return items["num"]

def sorted_dic_to_list(dict_items):
    text = ""
    new_list = []
    for item in dict_items:
        new_list.append({"char": item, "num": dict_items[item]})
    new_list.sort(reverse=True, key=sort_on)
    
    for content in new_list:
        if content["char"].isalpha():
            text += f"{content['char']}: {content['num']}\n"
    return text