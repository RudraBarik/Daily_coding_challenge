# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-sum-of-odd-elements/problem

"""
Print sum of all odd elements in an array.

Input Format

Input contains 2 lines, first line contains integer N - the size of the array and second line contains array elements.

Constraints

1 <= N <= 102 
-106 <= ar[i] <= 106 


Output Format

Print sum of all odd elements.

Sample Input 0

5
6 9 8 4 3
Sample Output 0

12
Explanation 0

Self Explanatory"""

def solve(arr, n):
    sum =0
    for ele in arr:
        if ele % 2 != 0:
            sum += ele
    return sum


n = int(input())
arr = list(map(int, input().split()))
print (solve(arr, n))