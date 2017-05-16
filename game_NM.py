import os
import sys
import csv


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
    return board#, y, x



def read_file(filename):
    board = []
    column = []
    with open(filename) as text:
        for line in text.readlines():
            column.append(line)
        board.append(column)
    for line in board:
        print(''.join(line))


def read_board(filename):
    board = []
    sun = []
    trees = []
    rowtxt = []
    inv = []
    text = []
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
    name = "\033[1;36mThe Legend Of Zelda: Cult of Deadly Python\033[1;m:\033[1;31m ♥\033[1;m"
    for i in name:
        rowtxt.append(i)
    print(rowtxt.index("♥"))
    board.append(rowtxt)
    print(board.index(rowtxt))
    board.append(inv)
    #board.append(text)
    return board



def add_to_inventory(board, added_items):
    inv = 0
    inv += 1
    #board[15] = '\033[94m' + 'Gathered items:' '\033[00m'
    board[14] += ' ❀ '*inv
    print_board(board)




def add_lifes(board):
    lifes = 0
    lifes += 1
    board[13][63] += lifes*" ♥ "
    print_board(board)


# def moving2(...):
#     direction = getch()
#     newx = x
#     newy = y
#     if direction == 'd':
#         newx+=1
#     elif di...




def moving(board, x, y, player_sign, obstacle, border):
    direction = getch()
    if direction == "d":
        current_yx = board[y][x+1]
        if not current_yx in border:
            if current_yx == obstacle:
                insert_player(board, x, y, obstacle)
            elif current_yx == "❀":
                add_lifes(board)
                add_to_inventory(board,'❀')
            else:
                insert_player(board, x, y, ".")
            x += 1
            #insert_player(board, x, y, player_sign)
    if direction == "a":
        current_yx = board[y][x-1]
        if not current_yx in border:
            if current_yx == obstacle:
                insert_player(board, x, y, obstacle)
            else:
                insert_player(board, x, y, ".")
            x -= 1
            #insert_player(board ,x ,y, player_sign)
    if direction == "w":
        current_yx = board[y-1][x]
        if not current_yx in border:
            if current_yx == obstacle:
                insert_player(board, x, y, obstacle)
            else:
                insert_player(board, x, y, ".")
            y -= 1
            #insert_player(board ,x ,y , player_sign)
    if direction == "s":
        current_yx = board[y+1][x]
        if not current_yx in border:
            if current_yx == obstacle:
                insert_player(board, x, y, obstacle)
            else:
                insert_player(board, x, y, ".")
            y += 1
            #insert_player(board, x ,y , player_sign)
    if direction == "x":
        sys.exit()
    return x, y


def main():
    #lifes = 3
    border = ['|','_','\033[94m' + '~' + '\033[00m']
    read_file('int_screen.txt')
    player_race = hero_race_def()
    player_sign = hero_class_def(player_race)
    x= 10
    y= 10
    board = read_board('maps.txt')
    #board = insert_player(board,x, y, player_sign)
    #insert_player(board,5, 5, "*")
    #print_board(board)
    while True:
        x, y = moving(board ,x ,y, player_sign, "#", border)
        board = insert_player(board, x, y, player_sign)
        os.system('clear')
        print_board(board)

main()
