# import itertools
# from itertools import count
# yield. fibonachi sonlar
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
# for num in fibonacci(8):
#     print(num, end=" ")

# yield. Har bir harfni boshqa harflar bilan yonmayon qoʻyadi
# def letter_pairs(letters):
#     for i in letters:
#         for j in letters:
#             if i != j:
#                 yield i + j
#
# for pair in letter_pairs("ABC"):
#     print(pair, end=" ")

# Generator comprehension bilan
# squares = (x**2 for x in range(20) if x % 2 == 0)
# print(list(squares))

# l harfi bor soʻzlarning uzunligini chiqaradi
# words = ["Ali", "Hasan", "Vali", "Sardor"]
# lengths = (len(w) for w in words if "l" in w)
# print(list(lengths))

# cheksiz sonlar generatori
# infinite_numbers = iter(lambda: 1, 2)
# print(next(infinite_numbers))  # 1


#: itertools.count() bilan cheksiz generator
from itertools import count
gen = count(10, 5)
for i in range(5):
    print(next(gen))

