def solution(n):
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    return (f"{thousands[n // 1000]}{hundreds[(n % 1000)//100]}{tens[(n % 100)//10]}{units[n % 10]}")


print(solution(2314))
print(solution(3111))
print(solution(85))
print(solution(32))
print(solution(666))
print(solution(555))
print(solution(444))
print(solution(100))
