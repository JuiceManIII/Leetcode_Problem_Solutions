# Problem description:
# Given an integer x, return true if x is palindrome integer.

def palindromeCheck(x):
  import math
  isPalindrome =  True
  numberLength = len(str(x))
  for i in range (int(math.ceil(numberLength / 2))):
    if str(x)[i] != str(x)[numberLength - 1 - i]:
      isPalindrome = False
  return isPalindrome

# Test Cases
print(palindromeCheck(1212121212121))
print(palindromeCheck(7586597598275))
print(palindromeCheck(12345678900987654321))
print(palindromeCheck(9))
print(palindromeCheck(2002))
print(palindromeCheck(345))
