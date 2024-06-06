'''
846. Hand of Straights

Medium

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

https://leetcode.com/problems/hand-of-straights/description
'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        countDict = Counter(hand)
        for key in sorted(countDict.keys()):
            # print(countDict)
            while countDict[key] != 0:
                countDict[key] -= 1
                for i in range(1, groupSize):
                    if key + i in countDict.keys() and countDict[key + i] > 0:
                        countDict[key + i] -= 1
                    else:
                        return False
        for key in countDict.keys():
             if countDict[key] != 0:
                return False
        return True
