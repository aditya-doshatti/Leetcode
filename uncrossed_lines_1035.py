'''
1035. Uncrossed Lines
Medium

We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

Example 1:

Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

https://leetcode.com/problems/uncrossed-lines/
'''
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                if A[i] == B[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], 1 + dp[i][j])
        return dp[-1][-1]
        # retVal = 0
        # if len(A) <= len(B):
        #     first = A
        #     orignal = B
        # else:
        #     first = B
        #     orignal = A
        # q, done = [0], set()
        # done.add(0)
        # while q:
        #     i = q.pop(0)
        #     curr = 0
        #     second = orignal
        #     while i in range(len(first)):
        #         if first[i] in second:
        #             k = second.index(first[i])
        #             second = second[k+1:]
        #             curr += 1
        #             if i not in done:
        #                 q.append(i)
        #                 done.add(i)
        #         i += 1
        #     retVal = max(curr, retVal)
        # return retVal
