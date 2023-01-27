#Importo librarine heapq per alokim te shtegut me koston me te ulet...
import heapq
#dhe random per te gjeneruar random fusha te bllokuara ne matrice
import random

def shtegu(landscape, start, goal, numObstacles):
    #Lista e blloqeve te ndaluara
    obstacles = set()
    #Shto random blloqe ne matrice si te ndaluara, por jo me shume
    #sesa numri i ndalesa te dhena paraprakisht (numObstacles)
    while len(obstacles) < numObstacles:
        obstacle = (random.randint(0, n-1), random.randint(0, m-1))
        #Mos e lejo te jete goal bllok i ndaluar apo blloku i fillimit (start)
        if obstacle != start and obstacle != goal:
            obstacles.add(obstacle)
    #Inicializimi i heap stack ne start
    heap = [(0, start)]
    #Lista e blloqeve te vizituara
    visited = set()
    #Dictionary per ruajtjen e gjatesise se rrugetimit dhe prindit
    #te vleres paraprake
    cost = {start: 0}
    parent = {start: None}
    #Perderisa nuk kemi mbaruar heap stack
    while heap:
        #Largo bllokun me peshen me te vogel drejt zgjidhjes nga heap stack
        currentCost, currentCell = heapq.heappop(heap)
        #Nese jemi te blloku i goal, kemi gjetur zgjidhjen
        if currentCell == goal:
            break
        #Ruaje bllokun si bllok te vizituar
        visited.add(currentCell)
        #Merr fqinjet e bllokut momental
        neighborsList = neighbors(landscape, currentCell, obstacles)
        #Per secilin fqinj...
        for neighbor in neighborsList:
            #...nese nuk eshte vizituar...
            if neighbor not in visited:
                #...fute ne kalkulimit shtegun me kosto me te ulet...
                new_cost = currentCost + 1
                #...dhe nese fqinji nuk eshte vizituar dhe ka koston me te ulet...
                if neighbor not in cost or new_cost < cost[neighbor]:
                    #...ruaje koston e re...
                    cost[neighbor] = new_cost
                    parent[neighbor] = currentCell
                    #...dhe fut fqinjin ne heap stack
                    heapq.heappush(heap, (new_cost + heuristic(neighbor, goal), neighbor))
    #Nese kemi gjetur shtegun, pershkruaj shtegun nga mbrapa dhe ruaje me vizualisht ndryshe si figure
    if goal in parent:
        path = [goal]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        for tile in path:
            landscape[int(tile[0])][int(tile[1])] = "\u2705"
        for obstackeTile in list(obstacles):
            landscape[int(obstackeTile[0])][int(obstackeTile[1])] = chr(0x1F4A3)
        return landscape
    #Nese nuk kemi shteg, kthe None per t'u vertetuar me poshte nga IF funksioni
    else:
        return None

def neighbors(landscape, cell, obstacles):
    #Inicializimi i matrices
    n, m = len(landscape), len(landscape[0])
    #Lista e fqinjeve
    neighbors = []
    #Shiko blloqet para, mbrapa, larte dhe poshte...
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        x, y = cell[0] + dx, cell[1] + dy
        #...nese blloku nuk eshte i ndaluar dhe eshte brenda kufijve te matrices...
        if 0 <= x < n and 0 <= y < m and (x, y) not in obstacles:
            #...shtoje te lista e fqinjeve
            neighbors.append((x, y))
    return neighbors


def heuristic(cell, goal):
    #Kthe rrugen e gjetur
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

#Madhesia e matrices se blloqeve
n, m = 10, 10
landscape = [['\u2b1c' for _ in range(m)] for _ in range(n)]
start = (0, 0)
goal = (9, 9)
numObstacles = input('Sa blloqe te ndaluara deshironi: ');

path = shtegu(landscape, start, goal, int(numObstacles))
if path:
    print("Shtegu me i shkurter u gjet \U0001F600:\n")
    for row in path:
        print(row,'\n')
    print('Vemendje: "\u2b1c" - eshte bllok i thate i shtegut, ' + chr(0x1F4A3) + ' - eshte bllok i ndaluar, "\u2705" - eshte shtegu ku ka kaluar roboti')
else:
    print("Nuk ka shteg per robotin \U0001F61E.")
