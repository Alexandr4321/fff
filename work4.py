import random
count_1=int(input())
count_2=int(input())
list_1=list()
list_2=list()
while count_1>0:
    new=random.randint(0,20)
    list_1.append(new)
    count_1-=1
    while count_2>0:
            new_1=random.randint(0,20)
            list_2.append(new_1)
            count_2-=1

list_3=list()

for i in range (len(list_1)):
    for item in range(len(list_2)):
        if list_1[i] == list_2[item]:
            list_3.append(list_1[i])
print(list_1)
print(list_2)

print(sorted(set(list_3)))