"""Two Number Sum
https://www.algoexpert.io/questions/Two%20Number%20Sum
​
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order. If no two numbers sum up to the target sum, the function should return an empty array. Assume that there will be at most one pair of numbers summing up to the target sum.
​
Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
Sample output: [-1, 11]
​"""

# Solution 1: O(n**2)

# def twoNumberSum(array, targetSum):
#   for i in range(len(array)-1):
#     firstNum = array[i]
#     for j in range(i+1, len(array)):
#       secondNum = array[j]
#       if firstNum + secondNum == targetSum:
#         return sorted([firstNum, secondNum])
#   return []


# Solution 2: Using hashtable

#O(n) time and O(n) space
def twoNumberSum(array, targetSum):
  nums = {}  
  for num in array:
    potentialMatch = targetSum - num
    if potentialMatch in nums:
      return sorted([potentialMatch, num])
    else:
      nums[num] = True # Storing that number in hash table if not present
  return []
  
# Solution 3:
# Time O(nlog(n)), space O(1)
# def twoNumberSum(array, targetSum):
#   array.sort()
#   left =0
#   right = len(array)-1
#   while left < right:
#     currentSum = array[left] + array[right]
#     if currentSum == targetSum:
#       return [array[left], array[right]]
#     elif currentSum < targetSum:
#       left += 1
#     elif currentSum > targetSum:
#       right -= 1
#   return []

# Soution 2 is better in time and solution 3 is better in space.
  
  