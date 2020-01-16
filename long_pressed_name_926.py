'''
925. Long Pressed Name
Easy

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

https://leetcode.com/problems/long-pressed-name/
'''
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while j < len(typed):
            if j+1 < len(typed):
                if typed[j] != typed[j+1]:
                    if name[i] != typed[j]:
                        return False
                    i+=1
                    c = 0
                    while name[i-1] == name[i]:
                        c+=1
                        if j > 0:
                            if typed[j] != typed[(j-c)]:
                                return False
                        else:
                            return False
                        i+=1
                    if i+1 < len(name):
                        if name[i] == name[i+1]:
                            j+=1
                            if typed[j] != name[i] or typed[j+1] != name[i+1]:
                                return False
                            else:
                                i+=1
                        
            else:
                if i < len(name)-1:
                    if name[i] != typed[j]:
                        return False
                else:
                    if name[-1] != typed[j]:
                        return False
            j +=1
        if i >= len(name)-1 or j == 1000:
            return True
        else:
            return False
