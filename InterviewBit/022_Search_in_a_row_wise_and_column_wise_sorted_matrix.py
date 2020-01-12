# https://www.interviewbit.com/problems/search-in-a-row-wise-and-column-wise-sorted-matrix/


"""Given a matrix of integers A of size N x M and an integer B.

In the given matrix every row and column is sorted in increasing order.

Find and return the position of B in the matrix in the given form:

If A[i][j] = B then return (i * 1009 + j)
And if B is not present return -1 instead.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Input Format

The first argument given is the integer matrix A.
The second argument given is the integer B.
Output Format

Return the position of B and if it is not present in A return -1 instead.
Constraints

1 <= N, M <= 1000
-100000 <= A[i] <= 100000
-100000 <= B <= 100000
For Example

Input 1:
    A = [   [1, 2, 3]
            [4, 5, 6]
            [7, 8, 9]   ]
    B = 2
Output 1:
    1011    (= 1 * 1009 + 2)

Input 2:
    A = [   [1, 3, 5, 7]
            [2, 4, 6, 8]    ]
    B = 10
Output 2:
    -1
    
"""

def solution(A, B):
  """
  The first argument given is the integer matrix A.
  The second argument given is the integer B.
  Return the position of B and if it is not present in A return -1 instead."""
  
  # Start searching from top right
  
  i = 0 # first row as given row numbers start from 1
  j = len(A[0]) - 1 # last column
  n = len(A) # no of rows
  
  while (i < n and j >= 0 ):
    if A[i][j] == B:
      i += 1   # just adding 1 to i and j as the answer expects
      j += 1
      return (i * 1009 + j)
    
    if A[i][j] > B:
      # skip the current column
      j -= 1
    else:
      # skip the current row
      i += 1
  return -1

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = 2

print (solution(A, B))