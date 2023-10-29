# simple pig latin


def pig_it(text):
    # your code here
    array = text.split()
    new_words = []
    for word in array:
        if word.isalpha():
            str = "".join(word[1:]) + word[0] + "ay"
            new_words.append(str)
        else:
            new_words.append(word)

    return " ".join(new_words)


print(pig_it("hola que hace"))
print(pig_it("Pig latin is cool"))
print(pig_it("This is my string"))
print(pig_it("Hello world !"))
