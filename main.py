'''Задача 1'''
# num=int(input("Введите трехзначное число:"))
# a=num//100
# b=(num%100)//10
# c=num%10
# sum=a+b+c
# print(sum)
'''Задача 2'''
# num=int(input("Введите число:"))
# a=num//3
# b=a//2
# c=b+(num//2)
# print(f"Катя {c}")
# print(f"Петя {b}")    
# print(f"Сережа {b}")
'''Задача 3'''
# num=int(input("Введите шестизначный код с билета :"))
# a=num//100000
# b=(num//10000)%10
# c=(num//1000)%10
# d=(num//100)%10
# e=(num//10)%10
# f=num%10
# if((a+b+c)==(d+e+f)):
#    print("У вас счастливый билет!!!")
# else:
#    print("У вас не счастливый билет, gовезет в сдедующий раз")

# my_limit=int(input("Введите предел факториала "))
# fact = 1
# count = 1
# while count <=my_limit:
#     fact*=count
#     count+=1
# print(fact)

# n1=0
# n2=1
# k=1
# a=int(input("Введите число фибоначи"))
# while n2<a:
#     n1,n2=n2,n2+n1
#     k+=1
# if n2!=a:
#     print("-1")
# else:
#     print(k)


# arbus=30
# i=0
# min_ar=30000
# max_ar=100
# while(i<arbus):
#     ves=random.randint(100,30000)
#     print(ves,end=' ,')
#     i+=1
#     if(ves>max_ar):
#         max_ar=ves
#     if(ves<min_ar):
#         min_ar=ves
# print(f"\nCебе:{max_ar} Теще:{min_ar}")


# import random

# money=int(input("Введите количество монет: "))
# i=0
# count0=0
# count1=0
# while(i<money):
#     copeika=random.randint(0,1)
#     print(f"({copeika})",end=' ')
#     i+=1
#     if(copeika==0):
#         count0+=1
#     else: 
#         count1+=1
# if (count0<count1):
#     print(f"\nПроще перевернуть {count0} монеток решка")
# else:
#     print(f"\nПроще перевернуть {count1} монеток орел")


# x = int(input())
# y = int(input())
# for i in range(x):
#    for j in range(y):
#        if x == i + j and y == i * j:
#            print(i, j)

# num=int(input("Число  "))
# num2=1
# while num2<num:
#     print(num2,end=" ")
#     num2+=num2
    
