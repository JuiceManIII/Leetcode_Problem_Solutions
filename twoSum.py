# Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(nums, target):
  arrayLength = len(nums)
  solution = []
  for i in range (arrayLength):
      for j in range (i + 1, arrayLength):
          if nums[i] + nums[j] == target:
              solution.append(i)
              solution.append(j)
  return solution

# Test Cases

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([4, 7, 13, 18, 21], 17))
