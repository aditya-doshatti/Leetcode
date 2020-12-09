'''
1010. Pairs of Songs With Total Durations Divisible by 60
Medium

You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
'''
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod_dict, retVal = defaultdict(int), 0
        for val in time:
            if val% 60 == 0:
                retVal += mod_dict[0]
            else:
                retVal += mod_dict[60-(val%60)]
            mod_dict[val%60] += 1
        return retVal
