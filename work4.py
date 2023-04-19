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
