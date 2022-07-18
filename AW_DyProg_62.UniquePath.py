def uniquePaths(m, n):
        row = [1] * n
        
        for i in range(m - 1):
            print("-----------")
            print("i = ",i)
            print("m = ",m)
            print("n = ",n)
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                print("j = ",j)
                print("newRow[j + 1] = ",newRow[j + 1])
                print("row[j] = ",row[j])
                print("newRow[j] = ",newRow[j])
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
        
        # O(n * m) O(n)

m = 3
n = 2
print(uniquePaths(m, n))


# Input: m = 3, n = 7
# Output: 28

# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down