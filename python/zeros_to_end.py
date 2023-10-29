"""Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

lst = [1, 23, 67, 0, 1, 2, 3, 5, 3, 1, 0, 3]


def move_zeros(lst):
    new_lst = []
    zero_count = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            new_lst.append(lst[i])
        else:
            zero_count += 1

    for z in range(zero_count):
        new_lst.append(0)

    return new_lst


print(move_zeros(lst))
