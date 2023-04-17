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

azb= {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JX',
      	10:'QZ'}

word= input("Слово: ").upper()
print(sum([k for i in word for k, v in azb.items() if i in v]))