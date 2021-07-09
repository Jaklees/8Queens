# This is the Eight Queens Problem
# 8x8 chess board

global N
N = 8

def pb(board):#Print Board util fnc
    for i in range(N):
        for j in range(N):
            print(board[i][j], end="")
            print("",end=" ")
        print()

def csafe(board,r,c): # Check if this spot is valid
    
    def horizontal(board,r,c): # check left side of current row
        for i in range(c):
            if board[r][i] == 1:
                return False
        return True
    
    def updiag(board,r,c): #high diag left side
        x = c
        for i in range(r,-1,-1):
            if x < 0:
                break
            if board[i][x] == 1:
                return False
            x -= 1
        return True
    
    def lodiag(board,r,c): #low diag left side
        x = c
        for i in range(r,N,1):
            if x > 7:
                break
            if board[i][x] == 1:
                return False
            x -= 1
        return True
    if horizontal(board,r,c) == False:
        return False
    if updiag(board,r,c) == False:
        return False
    if lodiag(board,r,c) == False:
        return False
    return True
        
def queen(board,r,c):
    if c >= N: # Base Case
        return True
    for i in range(N):
        if csafe(board,i,c) == True:
            board[i][c] = 1
            print("This is the next iteration")
            pb(board)
            if queen(board,0,c+1) == True:
                return True
        board[i][c] = 0
    return False

#the main, define board, call queen function with an empty board and at row 0
          #1 2 3 4 5 6 7 8 
board = [ [0,0,0,0,0,0,0,0],#1
          [0,0,0,0,0,0,0,0],#2
          [0,0,0,0,0,0,0,0],#3
          [0,0,0,0,0,0,0,0],#4
          [0,0,0,0,0,0,0,0],#5
          [0,0,0,0,0,0,0,0],#6
          [0,0,0,0,0,0,0,0],#7
          [0,0,0,0,0,0,0,0] ]#8
pb(board)
if queen(board,0,0):
         print("Success")
         pb(board)
else:
    print("error")
