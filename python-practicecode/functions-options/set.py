# a=set()
a={1,2,3.4,"t","r"}
a.add('e')
a.remove(1)
# a[0]=12 #unordered so set can't changed
print(a)


normal_set = set(["a", "b","c"])
 
print("Normal Set")
print(normal_set)
# A frozen set
frozen_set = frozenset(["e", "f", "g"])
print("\nFrozen Set")
print(frozen_set)


# for i in enumerate()

s = {1, 2, 3, 3, 2, 4, 5, 5}
# Insert multiple elements
print(s)
s.update([6, 7, 8])
s.add(17)
print(s)


'''remove and discard in set()'''
s1 = {1, 2, 3, 3, 2, 4, 5, 5}
print(s1)
# Remove will raise an error if the element is not in the set
s1.remove(3)
print(s1)
# Discard doesn't raise any errors
s1.discard(1)
print(s1)

'''set() Operations'''
a = {1, 2, 3, 3, 2, 4, 5, 5}
b = {4, 6, 7, 9, 3}
# Performs the Intersection of 2 sets and prints them
print("Intersection",a & b)
# Performs the Union of 2 sets and prints them
print("Union",a | b)
# Performs the Difference of 2 sets and prints them
print("Difference",a - b) 
# Performs the Symmetric Difference of 2 sets and prints them
#Returns all the elements not common to both the sets.
print("not common to both the sets",a ^ b)