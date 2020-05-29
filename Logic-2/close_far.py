"""

Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.


close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True

"""
1.
def close_far(a, b, c):
  if abs(b-a)<=1:
    if abs(c-a)>=2 and abs(c-b)>=2:
      return True
    else:
      return False
  else:
    if abs(c-a)<=1:
      if abs(b-a)>=2 and abs(b-c)>=2:
        return True
      else:
        return False
  return False
  

  
  
 2.

def close_far(a, b, c):
  return is_close(a, b) and is_far(a, b, c) or is_close(a, c) and is_far(a, c, b)
 
 
def is_close(a, b):
  return abs(b-a)<=1
  
def is_far(a, b, c):
  return abs(c-a)>=2 and abs(c-b)>=2
    
  
  
  
  
  
