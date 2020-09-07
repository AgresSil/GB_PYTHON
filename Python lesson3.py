# def my_f(var1, var2):
#     if var1 == 0 or var2 == 0:
#         print("Oшибка! Деление на ноль! ")
#         return
#     s = var1 / var2
#     print(f"Сумма - {s}")
#
# my_f((int(input("Введите первое число - "))), (int(input("Введите второе число - "))))
# *************************2***********
# def my_f():
#     name= (input("Имя: ")+ " ")
#     surname = (input("Фамилия: ")+ " ")
#     birth = (input("Год рождения: ")+ " ")
#     city = (input("Город проживания: ")+ " ")
#     mail = (input("Почта: ")+ " ")
#     phone = (input("Номер телефона: ")+ ".")
#     s = [name +surname + birth + city + mail + phone]
#     print(s)
# my_f()
# ************************3************
# def my_funс(num1,num2,num3):
#     num1=(int(input("Введите первое число - ")))
#     num2=(int(input("Введите второе число - ")))
#     num3=(int(input("Введите третье число - ")))
#     mylist=[num1,num2,num3]
#     try:
#         mylist.pop(mylist.index(min(mylist)))
#         return sum(mylist)
#     except TypeError:
#         return "Только числа! "
# print(my_funс(0,0,0))

# НЕКОРРЕКТНО РАБОТАЕТ "except". Подскажите, пожалуйста, что нужно исправить? И еще вопрос -
# почему программа работает, только если в конце "print(my_funс(0,0,0))"? Так и должно быть?
# ************************4********
# def my_func(x=int(input("Введите первое число - ")), y=int(input("Введите второе число -"))):
#     y = abs(y)
#     s = x ** y
#     return s
# print(my_func())
# *************4 ВТОРОЙ ВАРИАНТ****
# def my_func(x=int(input("Введите первое число - ")), y=int(input("Введите второе число -"))):
#     y = abs(y)
#     i = 1
#     while i != y:
#         s = x * x
#         i += 1
#
#     return s
#
# print(my_func())
# ********************5***********
# m = 0
# x = False
#
# while not x:
#     s = input("Введите число (для выхода введите m): ")
#     tk = s.split()
#     for t in tk:
#         if t == "m":
#             x = True
#             break
#         try:
#             i = int(t)
#             m += i
#         except ValueError:
#             pass
#     print("Сумма чисел: ", m)


# *********************6**************
#
# def int_func():
#     t = (input("Введите текст: "))
#     return t.title()
# print (int_func())
