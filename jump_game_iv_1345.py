'''
1345. Jump Game IV
Hard

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

https://leetcode.com/problems/jump-game-iv/
'''
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        d = defaultdict(list)
        for i, num in enumerate(arr):
            d[num].append(i)
        queue = deque([(0, 0)])
        visited, visited_groups = set(), set()
        while queue:
            steps, index = queue.popleft()
            if index == n - 1: 
                return steps
            for neib in [index - 1, index + 1]:
                if 0 <= neib < n and neib not in visited:
                    visited.add(neib)
                    queue.append((steps + 1, neib))
            if arr[index] not in visited_groups:
                for neib in d[arr[index]]:
                    if neib not in visited:
                        visited.add(neib)
                        queue.append((steps + 1, neib))
                visited_groups.add(arr[index])
