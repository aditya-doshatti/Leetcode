'''
825. Friends Of Appropriate Ages
Medium

Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.

https://leetcode.com/problems/friends-of-appropriate-ages/
'''
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = collections.Counter(ages)
        ages = sorted(counter.keys())
        retVal = 0
        for i in range(len(ages) - 1, -1, -1):
            for j in range(i, -1, -1):
                a_age = ages[i]
                b_age = ages[j]
                if b_age <= 0.5 * a_age + 7 or a_age < 100 and b_age > 100:
                    break
                if a_age == b_age:
                    retVal += counter[b_age] * (counter[b_age] - 1)
                else:
                    retVal += counter[a_age] * counter[b_age]
        return retVal
