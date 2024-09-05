from pyamaze import maze,agent,textLabel,COLOR
from collections import deque
from queue import PriorityQueue
import os

class Algorithms:
    def BFS(m,start=None):
        if start is None:
            start=(m.rows,m.cols)
        frontier = deque()
        frontier.append(start)
        bfsPath = {}
        visited = [start]
        bSearch=[]

        while len(frontier)>0:
            currCell=frontier.popleft()
            if currCell==m._goal:
                break
            for d in 'ESNW':
                if m.maze_map[currCell][d]==True:
                    if d=='E':
                        childCell=(currCell[0],currCell[1]+1)
                    elif d=='W':
                        childCell=(currCell[0],currCell[1]-1)
                    elif d=='S':
                        childCell=(currCell[0]+1,currCell[1])
                    elif d=='N':
                        childCell=(currCell[0]-1,currCell[1])
                    if childCell in visited:
                        continue
                    frontier.append(childCell)
                    visited.append(childCell)
                    bfsPath[childCell] = currCell
                    bSearch.append(childCell)

        fwdPath={}
        cell=m._goal
        while cell!=(m.rows,m.cols):
            fwdPath[bfsPath[cell]]=cell
            cell=bfsPath[cell]
        return bSearch,bfsPath,fwdPath
    


    def DFS(m,start=None):
        if start is None:
            start=(m.rows,m.cols)
        visited=[start]
        frontier=[start]
        dfsPath={}
        dSeacrh=[]
        while len(frontier)>0:
            currCell=frontier.pop()
            dSeacrh.append(currCell)
            if currCell==m._goal:
                break
            poss=0
            for d in 'ESNW':
                if m.maze_map[currCell][d]==True:
                    if d =='E':
                        child=(currCell[0],currCell[1]+1)
                    if d =='W':
                        child=(currCell[0],currCell[1]-1)
                    if d =='N':
                        child=(currCell[0]-1,currCell[1])
                    if d =='S':
                        child=(currCell[0]+1,currCell[1])
                    if child in visited:
                        continue
                    poss+=1
                    visited.append(child)
                    frontier.append(child)
                    dfsPath[child]=currCell
            if poss>1:
                m.markCells.append(currCell)
        fwdPath={}
        cell=m._goal
        while cell!=start:
            fwdPath[dfsPath[cell]]=cell
            cell=dfsPath[cell]
        return dSeacrh,dfsPath,fwdPath


    global m
    m=None
    def Generate():
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # maze_file = os.path.join(current_dir, 'astardemo.csv')
    
        global m
        m = maze(10,10)
        # m.CreateMaze(loadMaze=maze_file)
        m.CreateMaze(loopPercent=0)
        a=agent(m,footprints=True,shape="arrorw", color=COLOR.green)
        m.enableArrowKey(a)
        m.enableWASD(a)


    def main():
        global m
        print("Welcome to Maze World Algorithm Simulator")
        while True:
            print("\t1.Play")
            print("\t2.BFS")
            print("\t3.DFS")
            # print("\t4.A Star")
            print("\t5.Generate Maze")
            print("\t6.Exit")
            c=input("Choose Option : ")
            if c=='1':
                Algorithms.Generate()
            elif c=='2':
                delay = 300
                bSearch, bfsPath, fwdPath = Algorithms.BFS(m)
                a =agent(m, footprints=True, color=COLOR.yellow, shape='square', filled=True)
                b = agent(m, footprints=True, color=COLOR.red, shape='arrow', filled=False)
                c = agent(m, 1, 1, footprints=True, color=COLOR.cyan, shape='square', filled=True, goal=(m.rows, m.cols))
                m.tracePath({a: bSearch}, delay=delay)
                m.tracePath({c: bfsPath}, delay=delay)
                m.tracePath({b: fwdPath}, delay=delay)
                textLabel(m, 'BFS Path Length', len(fwdPath) + 1)
                textLabel(m, 'BFS Search Length', len(bSearch))
                m.run()

            elif c=='3':
                delay=300
                dSeacrh, dfsPath, fwdPath = Algorithms.DFS(m) 
                a = agent(m, footprints=True, shape='square', color=COLOR.green)
                b = agent(m, footprints=True,shape='arrow',  filled=True)
                c = agent(m, 5, 1, footprints=True, color=COLOR.yellow)
                m.tracePath({a: dSeacrh}, showMarked=True,delay=delay)
                m.tracePath({b: dfsPath},delay=delay)
                m.tracePath({c: fwdPath},delay=delay)
                m.run()
            # elif c=='4':
            #     delay=300
            #     searchPath, aPath, fwdPath = Algorithms.aStar(m)
            #     a = agent(m, footprints=True, color=COLOR.blue, filled=True)
            #     b = agent(m, 1, 1, footprints=True, color=COLOR.yellow, filled=True, goal=(m.rows, m.cols))
            #     c = agent(m, footprints=True,shape="arrow", color=COLOR.red)
            #     m.tracePath({a: searchPath}, delay=delay)
            #     m.tracePath({b: aPath}, delay=delay)
            #     m.tracePath({c: fwdPath}, delay=delay)
            #     textLabel(m, 'A Star Path Length', len(fwdPath) + 1)
            #     textLabel(m, 'A Star Search Length', len(searchPath))
            #     m.run()

            elif c=='5':
                Algorithms.Generate()
            elif c=='6':
                print("Thank You")
                break
            else:
                print("Enter Valid Input")

if __name__=='__main__':
    Algorithms.main()