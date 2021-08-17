'''
1723. Find Minimum Time to Finish All Jobs
Hard

You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.

There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.

Return the minimum possible maximum working time of any assignment.

 

Example 1:

Input: jobs = [3,2,3], k = 3
Output: 3
Explanation: By assigning each person one job, the maximum time is 3.

https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/
'''
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True) # opt 1
        self.retVal = sum(jobs)
        arr = [0] * k
        def dfs(i):
            if i == n:
                self.retVal = min(self.retVal, max(arr))
                return
            for j in range(k):
                if arr[j] + jobs[i] < self.retVal:
                    # print(arr, self.retVal)
                    arr[j] += jobs[i]
                    dfs(i + 1)
                    arr[j] -= jobs[i]
                if arr[j] == 0: 
                    break
            return False
        dfs(0)
        return self.retVal
        # jobs.sort(reverse = True)
        # if k >= len(jobs):
        #     return jobs[0]
        # arr = [0] *k
        # for i in range(len(jobs)//k+1):
        #     for j in range(k):
        #         if j + (i*k) >= len(jobs):
        #             break
        #         minVal = min(arr)
        #         idx = arr.index(minVal)
        #         arr[idx] += jobs[j + (i*k)]
        # return max(arr)
