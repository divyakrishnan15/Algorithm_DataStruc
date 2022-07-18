def missing_repeating(arr):
    numberMap = {}      
    lengthOfArray = len(arr)

    for i in arr:
        print("-----------")
        if i not in numberMap:
            print("if numberMap = ",numberMap)
            print("if i = ",i)
            numberMap[i] = True
              
        else:
            print("else i = ",i)
            print("Repeating =", i)
      
    for i in range(1, lengthOfArray + 1):
        print("++++++++++++++++++++++")
        print("i = ",i)
        print("missing numberMap = ",numberMap)
        if i not in numberMap:            
            print("Missing =", i)


arr = [3, 1, 3]
arr1 = [4, 3, 6, 2, 1, 1]
print(missing_repeating(arr))
print(missing_repeating(arr1))