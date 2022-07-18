def printRepeating(arr, size):
  
    print("FIRST - Repeating elements are ",
                         end = ',')
    for i in range (0, size-1):
        print("************")
        print("i = ",i)
        for j in range (i + 1, size):
            print("j == ",j)
            if arr[i] == arr[j]:
                print(" arr[i] = ",arr[i])
# Driver code
arr = [4, 2, 4, 5, 2, 3, 1]
arr_size = len(arr)
printRepeating(arr, arr_size)
#Time Complexity: O(n*n) 
#Auxiliary Space: O(1)

#----------------------------

def printRepeating_count(arr,size) :
    count = [0] * size
    print("COUNT - Repeating elements are ",end = ",")
    for i in range(0, size) :
        print("---COUNT-----")
        print("i =",i)
        print("arr[i] = ",arr[i])
        print("count[arr[i]] = ",count[arr[i]])
        if(count[arr[i]] == 1) :
            print(arr[i], end = " ")
        else :
            print("ELSE -- count[arr[i]] = ",count[arr[i]])
            count[arr[i]] = count[arr[i]] + 1
# Driver code
arr = [4, 2, 4, 5, 2, 3, 1]
arr_size = len(arr)
printRepeating_count(arr, arr_size)
#Time Complexity: O(n) 
#Auxiliary Space: O(n)

#----------------------------

def printRepeating_set(arr, size):
      
    s = set()
    print("SET -- The two Repeating elements are : ", end = "")
      
    for i in range(size):
        print("---SET-----")
        print("len(s) =",len(s))
        print("i =",i)
        print("arr[i] = ",arr[i])
        print("s = ",s)
        if (len(s) and arr[i] in s):
            print("IF == arr[i]  = ",arr[i])            
        s.add(arr[i]) 

# Driver code
arr = [ 4, 2, 4, 5, 2, 3, 1 ]
arr_size = len(arr)
printRepeating_set(arr, arr_size)
#Time Complexity: O(n)  
#Auxiliary Space: O(n)  