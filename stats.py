def get_num_words(book_text):
    all_words = book_text.split()
    return len(all_words)

def get_num_car(book_text):
    char_dict = {}
    lower_cars = book_text.lower()
    for char in lower_cars: 
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def get_sorted_char(num_char):
    list_dict = []
    for char in num_char:
        small_dict = {
            "char": char,
            "num": num_char[char]
            }
        list_dict.append(small_dict)
    def sort_on(dict):
        return dict["num"]
    
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict
    





