'''
1678. Goal Parser Interpretation
Easy

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

 

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

https://leetcode.com/problems/goal-parser-interpretation/
'''
class Solution:
    def interpret(self, command: str) -> str:
        retVal = ''
        i =0
        while i < len(command):
            if command[i] == 'G':
                retVal += 'G'
                i += 1
            elif command[i+1] == ')':
                retVal += 'o'
                i += 2
            else:
                retVal += 'al'
                i += 4
        return retVal
