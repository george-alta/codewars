# 6 kyu Duplicate Encoder

def duplicate_encode(word):
    new_string = ''

    def count_char_in_string(char, string):
        count = 0
        for c in string.lower():
            if c == char.lower():
                count += 1
        if count > 1:
            return True
        else:
            return False

    for l in word:
        if count_char_in_string(l, word):
            new_string = new_string + ")"
        else:
            new_string = new_string + "("
    return (new_string)


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))
