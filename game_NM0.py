
import os
import sys
import csv
import time
from hotcold import *
from gameInventory import *


def print_board(board, end_time):
    if end_time != 0 :
        end_timer = '\nTime left:',str(int(end_time))
        board[14] = end_timer
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
    hero_class = input("Choose your class by pressing a number: \n|  1. Warrior : @ (DMG: +3, HEALTH: +3, STR: +4, WISDOM: +1)\n|  2. Hunter : & (DMG: +4, HEALTH: +3, STR: +3, WISDOM: +1)\n|  3. Mage : \u2C07 (DMG: +2, HEALTH: +3, STR: +2, WISDOM: +4)    \n\n: ")
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
    hero_race = input("Choose your race by pressing a number: \n\n|  1. \033[1;33mHuman\033[1;m (DMG: 2, HEALTH: 2, STR: 2, WISDOM: 1)   \n|  2. \033[1;32mElf\033[1;m (DMG: 1, HEALTH: 1, STR: 1, WISDOM: 4)       \n|  3. \033[1;30mOrc\033[1;m (DMG: 2, HEALTH: 3, STR: 3, WISDOM: -1)    \n\n: ")
    if hero_race == "1":
        player_race = "\033[1;33m\033[1;m"
    elif hero_race == "2":
        player_race = "\033[1;32m\033[1;m"
    elif hero_race == "3":
        player_race = "\033[1;30m\033[1;m"
    else:
        sys.exit()
    return player_race



def hero_name_and_sex_def():
    hero_sex = input("Are you man(1) or woman(2)? ")
    hero_name = input("What's your name? ")
    if hero_sex == "1":
        print("\nHello Sir " + hero_name + "!\n")
    if hero_sex == "2":
        print("\nHello Lady " + hero_name + "!\n")
    return hero_sex, hero_name

def insert_sign(board,x,y,player_sign):
    board[y][x] = player_sign
    return board



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
    name = "\033[1;36mThe Legend Of Zelda: Cult of Deadly Python\033[1;m:" + "\033[1;31m ♥ \033[1;m"
    for i in name:
        rowtxt.append(i)
    board.append(rowtxt)
    board.append(timer)

    return board



def add_lifes(board, end_time):
    lifes = 0
    lifes += 1
    board[13][63] += lifes*" ♥ "
    print_board(board, end_time)
    return lifes




def move_player(board, x, y, player_sign, obstacle, border, end_time, inv, game):
    added_items= []
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

    items_list = ["❀", "🍶", "💰", "🌟", "🔑"]
    new_yx = board[new_y][new_x]

    if not new_yx in border:
        if new_yx == '●':
            game = hot_and_cold_game()
        if new_yx == ' ':
            insert_sign(board, x, y, '  ')
        if new_yx == obstacle:
            insert_sign(board, x, y, obstacle)
        elif new_yx in items_list:
            added_items.append(new_yx)
            add_lifes(board, end_time)
            add_to_inventory(inv,added_items)
            export_inventory(inv, 'inv.csv')
            show_pop_up(board, inv)
            insert_sign(board, x, y, ".")
        else:
            insert_sign(board, x, y, ".")
        x = new_x
        y = new_y

    if direction == "x":
        sys.exit()

    return x, y, game



def show_pop_up(board, inv):
    board_copy = []
    for line in board:
        board_copy.append(line[:])
    inv_list = []

    for item in inv:
        inv_list.append(str(item) + "  " + str(inv[item]))
    lenght = max(inv_list, key = len)
    pop_height, pop_width = 4 + len(inv), len(lenght) + 4
    x_start = 25 - pop_width//2
    x_end = x_start+pop_width+2

    for line in range(pop_height):
        if line in [0, pop_height-1]:
            board_copy[1+line][x_start:x_end] = ["#" for column in range(1, pop_width+3)]
        elif line in [1, pop_height-2]:
            board_copy[1+line][x_start:x_end] = ["#"] + [" " for column in range(2, pop_width+2)] + ["#"]
        else:
            board_copy[1+line][x_start:x_end] = ["#"] + [" "]*2 + list(inv_list[line-3]) + [" "]*(pop_width - 2 - len(inv_list[line-3])) + ["#"]

    print_board(board_copy, 0)
    time.sleep(2)
    print_board(board, 0)




def intro_hoho():
    intro_file = open("intro.txt", "r")
    brief_file = open("intr.txt", "r")
    intro_contents = intro_file.read()
    brief_contents = brief_file.read()
    timecount = 920
    timecount_1 = 330
    start = time.time()
    theme = 0
    while theme < 3:
        end = time.time()
        tictic = end - start
        if tictic >= 2:
            print(intro_contents[(-920 + timecount):(0 + timecount)])
            timecount = timecount + 920
            start = time.time()
            theme = theme + 1
            continue
        else:
            continue

    while theme >= 3:
        end = time.time()
        tictic = end - start
        if tictic >= 2:
            print(brief_contents[(-330 + timecount_1):(0 + timecount_1)])
            timecount_1 = timecount_1 + 330
            start = time.time()
            theme = theme + 1
            continue
        elif theme == 18:
            break
        else:
            continue




def main():
    inv = {}
    border = ['|','_','\033[94m' + '~' + '\033[00m']
    intro_hoho()
    hero_sex, hero_name = hero_name_and_sex_def()
    player_race = hero_race_def()
    player_sign = hero_class_def(player_race)
    x= 10
    y= 10
    board = read_board('maps.txt')
    start_time = 0
    end_time = 0

    while True:
        game = False
        x, y, game = move_player(board ,x ,y, player_sign, "#", border, end_time, inv, game)
        if board[y][x] == "^":
            board = read_board('lvl3.txt')
            x = 1
            y = 2
        elif board[y][x] == ">":
            board = read_board('test1.txt')
            x = 1
            y = 2
            start_time = time.time()
        elif board[y][x] == "🚪" and "🔑" in inv:
            board = read_board('python.txt')
            x = 1
            y = 2
        if game == True:
            board = read_file('level3.txt')
            sys.exit()
        if start_time != 0:
            end_time = 100 - (time.time() - start_time)


            if end_time < 0:
                sys.exit()

        insert_sign(board, x, y, player_sign)
        os.system('clear')
        print_board(board, end_time)



if __name__ == '__main__':
    main()
