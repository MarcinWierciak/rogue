from random import randint

def hot_and_cold_game():
    dupa = 0
    random_number = []
    while len(random_number) != 3:
        num = randint(0, 9)
        if num not in random_number:
            random_number.append(str(num))

    random_number = ''.join(random_number)
    print(random_number)

    while True:
        guess_number = input("\nGuess a 3digit number: ")

        while not guess_number.isdigit() or len(guess_number) != 3:
            guess_number = input("\n3-DIGIT INTEGER please! ")

        guess_number = list(guess_number)


        printing_result = []

        for i, elem in enumerate(guess_number):
            if elem in random_number:
                if elem == random_number[i]:
                    printing_result.insert(0, 'hot')
                else:
                    printing_result.append('warm')
            else:
                printing_result.append(' ')

        if all(i == ' ' for i in printing_result):
            print ("cold")

        print (*printing_result)

        if all(i == 'hot' for i in printing_result):
            dupa = True
            break
    return dupa
