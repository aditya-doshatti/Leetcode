'''
1024. Video Stitching
Medium

You are given a series of video clips from a sporting event that lasted T seconds.  These video clips can be overlapping with each other and have varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].  We can cut these clips into segments freely: for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event ([0, T]).  If the task is impossible, return -1.

 

Example 1:

Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
Output: 3
Explanation: 
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].

https://leetcode.com/problems/video-stitching/
'''
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # event = [float("inf")] * T
        # for i,elem in enumerate(clips):
        #     for k in range(elem[0], elem[1]):
        #         if k <= T:
        #             event[k] = i
        # print(event)
        # return len(set(event))
        clips.sort()
        end, curr_end, retVal = 0, 0, 1
        for clip in clips:
            if clip[0] > end:
                return -1
            elif clip[0] > curr_end:
                curr_end = end 
                retVal += 1
            end = max(end, clip[1])
            if end >= T:
                return retVal
        return -1
