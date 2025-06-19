grid = []
for i in range(5):
    for j in range(5):
        grid.append(i+j)
print(grid)
# but there is no efficient way to access the elements
#so use comprehension
grid = []
for i in range(5):
    row = [i + j for j in range(5)]  # builds the array by row
    grid.append(row)
print(grid)
# or use nested comprehension
grid = []
grid = [[i+j for i in range(5)] for j in range(5)]
print(grid)
# can keep adding dimensions. 3D array example below
grid = []
grid = [[[i+j+k for i in range(5)] for j in range(5)] for k in range(6)]
print(grid[3][3][3])