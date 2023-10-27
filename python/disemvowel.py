def disemvowel(string_):
    new_string = ""
    for char in string_:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            new_string = new_string + char
    return new_string
