# Input : s = “geeks for geeks contribute practice”, w1 = “geeks”, w2 = “practice” 
# Output : 1 
# There is only one word between the closest occurrences of w1 and w2.

# Input : s = “the quick the brown quick brown the frog”, w1 = “quick”, w2 = “frog”
# Output : 2


def words(s,w1,w2):
    l=s.split()
    s=0
    e=0
    if w1 not in l and w2 not in l:
        return -1
    if w1 not in l or w2 not in l:
        return -1
    for key,word in enumerate(l):
        if word==w1:
            s=key
        if word==w2:
            e=key 
            break
    if len(l[s:e])!=0:
        return len(l[s:e])-1
    else: return 0
          
s = "geeks for geeks contribute practice"
w1 = "for"
w2 = "practice"
print(words(s,w1,w2))
# s="the"
# w1 = "quick"
# w2 = "frog"
# print(words(s,w1,w2))
# s=" "
# w1="therr"
# w2="the"
# print(words(s,w1,w2))