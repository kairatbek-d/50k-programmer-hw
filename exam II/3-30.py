# # 3
# class Student:
#     def __init__(self, name, course):
#         self.name = name
#         self.course = course

# student_1 = Student('Asel', 'Python')
# student_2 = Student('Asel', 'Python')
# x = student_1 == student_2
# print(x) # False

# 7
# class Client:
#     def __init__(self, name, bill, credit_cart):
#         self.name = name
#         self._bill = bill # protected - can access self and childs
#         self.__credit_cart = credit_cart # private

# client_1 = Client('Asel', 100, 1234123412341234)
# print(client_1.__credit_cart) # Attribute error
# print(client_1._Client__credit_cart) # 1234123412341234

# как называется функция которая возвращает список содержащий пространство имен в объект
# globals


# # 14
# if True>False<=False:
#     print(True) # Trues

# # 15
# a = 0
# b = False
# c = a>b
# d = c == False
# x = a or b or c or d or None
# print(x) # True

# # 16
# lst =[0]
# for i in range(10):
#     if i%5!=0:
#         lst.append(i)
# x = max(lst) - min(lst)
# print(x) # 9

# # 17
# i = 2
# for i, item in enumerate([10, 20, 30], 5):
#     print(i, item, sep="-") # 5-10 6-20 7-30

# # 18
# def m(a, b):
#     return a*b
# def s(a, b):
#     return a+b
# c = True
# res = (m if c else s)(100, 23)
# print(res) # 2300

# # 19
# a = 10
# def func(a):
#     a = 100
# func(a)
# print(a) # 10

# # 20
# a, *b, c = 1, 2, 3, 4, 5, 6
# print(a) # 1
# print(b) # [2, 3, 4, 5]
# print(c) # 6

# # 21
# def foo(*args, **kwargs):
#     return kwargs
# print(foo()) # {}

# # 23
# def foo(n):
#     while n:
#         yield '$' * n
#         n -= 1
# x = foo(5)
# print(x) # genereator