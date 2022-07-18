arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]
 
# Function to merge two arrays
 
def merge(n, m):
    i = 0
    j = 0
    k = n - 1
    while (i <= k and j < m):
        print("------------")
        print("i = ",i)
        print("arr1[i] = ",arr1[i])
        print("j = ",j)
        print("arr2[j] = ",arr2[j])
        print("k = ",k)
        print("arr1[k] = ",arr1[k])
        if (arr1[i] < arr2[j]):
            i += 1
        else:
            temp = arr2[j]
            arr2[j] = arr1[k]
            arr1[k] = temp
            j += 1
            k -= 1
 
    arr1.sort()
    arr2.sort()
 
 
# Driver code
if __name__ == '__main__':
    merge(len(arr1), len(arr2))
    print("After Merging \nFirst Array: ")
    print(','.join(str(x) for x in arr1))
    print("Second Array:  ")
    print(','.join(str(x) for x in arr2))