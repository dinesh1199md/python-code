import re
def lonestword(s):
  words=s.split()
  d={}
  for word in words:
    if bool(re.match('[a-zA-Z]+$',word)):
      d[word]=len(word)
#   print(d)

  if d:
    print(d)
    print(list({k:v for k,v  in sorted(d.items(),key=lambda e:-e[1])}.items()))
    return list({k:v for k,v  in sorted(d.items(),key=lambda e:-e[1])}.items())[0]
  else:
     return -1     

s="kart2hi loki dinesh hel marimass22"
print(lonestword(s))