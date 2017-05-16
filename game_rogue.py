import os
import sys



def print_board(board):
    for line in board:
        print(''.join(line))
    return board

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def hero_class_def(player_race):
    hero_class = input("Choose your class by pressing a number: \n\n    1. Warrior  @     ||    2. Hunter  &       ||    3. Mage  \u2C07    \n: ")
    if hero_class == "1":
        player_sign = player_race[:7] + "@" + player_race[7:]
    elif hero_class == "2":
        player_sign = player_race[:7] + "&" + player_race[7:]
    elif hero_class == "3":
        player_sign = player_race[:7] + "\u2C07" + player_race[7:]
    else:
        sys.exit()
    return player_sign

def hero_race_def():
    hero_race = input("Choose your race by pressing a number: \n\n    1. \033[1;33mHuman\033[1;m     ||    2. \033[1;32mElf\033[1;m       ||    3.   \033[1;30mOrc\033[1;m    \n: ")
    if hero_race == "1":
        player_race = "\033[1;33m\033[1;m"
    elif hero_race == "2":
        player_race = "\033[1;32m\033[1;m"
    elif hero_race == "3":
        player_race = "\033[1;30m\033[1;m"
    else:
        sys.exit()
    return player_race

def insert_player(board,x,y,player_sign):
    board[y][x] = player_sign
    return board



def read_file(filename):
    board = []
    column = []
    with open(filename) as text:
        for line in text.readlines():
            column.append(line)
        board.append(column)
    return board


def read_board(filename):
    board = []
    sun = []
    trees = []
    rowtxt = []
    with open('sun.txt') as text:
        for line in text:
            line = "\033[1;33m"+ line + "\033[1;m"
            sun.append(line)
    board.append(sun)
    with open(filename) as text:
        for line in text:
            lista = []
            for char in line[:-1]:
                if char == '~':
                    char = '\033[94m' + char + '\033[00m'
                lista.append(char)
            board.append(lista)
    with open('map2.txt') as text:
        for line in text:
            line =  "\033[1;32m"+ line + "\033[1;m"
            trees.append(line)
    board.append(trees)
    rowtxt.append("\033[1;36mThe Legend Of Zelda: Cult of Deadly Python\033[1;m ~~~~~~~~~~ ENERGY: "+ 2*"\033[1;31m♥\033[1;m")
    board.append(rowtxt)
    return board


"""def add_to_inv(sign):
    inv = []
    inv.append(sign)
    board.append(inv)
    return board"""

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

def moving(board, x, y, player_sign):
    direction = getch()
    if (board[y][x] == "*"):
        insert_player(board, x, y, " ")
        energy = energy + 1
        #export_inventory(inv,'inv.csv')
    if direction == "d":
        if not(board[y][x+1] == "|"):
            insert_player(board, x, y, ".")
            x += 1
            insert_player(board, x, y, player_sign)
    if direction == "a":
        if not(board[y][x-1] == "|"):
            insert_player(board, x, y, ".")
            x -= 1
            insert_player(board ,x ,y, player_sign)
    if direction == "w":
        if not(board[y-1][x] == "_"):
            insert_player(board, x, y, ".")
            y -= 1
            insert_player(board ,x ,y , player_sign)
    if direction == "s":
        if not(board[y+1][x] == "_"):
            insert_player(board, x, y, ".")
            y += 1
            insert_player(board, x ,y , player_sign)
    if direction == "x":
        sys.exit()
    return x, y


def main():
    board = read_file('int_screen.txt')
    print_board(board)
    player_race = hero_race_def()
    player_sign = hero_class_def(player_race)
    #board = create_board()
    x= 10
    y= 10
    board = read_board('maps.txt')
    insert_player(board,x, y, player_sign)
    insert_player(board,5, 5, "*")
    while True:
        x, y = moving(board ,x ,y, player_sign)
        os.system('clear')
        print_board(board)

main()
