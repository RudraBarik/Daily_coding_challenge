# https://www.hackerrank.com/contests/smart-interviews/challenges/si-sum-of-pairs/problem

"""
Given an array of integers and a number K, check if there exist a pair of indices i,j s.t. a[i] + a[j] = K and i!=j.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, first line of each test case contains N - size of the array and K, and the next line contains N integers - the elements of the array. 

Constraints

30 points 
1 <= T <= 100 
2 <= N <= 1000 

70 points 
1 <= T <= 300 
2 <= N <= 10000 

General Constraints 
-108 <= K <= 108 
-108 <= ar[i] <= 108 

Output Format

For each test case, print "True" if such a pair exists, "False" otherwise, separated by newline. 

Sample Input 0

3
5 -15
-30 15 20 10 -10 
2 20
10 10 
4 7
-4 0 10 -7 
Sample Output 0

True
True
False"""

def sumOfPairs(arr, target):
    arr.sort()
    low = 0
    high = len(arr) - 1
    
    while (low < high): # Given that i #j
        total = low + high
        if total == target:
            return True
        elif total > target:
            high -= 1
        else:
            low += 1
    return False

if __name__ == '__main__':
    t = int(input())
    for tc in range(t):
        n, total = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        result = sumOfPairs(arr, total)
        print (result)