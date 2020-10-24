'''
500. Keyboard Row
Easy

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


 
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

https://leetcode.com/problems/keyboard-row/
'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = {"Q","W","E","R","T","Y","U","I","O","P","q","w","e","r","t","y","u","i","o","p"}
        secondRow = {"A","S","D","F","G","H","J","K","L","a","s","d","f","g","h","j","k","l"}
        thirdRow = {"Z","X","C","V","B","N","M","z","x","c","v","b","n","m"}
        retVal = []
        for word in words:
            char = word[0]
            flag = True
            if char in firstRow:
                checkSet = firstRow
            elif char in secondRow:
                checkSet = secondRow
            else:
                checkSet = thirdRow
            for char in word:
                if char not in checkSet:
                    break
            else:
                retVal.append(word)                
        return retVal
