'''
1255. Maximum Score Words Formed by Letters

Hard

Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.


Example 1:

Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.

https://leetcode.com/problems/maximum-score-words-formed-by-letters/description
'''
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        lettersCounter = Counter(letters)
        totalScore = 0
        def explore(index, letterCounter, currScore):
            nonlocal totalScore
            totalScore = max(totalScore, currScore)
            if index == len(words):
                return
            for i in range(index, len(words)):
                tmpCounter = copy.deepcopy(letterCounter)
                word = words[i]
                wordScore = 0
                isValid = True
                for ch in word:
                    if ch in tmpCounter and tmpCounter[ch] > 0:
                        tmpCounter[ch] -= 1
                        wordScore += score[ord(ch) - ord("a")]
                    else:
                        isValid = False
                        break
                if isValid:
                    explore(i + 1, tmpCounter, currScore + wordScore)
        explore(0, lettersCounter, 0)
        return totalScore
