import functools
from itertools import count

li=[1,2,3,4,5]

print(tuple(filter(lambda x: x%2==0, li)))


print(functools.reduce(lambda x,y:x+y,li))

print(list(map(lambda x:x*2,li)))
print(list(map(lambda x:x*x,li)))


#print(tuple(filter(lambda x:  true if x%2==0 false,li)))
#print(set(lambda x: x*2,li))





