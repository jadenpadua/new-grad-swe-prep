def allSubstrings(s):
  n = len(s)
  substrings = []
  for i in range(n):
    for j in range(i, n):
      substrings.append(s[i:j+1])
  return substrings
      
