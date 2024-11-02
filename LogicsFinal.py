import random
def start_game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat
def add_new_two(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while(mat[r][c]!=0):
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2
def current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return "WON"
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return "GAME NOT OVER"
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] or mat[i][j]==mat[i+1][j]:
                return "GAME NOT OVER"
    for j in range(3):
        if mat[3][j]==mat[3][j+1]:
            return "GAME NOT OVER"
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return "GAME NOT OVER"
    return "LOST"
def reverse(mat):
    new=[[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            new[i][j]=mat[i][3-j]
    return new
def transpose(mat):
    new=[[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            new[i][j]=mat[j][i]
    return new
def compress(mat):
    new_mat=[]
    change=False
    for i in range(4):
        new_mat.append([0]*4)
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                
                if j!=pos:
                    change=True
                pos+=1
    return new_mat,change
def merge(mat):
    change=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                mat[i][j]*=2
                mat[i][j+1]=0
                change=True
    return change

def move_left(mat):
    mat,c1=compress(mat)
    c2=merge(mat)
    change=c1 or c2
    mat,c=compress(mat)
    return mat,change
def move_right(mat):
    mat=reverse(mat)
    mat,c1=compress(mat)
    c2=merge(mat)
    change=c1 or c2
    mat,c=compress(mat)
    mat=reverse(mat)
    return mat,change
def move_down(mat):
    mat=transpose(mat)
    mat=reverse(mat)
    mat,c1=compress(mat)
    c2=merge(mat)
    change=c1 or c2
    mat,c=compress(mat)
    mat=reverse(mat)
    mat=transpose(mat)
    return mat,change
def move_up(mat):
    mat=transpose(mat)
    mat,c1=compress(mat)
    c2=merge(mat)
    change=c1 or c2
    mat,c=compress(mat)
    mat=transpose(mat)
    return mat,change

def print_board(mat):
    for i in mat:
        for j in i:
            print(j,end="    ")
        print()