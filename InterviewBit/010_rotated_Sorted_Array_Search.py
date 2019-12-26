# https://www.interviewbit.com/problems/rotated-sorted-array-search/

"""
Rotated Sorted Array Search
Asked in:  
Facebook
Google
Microsoft
Amazon
Bookmark Suggest Edit
Given an array of integers A of size N and an integer B.

array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

You are given a target value B to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

NOTE:- Array A was sorted in non-decreasing order before rotation.

NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
Input Format

The first argument given is the integer array A.
The second argument given is the integer B.
Output Format

Return index of B in array A, otherwise return -1
Constraints

1 <= N <= 1000000
1 <= A[i] <= 10^9
all elements in A are disitinct.
For Example

Input 1:
    A = [4, 5, 6, 7, 0, 1, 2, 3]
    B = 4
Output 1:
    0
Explanation 1:
 Target 4 is found at index 0 in A.


Input 2:
    A = [5, 17, 100, 3]
    B = 6
Output 2:
    -1"""
    
# Solution: Iterative way: O(log(n)) time |O(1) space

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        return self.binarysearchHelper(A,B, 0, len(A) -1)
    
    def binarysearchHelper(self, array, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            potentialMatch = array[mid]
            leftNum = array[left]
            rightNum = array[right]
            
            if target == potentialMatch:
                return mid
                
            elif leftNum <= potentialMatch:
                if target < potentialMatch and target >= leftNum:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > potentialMatch and target <= rightNum:
                    left = mid + 1
                else:
                    right = mid -1
        return -1 

