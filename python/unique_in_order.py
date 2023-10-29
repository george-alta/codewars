"""
6 kyu
Unique In Order
Instructions

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""


def unique_in_order(sequence):
    new_list = [sequence[0]]
    for char in sequence[1:]:
        if char != new_list[-1]:
            new_list.append(char)
    return new_list


print(unique_in_order("AAAABBBCCDAABBB"))
print(unique_in_order("ABBCcAD"))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order((1, 2, 2, 3, 3)))
