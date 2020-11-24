'''
337. House Robber III
Medium

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

https://leetcode.com/problems/house-robber-iii/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return (0,0)
            left = helper(node.left)
            right = helper(node.right)
            
            yes = node.val + left[1] + right[1]
            no = max(left) + max(right)
            return [yes, no]
        return max(helper(root))

        # q, vals = [root], [0]
        # cnt, temp = len(q), 0
        # while cnt > 0:
        #     node = q.pop(0)
        #     vals[temp] += node.val
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        #     cnt -= 1
        #     if cnt == 0:
        #         vals.append(0)
        #         temp += 1
        #         cnt = len(q)
        # if vals[-1] == 0:
        #     vals = vals[:-1]
        # print(vals)
        # retVal = 0 
        # prev, curr = 0, 0
        # for num in vals:
        #     prev, curr = curr, max(prev+num, curr)
        # return curr
