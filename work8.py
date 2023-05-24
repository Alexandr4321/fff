def read ():
    file=open('text.txt', 'r', encoding='utf-8') 
    print(file.read())
    file.close()

def inp ():
    file=open('text.txt', 'a', encoding='utf-8')
    name=input('Имя: ')
    surname=input('Фамилия: ')
    phone=input('Номер: ')
    file.write(f"{name} {surname}: {phone}\n")
    file.close()

def goog():
    read()
    print()
    word=input('Введите данные: ')
    file=open('text.txt', 'r', encoding='utf-8')
    strings= file.readlines()
    for string in strings:
        if word in string:
            print(string)
    file.close()


print('Посмотреть: 1\n'
      'Добавить: 2\n'
      'Поиск: 3\n')
res=int(input())
if res==1:
    read()
if res==2:
    inp()
if res==3:
    goog()