# Problem Description:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):

    shortestWordLength = len(strs[0])
    for i in range(len(strs)):
      if len(strs[i]) < shortestWordLength:
        shortestWordLength = len(strs[i])

    longestCommonPrefix = ""
    for i in range(shortestWordLength):
      comparisonLetter = strs[0][i]
      lettersMatch = True
      for j in range(len(strs)):
        if strs[j][i] == comparisonLetter:
          lettersMatch = True
        else:
          lettersMatch = False
          break
      if lettersMatch == False:
        break
      else:
        longestCommonPrefix += comparisonLetter
    return longestCommonPrefix
  
# Test Cases
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["malice","malcontent","mallard"]))
