def count_of_words_in_text(file_content: str) -> int:
    list = file_content.split()
    return len(list)

def count_characters(file_content: str) -> dict:
    character_dict = {}
    text_with_lowered_case = file_content.lower()
    for ch in text_with_lowered_case:
        if ch in character_dict:
            character_dict[ch] += 1
        else:
            character_dict[ch] = 1
    sorted_dict_by_values = sorted(character_dict.items(),key = lambda x:x[1], reverse=True)
    converted_dict = dict(sorted_dict_by_values)
    return converted_dict

def sorted_by_alphabetical_order(input_dict):
    string_in_column = ""
    for ch in input_dict:
        if ch.isalpha():
            string_in_column += str(ch)+": "+str(input_dict[ch])+"\n"
    return string_in_column[:-1]
        






if __name__ == "__main__":
    print("This is script")