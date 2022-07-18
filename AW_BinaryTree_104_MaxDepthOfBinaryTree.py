
class Solution:
    def maxDepth_recursive(self, TreeNode):
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# ITERATIVE DFS   
class Solution:
    def maxDepth_dfs(self,reeNode):
        stack = [[root, 1]]
        res = 0
        
        while stack:
            node, depth = stack.pop()
        
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

# BFS
class Solution:
    def maxDepth_bfs(self,TreeNode):
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


root = [3,9,20,null,null,15,7]
a=Solution()
print(a.maxDepth_recursive(root))
print(a.maxDepth_dfs(root))
print(a.maxDepth_bfs(root))