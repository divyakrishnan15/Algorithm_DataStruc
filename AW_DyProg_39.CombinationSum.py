def combinationSum(candidates, target):
        res = []
        
        def dfs(i, cur, total):
            print("------------")
            print("cur = ",cur)
            print("total = ",total)
            print("candidates = ",candidates)
            print("total = ",total)
            print("target = ",target)
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            print("candidates[i] = ",candidates[i])
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            #print("cur.pop() = ",cur.pop())
            cur.pop()
            dfs(i + 1, cur, total)    
        
        dfs(0, [], 0)
        return res
candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []