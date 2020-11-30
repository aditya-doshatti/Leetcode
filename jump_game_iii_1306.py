'''
1306. Jump Game III
Medium

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 

https://leetcode.com/problems/jump-game-iii/
'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        dest, pos, visited = set(), [], [False] * len(arr)
        for i,val in enumerate(arr):
            if val == 0:
                if i == start:
                    return True
                dest.add(i)
            l, r = -1, -1
            if i-val >= 0:
                l = i - val
            if i + val < len(arr):
                r = i + val
            pos.append([l,r])
        q = [start]
        while q:
            ele = q.pop(0)
            if ele in dest:
                return True
            if visited[ele]:
                continue
            else:
                visited[ele] = True
                if pos[ele][0] != -1:
                    q.append(pos[ele][0]) 
                if pos[ele][1] != -1:
                    q.append(pos[ele][1]) 
        return False
