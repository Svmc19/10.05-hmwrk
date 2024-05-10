# Task1
# def find_odd(nums):
#     for x in nums:
#         if nums.count(x) % 2 !=0:
#             return x
#
# print(find_odd([1,1,2,-2,5,2,4,4,-1,-2,5]))

# Task2
# def filter_list(lst):
#     lst1 = []
#     for x in lst:
#         if type(x) == int:
#             lst1.append(x)
#     return lst1
#
#
#
# print(filter_list([1,2,"a","b"]))
# print(filter_list([1,"a","b",0,15]))
# print(filter_list([1,2,"aasf",1,"123",123]))

# Task3
# def nums(lst):
#     first = lst[0]
#     middle = lst[1:-1]
#     last = lst[-1]
#     print(first)
#     print(middle)
#     print(last)
#
# print(nums([1,2,3,4,5,6])

# Task4
# def st(lst):
#     result = 0
#     for x in lst:
#         d = len(x)
#         result+=d
#     return result
#
#
#
# print(st(["###","###","###"]))

# Task5 ------way1
# def nums(lst,num):
#     lst1 =[]
#     lst2 = []
#     for x in lst:
#         if x == num:
#             lst1.append(x)
#         else:
#             lst2.append(x)
#     lst2.extend(lst1)
#     return lst2
# print(nums([1,1,2,1,3,4],1))
# ---------way2
# def nums(lst,num):
#     lst1 = lst
#     for x in lst:
#         if x == num:
#             p =lst.pop(lst.index(num))
#             lst1.append(p)
#     return lst1
#
# print(nums([1,2,1,1,3,4],1))
