'''
1104. Path In Zigzag Labelled Binary Tree
Medium

In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.


Example 1:

Input: label = 14
Output: [1,3,4,14]

https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
'''
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        retVal = []
        retVal.append(label)
        n = 1
        while label > 2**(n)-1:
            n += 1
        while label >1:
            n = n - 1
            newVal = (2**(n)) + (2**(n-1)-1- int(label/2))
            label = newVal
            retVal.append(newVal)
        return sorted(retVal)
