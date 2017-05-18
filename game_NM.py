import os
import sys
import csv
import time


def print_board(board, end_time):
    if end_time != 0 :
        end_timer = '\n',str(int(end_time))
        board[14] = end_timer
        #if end_time < 10:
        #    x = int(end_time)
        #    y = int(end_time)
        #else:
        #    x = int(end_time)/3
        #    y = int(end_time)/3
        #    if x % 2 == 0:
        #        insert_sign(board, x, y, '*')
        #    else:
        #        insert_sign(board, x, y, '.')
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



def insert_sign(board,x,y,player_sign):
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
    timer = []
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
                chars = ["M", '+','s', 'h', ':', '/', 'y', 'o', '-', 'd', 'm']
                if char in chars:
                    char = '\033[94m' + char + '\033[00m'
                chars2 = ['N', 'n', 'u', '0']
                if char in chars2:
                    char = "\033[1;33m"+ char + "\033[1;m"

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
    board.append(rowtxt)
    board.append(inv)
    board.append(timer)

    #board.append(text)
    return board



def add_to_inventory(board, added_items):
    inv = 0
    inv += 1
    #board[15] = '\033[94m' + 'Gathered items:' '\033[00m'
    board[14] += ' ❀ '*inv
    print_board(board)




def add_lifes(board, end_time):
    lifes = 0
    lifes += 1
    board[13][63] += lifes*" ♥ "
    print_board(board, end_time)
    return lifes



def moving2(board, x, y, player_sign, obstacle, border, end_time):
    direction = getch()
    new_x = x
    new_y = y
    if direction == "d":
        new_x += 1
    if direction == "a":
        new_x -= 1
    if direction == "w":
        new_y -= 1
    if direction == "s":
        new_y += 1
    new_yx = board[new_y][new_x]
    if not new_yx in border:
        if new_yx == obstacle:
            insert_sign(board, x, y, obstacle)
        elif new_yx == "❀":
            add_lifes(board, end_time)
            add_to_inventory(board,'❀')
            insert_sign(board, x, y, ".")
        else:
            insert_sign(board, x, y, ".")
        x = new_x
        y = new_y
    if direction == "x":
        sys.exit()
    return x, y




def main():
    border = ['|','_','\033[94m' + '~' + '\033[00m']
    read_file('int_screen.txt')
    #start_time = time.time()

    player_race = hero_race_def()
    player_sign = hero_class_def(player_race)

    #print(round(int(end_time)))
    x= 10
    y= 10
    board = read_board('maps.txt')
    #dupa = False
    start_time = 0
    #lifes = add_lifes(board)
    end_time = 0
    while True:
        x, y = moving2(board ,x ,y, player_sign, "#", border, end_time)
        if board[y][x] == "^":
            board = read_board('python.txt')
            x = 1
            y = 2
        elif board[y][x] == ">":
            board = read_board('test1.txt')
            x = 1
            y = 2
            #dupa = True
            start_time = time.time()
            #timer(board, start_time)
        if start_time != 0:
            end_time = time.time() - start_time
        #else:
        #    end_time = 0
        #if int(end_time) > 30 and dupa == True:
        #    sys.exit()
            #start_time = time.time()

        insert_sign(board, x, y, player_sign)
        os.system('clear')
        print_board(board, end_time)
        #timer(5)




if __name__ == '__main__':
    main()
