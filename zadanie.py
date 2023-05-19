def writeInList(list, line):
    word=''
    for symbol in line:
        if symbol != ' ':
            word += symbol
        else:
            list.append(word)
            word = ''
def check():
    if result>=list1[2]:
        return 1
    elif list2[2]<=result<list1[2]:
        return 2
    elif list3[2]<=result<list2[2]:
        return 3
    elif list4[2]<=result<list3[2]:
        return 4
    elif list5[2]<=result<list4[2]:
        return 5
    elif list6[2]<=result<list5[2]:
        return 6
    elif list7[2]<=result<list6[2]:
        return 7
    elif list8[2]<=result<list7[2]:
        return 8
    elif list9[2]<=result<list8[2]:
        return 9
    elif list10[2]<=result<list9[2]:
        return 10
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
name = input("Введите ваше имя: ")
result = input("Введите ваш результат: ")
with open('results.txt', 'r', encoding='UTF-8') as file:
    writeInList(list1, file.readline())
    writeInList(list2, file.readline())
    writeInList(list3, file.readline())
    writeInList(list4, file.readline())
    writeInList(list5, file.readline())
    writeInList(list6, file.readline())
    writeInList(list7, file.readline())
    writeInList(list8, file.readline())
    writeInList(list9, file.readline()) 
    writeInList(list10, file.readline())
if check() == 1:
    list10 = ['10', list9[1], list9[2]]
    list9 = ['9', list8[1], list8[2]]
    list8 = ['8', list7[1], list7[2]]
    list7 = ['7', list6[1], list6[2]]
    list6 = ['6', list5[1], list5[2]]
    list5 = ['5', list4[1], list4[2]]
    list4 = ['4', list3[1], list3[2]]
    list3 = ['3', list2[1], list2[2]]
    list2 = ['2', list1[1], list1[2]]
    list1 = ['1', name, result]
elif check() == 2:
    list10 = ['10', list9[1], list9[2]]
    list9 = ['9', list8[1], list8[2]]
    list8 = ['8', list7[1], list7[2]]
    list7 = ['7', list6[1], list6[2]]
    list6 = ['6', list5[1], list5[2]]
    list5 = ['5', list4[1], list4[2]]
    list4 = ['4', list3[1], list3[2]]
    list3 = ['3', list2[1], list2[2]]
    list2 = ['2', name, result]
elif check() == 3:
    list10 = ['10', list9[1], list9[2]]
    list9 = ['9', list8[1], list8[2]]
    list8 = ['8', list7[1], list7[2]]
    list7 = ['7', list6[1], list6[2]]
    list6 = ['6', list5[1], list5[2]]
    list5 = ['5', list4[1], list4[2]]
    list4 = ['4', list3[1], list3[2]]
    list3 = ['3', name, result]
elif check() == 4:
    list10 = ['10', list9[1], list9[2]]
    list9 = ['9', list8[1], list8[2]]
    list8 = ['8', list7[1], list7[2]]
    list7 = ['7', list6[1], list6[2]]
    list6 = ['6', list5[1], list5[2]]
    list5 = ['5', list4[1], list4[2]]
    list4 = ['4', name, result]
elif check() == 5:
    list10 = ['10', list9[1], list9[2]]
    list9 = ['9', list8[1], list8[2]]
    list8 = ['8', list7[1], list7[2]]
    list7 = ['7', list6[1], list6[2]]
    list6 = ['6', list5[1], list5[2]]
    list5 = ['5', name, result]
elif check() == 6:
    list10 = ['10', list9[1], list9[2]]
    list9 = ['9', list8[1], list8[2]]
    list8 = ['8', list7[1], list7[2]]
    list7 = ['7', list6[1], list6[2]]
    list6 = ['6', name, result]
elif check() == 7:
    list10 = ['10', list9[1], list9[2]]
    list9 = ['9', list8[1], list8[2]]
    list8 = ['8', list7[1], list7[2]]
    list7 = ['7', name, result]
elif check() == 8:
    list10 = ['10', list9[1], list9[2]]
    list9 = ['9', list8[1], list8[2]]
    list8 = ['8', name, result]
elif check() == 9:
    list10 = ['10', list9[1], list9[2]]
    list9 = ['9', name, result]
elif check() == 10:
    list10 = ['10', name, result]
with open('results.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{list1[0]} {list1[1]} {list1[2]}\n{list2[0]} {list2[1]} {list2[2]}\n{list3[0]} {list3[1]} {list3[2]}\n{list4[0]} {list4[1]} {list4[2]}\n{list5[0]} {list5[1]} {list5[2]}\n{list6[0]} {list6[1]} {list6[2]}\n{list7[0]} {list7[1]} {list7[2]}\n{list8[0]} {list8[1]} {list8[2]}\n{list9[0]} {list9[1]} {list9[2]}\n{list10[0]} {list10[1]} {list10[2]}')