# Problem Description:
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

def removeDuplicates(nums):
  if len(nums) == 0:
    return 0
  else:
    currentComparison = nums[0]
    uniqueValues = 1
    counter = 1
    while counter < len(nums):
      if nums[counter] == currentComparison:
        nums.pop(counter)
        nums.append('_')
      elif nums[counter] == '_':
        break
      else:
        currentComparison = nums[counter]
        uniqueValues += 1
        counter += 1
    return uniqueValues

# Test Cases
print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([-1, 0, 0, 0, 0, 3, 3]))
