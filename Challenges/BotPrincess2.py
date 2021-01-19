# https://www.hackerrank.com/challenges/saveprincess2/problem

def nextMove(n,r,c,grid):
    m_coord = [r,c]
    p_coord = [0,0]

    x = 0
    for x_c in grid:
        y = 0
        for y_c in x_c:
            if y_c == 'p': 
                p_coord = [x,y]
            y += 1
        x += 1
    
    if m_coord[0] != p_coord[0]:
        if m_coord[0] < p_coord[0]:
            m_coord[0] += 1
            return "DOWN"
        else:            
            m_coord[0] -= 1
            return "UP"
    elif m_coord[1] != p_coord[1]:
        if m_coord[1] < p_coord[1]:
            m_coord[1] += 1
            return "RIGHT"
        else:            
            m_coord[1] -= 1
            return "LEFT"
    return ""

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))