import os
from termcolor import colored

def check(a,b):
    c = 0
    word = ""
    for i in a:
        if(str(a[c])==str(b[c])):
            word += colored(f'{b[c]}','green')
        elif((a[c]!=b[c])&(b[c]in a)):
            word += colored(f'{b[c]}','yellow')
        else:
            word += b[c]
        c+=1
    print(word)
    


word=str(input("Слово другому игроку: "))
word = word.lower()
if(len(word)==5):
    os.system('cls')
    attempt = 6
    while attempt!=0:
        answer = input("Введите свое слово: ")
        if(len(answer)==5):
            answer = answer.lower()
            check(word,answer)
            attempt-=1
            if(answer==word):
                print("Вы угадали слово!")
                break
        else:
            print("Вы ввели больше/меньше пяти букв")
            break
    else:
        print("Вы потратили все попытки")
else:
    print("Вы ввели больше/меньше пяти букв")



