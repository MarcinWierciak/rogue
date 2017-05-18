import random
import sys

lista = []
lista2 = []
hint = []

def hot_warm():
    lista = []
    #lista2 = []

    for i in range(3):
        lista.append(random.randint(0,9))
        if lista[i] == lista[i-1]:
            lista[i]=random.randint(0,9)

    print(lista)

    while True:

        user_number = input("Enter a 3digit number:")
        hint = []
        lista2
        while user_number != int and len(user_number) != 3:

            user_number = list(input("Enter a 3digit number:"))
        for i in user_number:
            lista2.append(int(i))
        for i in range(3):
            print(lista2[i])
            if lista2[i] in lista:
                if lista2[i] == lista[i]:
                    hint.append("hot")
                else:
                    hint.append("warm")
            else:
                hint.append("cold")

        print(*hint)

        if lista2 == lista:
            print("<3")
            sys.exit()
