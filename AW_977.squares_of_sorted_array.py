def squares_of_sorted_array(nums):
    res=[]
    l,r=0,len(nums)-1

    while l<r:
        if nums[l] * nums[l] > nums[r] * nums[r]:
            res.append(nums[l]*nums[l])
            l+=1
        else:
            res.append(nums[r]*nums[r])
            r-=1
    return sorted(res),res[::1]

def new(nums):
    print("====== [2 - FUNCTION LIST] ======")
    #List = .append()
    #set = .add()
    #dict = dict[i]=i
    mylist=[]
    for i in nums:
        mylist.append(i*i)
    a=sorted(mylist)
    return a,a[:3]

def list_comp(nums):
    print("====== [3 - LIST COMPREHENSION] ======")
    print("sum of nums in list = ",[a*a for a in nums]) 
    print("sum of nums in the length = ",[a*a for a in range(len(nums))]) 
    print(sorted([a*a if a%2==0 else False for a in (nums)]))   
    print({a*a if a%2==0 else False for a in (nums)})
def oneline(nums):
    print("====== [4 - LAMBDA] ======")
    print(sorted(set(list(map(lambda x:x*x,nums)))))
    print(sorted(list(map(lambda x:x*x if x%2==0 else False,nums))))
    print(sorted(list(map(lambda x:x*x,nums1))))
    print("====== [5 - LAMBDA DICT] ======")
    print(sorted(list(map(lambda x:x['Math']*x['Math'],dict1))))

nums=[-4,-1,0,3,3,10]
nums1=[-7,-3,2,3,11]

dict1=[{"Name":"Div","Class":10,"Math":-4},
        {"Name":"Sush","Class":11,"Math":-1},
        {"Name":"Balaji","Class":12,"Math":-0},
        {"Name":"Mena","Class":1,"Math":3},
        {"Name":"Krish","Class":11,"Math":10}]
print(squares_of_sorted_array(nums))
print(new(nums))
print(list_comp(nums))
print(oneline(nums))

#Ans =[16,1,0,9,81,225] sortted [1,9,16,81,225]

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.