
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
