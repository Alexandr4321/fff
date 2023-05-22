# import random
# count_1=int(input())
# count_2=int(input())
# list_1=list()
# list_2=list()
# while count_1>0:
#     new=random.randint(0,20)
#     list_1.append(new)
#     count_1-=1
#     while count_2>0:
#             new_1=random.randint(0,20)
#             list_2.append(new_1)
#             count_2-=1

# list_3=list()

# for i in range (len(list_1)):
#     for item in range(len(list_2)):
#         if list_1[i] == list_2[item]:
#             list_3.append(list_1[i])
# print(list_1)
# print(list_2)

# print(sorted(set(list_3)))


# list_1=list()
# num=int(input("Длина "))
# for i in range(num):
#     x=int(input())
#     list_1.append(x)
# print(list_1)

# list_2=list()
# for i in range(len(list_1)-2):
#     list_2.append(list_1[i]+list_1[i+1]+list_1[i+2])
# list_2.append(list_1[0] + list_1[len(list_1)-2]+ list_1[len(list_1)-1])
# list_2.append(list_1[0] + list_1[1]+ list_1[len(list_1)-1])
# print(list_2)
# print(max(list_2))


# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:]if i <= pivot]
#     greater = [i for i in array[1:]if i > pivot]
#     return quick_sort(less)+[pivot]+quick_sort(greater)


# print(quick_sort([4, 5, 3, 2, 7, 8, 5, 21, 11]))


# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums)//2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i<len(left) and j<len(right):
#             if left[i]<right[j]:
#                 nums[k]=left[i]
#                 i+=1
#             else:
#                 nums[k]=right[j]
#                 j+=1
#             k+=1

#         while i < len(left):
#             nums[k]=left[i]
#             i+=1
#             k+=1
#         while j < len(right):
#             nums[k]=right[j]
#             j+=1
#             k+=1

# list1=[1,4,2,7,9,55,4,32,2,1]
# merge_sort(list1)
# print(list1)

# n=4
# def fibo(n):
#     if n == 0 or n == 1:
#         return 1
#     return fibo(n-2)+fibo(n-1)

# print (fibo(n))


# list_1=[3,3,4,5,3,2,4,2,5,2,5]
# print(list_1)
# for i in range(len(list_1)):
#     if list_1[i] == 2:
#         list_1[i]= 5
# print(list_1)


# import random

# mark_list = [random.randint(1,5) for _ in range (10)]
# print(mark_list)
# mark_list=[min(mark_list)if i ==max(mark_list) else i for i in mark_list]
# print(mark_list)

# # number= int(input())

# # def is_simple(num:int) -> bool:
# #     if num in [1,2]:
# #         return True
# #     for i in range(3, num//2+1,2):
# #         if num%i==0:
# #             return False
# #     return True
# # print (is_simple(number))

# n='qwerty'
# def requr(s):
#     if len(s)== 1:
#         return s    
#     return s[-1]+requr(s[:-1])
# print(requr(n))

# num = int(input('Число '))
# step = int(input('Степень '))
# res=num
# count=1
# def Proiz (num , step, res, count):
#     res=res*num
#     count+=1
#     if count == step:  
#        return print(res)
#     Proiz(num,step,res, count)
# Proiz(num,step,res, count)

# num1=int(input())
# num2=int(input())
# count=0
# min_n=min(num1,num2)
# max_n=max(num1,num2)

# def summa(max_n,min_n,count):
#     if min_n==count:
#         return print(max_n)
#     else:
#         max_n+=1
#         count+=1
#     summa(max_n,min_n,count)
# summa(max_n,min_n,count)
def rhythm(str):
    str = str.split()
    list = []
    for word in str:
        result = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                result += 1
        list.append(result)
    return len(list) == list.count(list[0])

print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')
str = input()
if rhythm(str):
    print('Парам пам-пам')
else:
    print('Пам парам')
    