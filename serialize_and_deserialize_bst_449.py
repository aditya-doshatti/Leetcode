'''
449. Serialize and Deserialize BST
Medium

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

 

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]

https://leetcode.com/problems/serialize-and-deserialize-bst/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root) -> str:
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)

        return ' '.join(map(str, vals))

    
    def deserialize(self, data)-> TreeNode:
        vals = collections.deque(int(val) for val in data.split())

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(float('-infinity'), float('infinity'))


#     def serialize(self, root: TreeNode) -> str:
#         """Encodes a tree to a single string.
#         """
#         arr, q = [], [root]
#         while q:
#             node = q.pop(0)
#             if node:
#                 arr.append(node.val)
#                 if node.left:
#                     arr.append(node.left.val)
#                 else:
#                     arr.append(None)
#                 if node.right:
#                     arr.append(node.right.val)
#                 else:
#                     arr.append(None)
#                 q.append(node.left)
#                 q.append(node.right)
#         return ''.join(str(arr))

#     def deserialize(self, data: str) -> TreeNode:
#         """Decodes your encoded data to tree.
#         """
#         arr = data.split(',')
#         arr[0] = arr[0][1:]
#         arr[-1] = arr[-1][:-1]
#         print(data, arr)
#         if len(arr) <=1:
#             return None
#         dic, i = {}, 0
#         rootNode = TreeNode(arr[0].strip())
#         dic[int(arr[0].strip())] = rootNode
#         while i < len(arr):
#             try:
#                 val = int(arr[i].strip())
#             except:
#                 val = None
#             if val in dic:
#                 node = dic[val]
#             else:
#                 node = TreeNode(val)    
#             i += 1
#             print(val, i)
#             if val:
#                 try:
#                     lVal = int(arr[i].strip())
#                     node.left = TreeNode(lVal)
#                     dic[lVal] = node.left
#                 except:
#                     pass
#                 i += 1
#                 try:
#                     rVal = int(arr[i].strip())
#                     node.right = TreeNode(rVal)
#                     dic[rVal] = node.right
#                     print(node)
#                     print("Value set")
#                 except:
#                     pass
#                 i += 1
#             print(dic)
#         return rootNode
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
