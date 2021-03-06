"""
Search In Sorted Matrix

​https://www.algoexpert.io/questions/Search%20In%20Sorted%20Matrix

You are given a two-dimensional array (matrix) of distinct integers where each row is sorted and each column is also sorted. The matrix does not necessarily have the same height and width. You are also given a target number, and you must write a function that returns an array of the row and column indices of the target number if it is contained in the matrix and [-1, -1] if it is not contained in the matrix.
​
Sample input:
[
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
], 44
Sample output: [3, 3]"""



# Time: O(n+m) where n is no. of rows, m is no. of columns
# Space: O(1)

# Hint: Start at first row last element, compare with target, keep checking, eliminate columns and rows where target would not be present.

def searchInSortedMatrix(matrix, target):
  row = 0
  col = len(matrix[0]) - 1 # Last element in first row
  while row < len(matrix) and col >=0:
    if matrix[row][col] > target:
      col -= 1  # Shift to previous column (Eliminating the current column)
    elif matrix[row][col] < target:
      row += 1  # Shift to next row (Eliminating the current row)
    else:
      return [row, col]
  return [-1, -1]

matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
]
target = 44
print (searchInSortedMatrix(matrix, target))
  