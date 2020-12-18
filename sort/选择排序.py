# def selectSort(list):
#
#     for i in range(len(list)):
#         min_index = i
#         for j in range(i+1, len(list)):
#             if list[j] < list[min_index]:
#                 min_index = j
#                 list[min_index], list[i] = list[i], list[min_index]
#
#     return list
#
#
# print(selectSort([1, 5, 3, 9, 2]))

fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
for i in range(10):
    print(fib(i))
