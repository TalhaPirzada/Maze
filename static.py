from collections import deque
class Maze :
    def print_maze(self, grid, rows, cols) :
        i = 0
        j = 0
        while (i < rows) :
            j = 0
            while (j < cols) :
                print("  ", grid[i][j], end = "")
                j += 1
            
            print("\n", end = "")
            i += 1
        
        print("\n", end = "")
    
    def solve_maze_bfs(self,collection, output, rows, cols, r, c):
        queue = deque([(r, c)])  
        visited = set()
        while queue:
            row, col = queue.popleft()
            if row < 0 or row >= rows or col < 0 or col >= cols or output[row][col]:
                continue
            if row == rows - 1 and col == cols - 1: 
                output[row][col] = True
                return True
            if collection[row][col] == 1:
                output[row][col] = True
                visited.add((row, col))
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = row + dr, col + dc
                    if (nr, nc) not in visited:
                        queue.append((nr, nc))
        return False

    def maze_test(self, collection, rows, cols) :
        output = [[False] * (cols) for _ in range(rows) ]
        i = 0
        j = 0
        if (self.solve_maze_bfs(collection, output, rows, cols, 0, 0)) :
            print("\n  Input Maze \n", end = "")
            self.print_maze(collection, rows, cols)
            print("  Output Maze \n", end = "")
            i = 0
            while (i < rows) :
                j = 0
                while (j < cols) :
                    if (output[i][j] == False) :
                        print("   0", end = "")
                    else :
                        print("   1", end = "")
                    
                    output[i][j] = False
                    j += 1
                
                print("\n", end = "")
                i += 1
            
        else :
            print("\n No Result \n", end = "")
        
    

def main() :
    obj = Maze()

    # ONLY ONE SOLUTION 
    collection = [
        [1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1],
        [0, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1]
    ]


# NO RESULT 
    # collection = [
    #     [0, 0, 0, 1, 1, 1],
    #     [0, 1, 0, 1, 0, 1],
    #     [0, 1, 0, 0, 1, 1],
    #     [0, 0, 0, 1, 1, 0],
    #     [0, 0, 0, 1, 0, 1],
    #     [0, 0, 0, 1, 1, 1]
    # ]


    # # MULTIPLE SOLUTION

    # collection = [
    #     [1, 0, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 0, 1],
    #     [0, 1, 0, 0, 1, 1],
    #     [0, 1, 1, 1, 1, 0],
    #     [1, 0, 1, 1, 0, 1],
    #     [1, 0, 1, 1, 1, 1]
    # ]

    rows = len(collection)
    cols = len(collection[0])
    obj.maze_test(collection, rows, cols)

if __name__ == "__main__": main()