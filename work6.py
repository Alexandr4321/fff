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

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input())
max_number = int(input())
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)