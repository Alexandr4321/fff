# num_1=int(input("С чего: "))
# num_2=int(input("C шагом: "))
# num_3=int(input("Сколько: "))
# list_1=[]
# count=0
# while count < num_3:
#     list_1.append(num_1)
#     num_1=num_1+num_2
#     count+=1
# print(list_1)

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)


# def calk2(a, b):
#     return a*b

# def math(oper, num , num2):
#    print(oper(num,num2))

# calk1=lambda a,b: a+b

# math(lambda a,b: a+b,9,9)


# list1=(1,2,3,5,8,15,23,38)
# def f(list1):
#     for i in range(len(list1)):
#         if list1[i] %2==0:
#             print(f"{list1[i],list1[i]*list1[i]}")
# f(list1)

# list2=[]
# for i in list1:
#     if i % 2==0:
#         list2.append((i,i*i))
# print(list2)

# data="25 53 75 4 567 85 5"
# print(data)

# data=list(map(int, data.split()))
# print(data)

# res=list(filter(lambda x: x%10==5, data))
# print(res)


# users=['user1', 'user2', 'user3', 'user4']

# data= list(enumerate(users))
# print(data)


# my_list1= '123456789'
# my_list2= 'qwertyuio'
# list1=list(my_list1)
# list2=list(my_list2)
# print(list1)
# print(list2)
# new_list=[]

# for i in range(len(list1)):
#     new_list.append((list1[i],list2[i]))
# print(new_list)

# new_list=(list(zip(list1,list2)))

# print(new_list)
# new_list='12jkl686;5mn5534'
# list1=list(new_list)

# my_list=list(filter(lambda x: x.isdigit() , list1))
# print(my_list)


# def funchion(charactiristic, objects):
#      my_list=set(map(charactiristic,objects))
#      print(my_list)
#      if len(my_list)==1:
#           return True
#      return False
# my_list=(8,2,2,400)

# print(funchion(lambda x: x%2==0, my_list))

# def rhythm(str):
#     str=str.split()
#     list = []
#     for word in str:
#         print(word)
#         result = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 result += 1
#         list.append(result)
#         print(list)
#         print(list[0])
#     return len(list) == list.count(list[0])

# print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')
# str = input()
# if rhythm(str):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


# def slogi(str):
#     str=str.split()
#     list1=[]
#     result=0
#     for word in str:
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 result+=1
#                 list1.append(result)
#     if(len(list1))==list1.count(list1[0]):
#         print('парам пам пам')
#     else :
#           print('пам парам')

# str=input()
# slogi(str)


def oper(row, col):
    c1 = 0
    c2 = 0
    while c1 < row:
        c2 = 1
        print()
        c1 += 1
        while c2 < col+1:
            print(c1*c2, end='   ')
            c2 += 1
oper(6, 6)

print('\n' '///////////////////////////////////////////')
def oper(operat, row, col):
    c1 = 0
    c2 = 0
    while c1 < row:
        c2 = 1
        c1 += 1
        print()
        while c2 < col+1:
            print(operat(c1,c2),end='   ')
            c2 += 1


operat=lambda x,y: x*y
oper(operat, 6, 6)