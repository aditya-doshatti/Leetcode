'''
916. Word Subsets
Medium

We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.

 

Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]

https://leetcode.com/problems/word-subsets/
'''
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bCount = defaultdict(int)
        for b in B:
            temp = Counter(b)
            for key in temp:
                bCount[key] = max(bCount[key], temp[key])
        retVal = []
        # print(bCount)
        for a in A:
            cntA = Counter(a)
            fail = False
            for key in bCount:
                if key not in cntA or bCount[key] > cntA[key]:
                    print(key)
                    fail = True
                    break
            if not fail:
                retVal.append(a)
        return retVal
        
        # TLE
        # cntArr = []
        # for b in B:
        #     cntArr.append(Counter(b))
        # retVal = []
        # # print(cntArr)
        # for a in A:
        #     cntA = Counter(a)
        #     fail = False
        #     for dic in cntArr:
        #         for key in dic:
        #             if key not in cntA or dic[key] > cntA[key]:
        #                 fail = True
        #                 break
        #     if not fail:
        #         retVal.append(a)
        # return retVal
