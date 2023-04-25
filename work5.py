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







num1=int(input())
num2=int(input())
count=0
min_n=min(num1,num2)
max_n=max(num1,num2)

def summa(max_n,min_n,count):
    if min_n==count:
        return print(max_n)
    else:
        max_n+=1
        count+=1
    summa(max_n,min_n,count)
summa(max_n,min_n,count)