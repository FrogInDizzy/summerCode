def is_substring(main_string, sub_string):
    sub_length = len(sub_string)
    main_length = len(main_string)

    for i in range(main_length - sub_length + 1):
        if main_string[i:i+sub_length] == sub_string:
            return True
    
    return False

print(is_substring("rat", "labtorary"))