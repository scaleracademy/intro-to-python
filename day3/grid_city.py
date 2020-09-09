# take a m * n grid (matrix) as input
# print the sum of all the elements, max,
# and the sum of left_diagonal

n, m = map(int, input().split())

matrix = []
for r in range(n):
  row = list(map(int, input().split()))
  matrix.append(row)

print(matrix)
