import os
import sys

def create_board(energy):
    '''
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    '''
    width = 110
    height = 40
    board = []
    row = []
    rowtxt = []
    rowtxt.append("###### \033[1;36mThe Legend Of Zelda: Cult of Deadly Python\033[1;m ##################################### ENERGY: "+ int(energy)*"\033[1;31m♥\033[1;m "   +    "     ###")
    for i in range(width):
        row.append("#")
    middle = []
    for a in range(width):
        if a == 0 or a == width - 1:
            middle.append("#")
        else:
            middle.append(" ")
    board.append(row)
    for i in range(height-2):
        board.append(middle[:])
    board.append(row)
    board.append(rowtxt)
    board.append(row)
    return board

def print_board(board):
    for line in board:
        print(''.join(line))

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

def moving(board, x, y, player_sign, energy):
    direction = getch()
    if (board[y][x] == "\033[1;31m🍶\033[1;m"):
        insert_player(board, x, y, " ")
        energy = energy + 1
    if direction == "d":
        if not(board[y][x+1] == "#"):
            insert_player(board, x, y, " ")
            x += 1
            insert_player(board, x, y, player_sign)
    if direction == "a":
        if not(board[y][x-1] == "#"):
            insert_player(board, x, y, " ")
            x -= 1
            insert_player(board ,x ,y, player_sign)
    if direction == "w":
        if not(board[y-1][x] == "#"):
            insert_player(board, x, y, " ")
            y -= 1
            insert_player(board ,x ,y , player_sign)
    if direction == "s":
        if not(board[y+1][x] == "#"):
            insert_player(board, x, y, " ")
            y += 1
            insert_player(board, x ,y , player_sign)
    if direction == "x":
        sys.exit()
    return x, y, energy

player_race = hero_race_def()
player_sign = hero_class_def(player_race)
energy = 3
board = create_board(energy)
x= 100
y= 10
insert_player(board,x, y, player_sign)
insert_player(board, 20, 20, "\033[1;31m🍶\033[1;m")

while True:
    x, y, energy = moving(board ,x ,y, player_sign, energy)
    os.system('clear')
    print_board(board)
