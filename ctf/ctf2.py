from typing import List


def numbers(num: int) -> List[int]:  # 123 -> [1,2,3]
    str_num = str(num)
    num_array = []
    for char in str_num:
        num_array.append(int(char))
    return num_array


def luhn(card_num: int) -> bool:
    card_numbers = numbers(card_num)
    two_one = [2, 1] * 8
    summ = 0
    for card, luhn_num in zip(card_numbers, two_one):
        mult = card * luhn_num
        check = mult
        if mult >= 10:
            check = sum(numbers(mult))
        summ += check
    return summ % 10 == 0


must_divide_by = 123457
partial_card_number = "543210******1234"

l = 5432100000001234
r = 5432109999991234
# smallest = 0
# for i in range(l, r):
#     if i % must_divide_by == 0:
#         smallest = i
#         break
print("start")
for i in range(l, r, 10_000):
    if i % must_divide_by == 0 and luhn(i):
        print(i)
