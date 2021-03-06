# https://www.interviewbit.com/problems/multiply-strings/

"""Multiply Strings
Asked in:  
Microsoft
Google
Bookmark Suggest Edit
Given two numbers represented as strings, return multiplication of the numbers as a string.

 Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. 
For example, 
given strings "12", "10", your answer should be “120”.

NOTE : DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ). 
We will retroactively disqualify such submissions and the submissions will incur penalties."""

# Hint: If length of input strings are N and M, then the expected comlexity is O(N*M) here.

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        return str(int(A) * int(B))
