"""

Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

"""

def cat_dog(str):
  catCount=0
  dogCount=0
  
  for i in range(len(str)-2):
    if str[i:i+3]=="cat":
      catCount = catCount + 1
    else:
      if str[i:i+3] =="dog":
        dogCount = dogCount+1
      else:
        continue
  
  return catCount == dogCount
  
