# Problem Description: 
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

def isValid(s):
  pairRemoved = True
  arrayS = []
  for i in range(len(s)):
    arrayS.append(s[i])
  while pairRemoved == True:
    if arrayS == [] or len(arrayS) == 1:
      break
    for i in range(len(arrayS) - 1):
      if arrayS[i] == "(" and arrayS[i + 1] == ")":
        arrayS.pop(i + 1)
        arrayS.pop(i)
        break
      elif arrayS[i] == "[" and arrayS[i + 1] == "]":
        arrayS.pop(i + 1)
        arrayS.pop(i)
        break
      elif arrayS[i] == "{" and arrayS[i + 1] == "}":
        arrayS.pop(i + 1)
        arrayS.pop(i)
        break
      else:
        if i == len(arrayS) - 2:
          pairRemoved = False
          break
  if arrayS == []:
    return True
  else:
    return False
  
 # Test Cases
print(isValid('(){}[]'))
print(isValid('(())({[]})'))
print(isValid('(()[]'))
