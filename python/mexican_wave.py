# mexican wave

def wave(people):
    people.lower()
    new_array = []

    for i in range(len(people)):
        if people[i] != " ":
            str = "". join(people[:i]) + \
                people[i].upper() + "". join(people[i+1:])
            new_array.append(str)
    return new_array


print(wave('holanda'))
