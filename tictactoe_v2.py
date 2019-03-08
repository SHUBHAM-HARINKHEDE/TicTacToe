import os
import logging
logging.basicConfig(filename='app.log',filemode='w',format='%(name)s - %(levelname)s - %message)s')

clear=lambda: os.system('' if os.name=='nt' else 'clear')

a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
count = 0
player="X"
opponent="O"

#board
def board():
    print(a[0], a[1], a[2], sep="|")
    print(a[3], a[4], a[5], sep="|")
    print(a[6], a[7], a[8], sep="|")

#player1
def player1():
    i = int(input("Player 1:Enter (1-9):"))
    if (i < 1 or i > 9 or a[i - 1] == player or a[i - 1] == opponent):
        print("INVALID INPUT!")
        player1()
    else:
        a[i - 1] = opponent

#player2
def player2():
    '''i = int(input("Player 2:Enter (1-9):"))
    if (i < 1 or i > 9 or a[i - 1] == player or a[i - 1] == opponent):
        print("INVALID INPUT!")
        player2()
    else:
        a[i - 1] = player
    '''
    a[findBestMove()]=player


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

#check draw
def isMoveLeft():
    for i in a:
        if(i not in [player,opponent]):
            return True
    return False


def evaluate():
    # horizontal
    for i in [0, 3, 6]:
        if (a[i] == a[i + 1] == a[i + 2] != " "):
            if a[i]==player:
                return +10
            else:
                return -10
    #vertical
    for i in [0, 1, 2]:
        if (a[i] == a[i + 3] == a[i + 6] != " "):
            if a[i]==player:
                return +10
            else:
                return -10
    #digonal
    if (a[0] == a[4] == a[8] != " "):
        if a[i]==player:
            return +10
        else:
            return -10
    if (a[2] == a[4] == a[6] != " "):
        if a[i]==player:
            return +10
        else:
            return -10
    return 0
def minimax(depth,isMax):
    score=evaluate()
    if(score==10):
        return score
    if(score==-10):
        return score
    if not isMoveLeft():
        return 0
   
    if isMax:
        best=-1000;
        for i in range(9):
            if a[i]not in [player,opponent]:
                a[i]=player
                best=max(best,minimax(depth+1,not isMax))
                a[i]=i+1#Undo move
        return best
    
    else:
        best=1000;
        for i in range(9):
            if a[i]not in [player,opponent]:
                a[i]=opponent
                best=min(best,minimax(depth+1,not isMax))
                a[i]=i+1#Undo move
        return best
            
def findBestMove():
    bestVal=-1000
    bestMove=-1
    for i in range(9):
        if a[i]not in [player,opponent]:
            a[i]=player
            moveVal=minimax(0,False)
            a[i]=i+1
            if moveVal>bestVal:
                bestMove=i#best move
                bestVal=moveVal
    return bestMove
            
                

if __name__ == "__main__":

    while True:
        board()
        player1()
        clear()
        board()
        if isWin():
            print("Player 1 You Won!")
            break
        if not isMoveLeft():
            print("Match draw!")
            break
        player2()
        clear()
        board()
        if isWin():
            print("player 2 You Won!")
            break
        if not isMoveLeft():
            print("Match draw!")
            break
        clear()
