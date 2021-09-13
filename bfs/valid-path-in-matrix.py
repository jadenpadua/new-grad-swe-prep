"""
Given N X N matrix filled with 1, 0, 2, 3. Find whether there is a path possible from source to destination, traversing through blank cells only. You can traverse up, down, right, and left. 

A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Blank Wall.
Note: there are an only a single source and single destination(sink).
"""
from collections import deque
def valid_path(matrix):
    queue = deque()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                queue.append([i,j])
    
    while len(queue) > 0:
        popped = queue.popleft()
        i , j = popped[0], popped[1]
        
        if i < 0 or i > len(matrix) - 1 or j < 0 or j > len(matrix[0]) - 1:
            continue
        if matrix[i][j] == 0:
            continue
        if matrix[i][j] == 2:
            return True
        
        matrix[i][j] = 0

        queue.append([i + 1, j])
        queue.append([i - 1, j])
        queue.append([i, j - 1])
        queue.append([i, j + 1])
    
    return False

print(valid_path([[0, 3, 0, 1], [3, 0, 3, 3], [2, 3, 3, 3], [0, 3, 3, 3]]))
