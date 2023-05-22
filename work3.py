# num_list = [1, 21, 3, 18, 20, 6, 5, 8, 489]
# per=int(input())
# leng=len(num_list)
# count=0
# min_n=max(num_list)*9
# for i in range(leng):
#     if num_list[i]==per:
#         count+=1
#     else :
#         for i in range(leng):
#             num=abs(per-num_list[i])
#             if num<min_n:
#                min_n=num
#                res=num_list[i]
# if count!=0:      
#     print(f"есть такое значение {count}")
# else:
#     print(f"этого значения нет , самое близкое {res}")

# azb= {1:'AEIOULNSTR',
#       	2:'DG',
#       	3:'BCMP',
#       	4:'FHVWY',
#       	5:'K',
#       	8:'JX',
#       	10:'QZ'}

# word= input("Слово: ").upper()
# print(sum([k for i in word for k, v in azb.items() if i in v]))


# scrabble= {1:'AEIOULNSTR',
#       	2:'DG',
#       	3:'BCMP',
#       	4:'FHVWY',
#       	5:'K',
#       	8:'JX',
#       	10:'QZ'}

# word=input()
# total=0
# for letter in word.upper():
#     for points ,letters in scrabble.items():
#         if letter in letters:
#             total+=points
#             break
# print(f'Слово {word.upper()} стоит {total}')


# word=list(input())
# print(word[0], end=" ")
# for i in range(1,len(word)):
#     print(word[i], end=" ")
#     count=word[:i-1].count(word[i])
#     if count > 0:
#         print(f"_{count}", end=" ")


# count_dict={}
# for letter in word:
#     count_dict[letter]=count_dict.get(letter,0)+1

# print(f'{letter}'if count_dict.get(letter)<2 else f'{letter}_{count_dict.get(letter)-1}', end=' ')


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
















