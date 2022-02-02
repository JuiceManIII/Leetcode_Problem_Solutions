#Problem Description:
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

def romanToInt(s):
  numeralLength = len(s)
  integerSolution = 0
  for i in range(numeralLength - 1, -1, -1):

  #------------------------------------------------------
    if s[i].upper() == "I":
      if i != numeralLength - 1:
        if s[i + 1].upper() == "V":
          integerSolution -= 5
          integerSolution += 4
        elif s[i + 1].upper() == "X":
          integerSolution -= 10
          integerSolution += 9
        else:
          integerSolution += 1
      else:
        integerSolution += 1

  #------------------------------------------------------
    if s[i].upper() == "V":
      integerSolution += 5

  #------------------------------------------------------
    if s[i].upper() == "X":
      if i != numeralLength - 1:
        if s[i + 1].upper() == "L":
          integerSolution -= 50
          integerSolution += 40
        elif s[i + 1].upper() == "C":
          integerSolution -= 100
          integerSolution += 90
        else:
          integerSolution += 10
      else:
        integerSolution += 10

#------------------------------------------------------

    if s[i].upper() == "L":
      integerSolution += 50

#-------------------------------------------------------
    if s[i].upper() == "C":
      if i != numeralLength - 1:
        if s[i + 1].upper() == "D":
          integerSolution -= 500
          integerSolution += 400
        elif s[i + 1].upper() == "M":
          integerSolution -= 1000
          integerSolution += 900
        else:
          integerSolution += 100
      else:
        integerSolution += 100
  
#------------------------------------------------------
  
    if s[i].upper() == "D":
      integerSolution += 500
  
#------------------------------------------------------
  
    if s[i].upper() == "M":
      integerSolution += 1000
  
#------------------------------------------------------
  
  return integerSolution

# Test Cases
print(romanToInt("iii"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
