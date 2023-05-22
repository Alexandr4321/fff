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


# list_1=[1,7,3,9,5]
# list_2=[6,7,8,9,0]
# list_3=list()

# l=len(list_1)
# l2=len(list_2)
# for i in list_1 :
#     if i not in list_2:
#             list_3.append(i)
# print(list_3)
            




# list_1=[2,8,7,4,3,6,7,5,8,10,3,8]
# # for i in range(1,len(list_1)-1):
# #     if list_1[i-1]<list_1[i]>list_1[i+1]:
# #         print(list_1[i],end =' ')
# [print(list_1[i]) for i in range(1,len(list_1)-1)  if list_1[i-1]<list_1[i]>list_1[i+1]]





# list_1=[1,1,2,2,2,8,5,6,3,3,4,4,1,1]

# def uniq_dictionary(list_1):
#     uniq_dict={}
#     for number in list_1:
#         uniq_dict[number]=uniq_dict.get(number,0)+1
#     print(uniq_dict)
#     return uniq_dict

# def uniq_pairs(dict_n: dict, count=0):
#     for values in dict_n.values():
#             count+=values//2
#     return count
# a=(uniq_pairs(uniq_dictionary(list_1)))

# print(a)
# number=220
# sum=0
# while number<2840:
#  #  def summarize(number,sum=0):
#        for item in range(1,number//2+1):
#           if number%item==0:
#               sum+=item
#        print(sum,end=' ')
#        number+=1


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
