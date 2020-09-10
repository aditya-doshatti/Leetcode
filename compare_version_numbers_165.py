'''
165. Compare Version Numbers
Medium

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.

 

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1

https://leetcode.com/problems/compare-version-numbers/
'''
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        levels1 = [int(x) for x in version1.split('.')]
        levels2 = [int(x) for x in version2.split('.')]
        minLen = min(len(levels1), len(levels2))
        for i in range(minLen):
            if levels1[i] < levels2[i]:
                return -1
            elif levels1[i] > levels2[i]:
                return 1
            else:
                continue
        if len(levels1) > minLen:
            for i in range(minLen, len(levels1)):
                if levels1[i] != 0:
                    return 1
        elif len(levels2) > minLen:
            for i in range(minLen, len(levels2)):
                if levels2[i] != 0:
                    return -1
        return 0
