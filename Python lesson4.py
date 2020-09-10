# from sys import argv
# def wage():
#     try:
#         time, rate, premium= map(int, argv[1:])
#         print (f"Сумма - {time*rate+premium}")
# wage()
# *********************************2***********

# l=[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_l=[l[i] for i in range(len(l))if l[i]> l[i-1]]
# print(new_l)
# **********************************3*********
# my_list = [i for i in range(20, 241) if i % 21 == 0 or i % 20 == 0]
# print(my_list)
# ***********************************4**********
# list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# my_list = []
# my_list = [i for i in list1 if list1.count(i) == 1]
# print(my_list)
# ***ВАРИАНТ РЕШЕНИЯ, ЕСЛИ НУЖНО ОСТАВИТЬ ОДИН ЭЛЕМЕНТ, ИЗ ПОВТОРЯЮЩИХСЯ

# list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# my_list = []
# [my_list.append(i) for i in list1 if i not in my_list]
# print(my_list)
# ********************************5****************
# from functools import reduce
#
# print(f"Сумма {reduce(lambda num1, num2: num1 * num2, [i for i in range(100, 1001) if i % 2 == 0])}")

# *********************************6*************
#from itertools import cycle, count

#
# for i in count(int(3)):
#     print(i)
#     if i == 10:
#         break

# my_list = (input("число - ")).split()
# quit = "q"
# while quit != True:
#     cycler = cycle(my_list)
#     cycler = (input("число - "))
#     if cycler == "q":
#         quit = True
#         break
#     print(cycler)
