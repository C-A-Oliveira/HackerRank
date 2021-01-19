# https://www.hackerrank.com/challenges/saveprincess/problem

def displayPathtoPrincess(n,grid):
    m_coord = [0,0]
    p_coord = [0,0]

    x = 0
    for x_c in grid:
        y = 0
        for y_c in x_c:
            if y_c == 'm': 
                m_coord = [x,y]
            if y_c == 'p': 
                p_coord = [x,y]
            y += 1
        x += 1
    
    while m_coord[0] != p_coord[0]:
        if m_coord[0] < p_coord[0]:
            m_coord[0] += 1
            print("DOWN")
        else:            
            m_coord[0] -= 1
            print("UP")
    while m_coord[1] != p_coord[1]:
        if m_coord[1] < p_coord[1]:
            m_coord[1] += 1
            print("RIGHT")
        else:            
            m_coord[1] -= 1
            print("LEFT")
    #print all the moves here


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)