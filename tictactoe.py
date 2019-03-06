import os

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
count = 0


def board():
    print(a[0], a[1], a[2], sep="|")
    print(a[3], a[4], a[5], sep="|")
    print(a[6], a[7], a[8], sep="|")


def player1():
    i = int(input("Player 1:Enter (1-9):"))
    if (i < 1 or i > 9 or a[i - 1] == "X" or a[i - 1] == "O"):
        print("INVALID INPUT!")
        player1()
    else:
        a[i - 1] = "O"


def player2():
    i = int(input("Player 2:Enter (1-9):"))
    if (i < 1 or i > 9 or a[i - 1] == "X" or a[i - 1] == "O"):
        print("INVALID INPUT!")
        player2()
    else:
        a[i - 1] = "X"


def isWin():
    # horizontal
    for i in [0, 3, 6]:
        if (a[i] == a[i + 1] == a[i + 2] != " "):
            return True
    #vertical
    for i in [0, 1, 2]:
        if (a[i] == a[i + 3] == a[i + 6] != " "):
            return True
    #digonal
    if (a[0] == a[4] == a[8] != " "):
        return True
    if (a[2] == a[4] == a[6] != " "):
        return True
    return False


def isdraw():
    if count == 9:
        return True


if __name__ == "__main__":
    while True:
        board()
        player1()
        clear()
        board()
        if isWin():
            print("Player 1 You Won!")
            break
        count += 1
        if isdraw():
            print("Match draw!")
            break
        player2()
        clear()
        board()
        if isWin():
            print("player 2 You Won!")
            break
        count += 1
        if isdraw():
            print("Match draw!")
            break
        clear()
