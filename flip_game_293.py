'''
293. Flip Game

Easy

You are playing a Flip Game with your friend.

You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return all possible states of the string currentState after one valid move. You may return the answer in any order. If there is no valid move, return an empty list [].

 
Example 1:

Input: currentState = "++++"
Output: ["--++","+--+","++--"]

https://leetcode.com/problems/flip-game/description/
'''
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        retVal = []
        for i in range(len(currentState) - 1):
            if currentState[i] == "+" and currentState[i+1] == "+":
                retVal.append(currentState[:i] + "--" + currentState[i+2:])
        return retVal
