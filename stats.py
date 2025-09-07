def word_count(content_string):
    words_list = content_string.split()
    if __name__ == "main":
        print(words_list[0:100])
    return len(words_list)

def char_count(content_string):
    
    #First Convert the string to lowercase
    lower_string = content_string.lower()
    
    #now loop through the lowercase string checking whether the char exists
    #in the dictionary, and then incrementing the count if it does
    char_count_dict = {}

    for char in lower_string:
        if char in char_count_dict:
            char_count_dict[char] = char_count_dict[char] + 1
        else:
            char_count_dict[char] = 1

    return char_count_dict