import time

intro_file = open("intro.txt", "r")
brief_file = open("intro1.txt", "r")
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
    else:
        continue
