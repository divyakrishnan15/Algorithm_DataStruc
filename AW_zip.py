import itertools
from multiprocessing.connection import answer_challenge

def zip1(a,b,c):
    for (x,y,z) in zip(a,b,c):
        print(x,y,z) 
 

if __name__ == "__main__":
    a=[1,2,3]
    b=['a','b','c']
    c=[100,101]

    zip1(a,b,c)

# answer
# 1 a 100
# 2 b 101