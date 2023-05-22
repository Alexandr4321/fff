# list_1=[0, 88, 6, 3 , 10]
# # print(list_1)
# # for i in range(5):
# #     list_1.append(i)
# #     print(list_1)
# #print(list_1.insert(2,22))
# print(list_1[len(list_1)-1])

# # list_numbers=[0, 88, 6, 3 , 10, 3, 12, 6, 1]
# print(list_numbers)
# list_unic_numbers=[]
# list_unic_numbers=set(list_numbers)
# len(list_unic_numbers)
# print(list_numbers)
# print(len(list_unic_numbers))


# list_numbers=list(input())
# uniq_list=[]
# for item in list_numbers:
#     if not item in uniq_list:
#         uniq_list.append(item)
# print(list_numbers)
# print(uniq_list)
# print(len(uniq_list))

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# per=int(input())
# i=0
# while(i<per):
#     num_list.append(num_list.pop(0))
#     i+=1
# print(num_list)

# num_list = [1, 1, 3, 4, 2, 6, 7, 1, 9]
# leng = len(num_list)-1
# count = 0
# for i in range(leng):
#     if num_list[i] < num_list[i+1]:
#         count += 1
# print(count)

# list_numbers =[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, 
#                  {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# new_list=[]
# new_new=[]
# for item in list_numbers:
#     new_list.append(list(item.values()))
# p=len(new_list)
# for item in new_list:
#     if not item in new_new:
#        new_new.append(item)
       
# print(new_list)
# print(new_new)





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
#     print(f"есть такое число {count}")
# else:
#     print(f"самое близкое {res}")
# list_numbers =[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, 
#                  {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# new_list=[]
# new_new=[]
# for item in list_numbers:
#     new_list.append(list(item.values()))
# p=len(new_list)
# for item in new_list:
#     if not item in new_new:
#        new_new.append(item)
       
# print(new_list)
# print(new_new)

# list_numbers =[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, 
#                  {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# uniq=set()
# for item in list_numbers:
#     for value in item.values():
#         uniq.add(value)
# print(uniq)

azb= {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JX',
      	10:'QZ'}

word= input("Слово: ").upper()
print(sum([k for i in word for k, v in azb.items() if i in v]))


















