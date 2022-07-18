def boat(people,limit):
    people.sort()
    print("1,2,2,3")

    left = 0
    right = len(people)-1

    boats_number = 0

    while(left<=right):
        print("----------")
        print("left = ",left)
        print("right = ",right)
        
        print("people[left] = ",people[left])
        print("people[right] = ",people[right])
        print("limit = ",limit)
        if(left==right):
            boats_number+=1
            break
        if(people[left]+people[right]<=limit):
            print(people[left],people[right],"<= limit(",limit)
            left+=1
            print("left===",left)

        right-=1
        print("right ===",right)
        boats_number+=1
        print("boats_number ===",boats_number)
    return boats_number

people=[3,2,2,1]
limit=3
print(boat(people,limit))


# Example 1:
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)

# Example 2:
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)

# Example 3:
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
 

# Constraints:
# 1 <= people.length <= 5 * 104
# 1 <= people[i] <= limit <= 3 * 104