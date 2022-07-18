
########--REDUCE- FUNCTOOLS--###########
#-------------MAX Element in list---------
import functools 
lis = [ 1 , 3, 5, 6, 2, ] 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 

#--------------SUM OF A LIST----------------------
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)


########--MAP--###########
animals = ['dog', 'cat', 'parrot', 'rabbit']  
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
print(uppered_animals)

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]     
final_list = list(map(lambda x: x*2, li))
print(final_list)

########--FILTER--###########
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]  
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)

ages = [13, 90, 17, 59, 21, 60, 5]  
adults = list(filter(lambda age: age>18, ages))  
print(adults)