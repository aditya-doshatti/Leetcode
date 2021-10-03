'''
819. Most Common Word
Easy

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

https://leetcode.com/problems/most-common-word/
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        symbols = ['!', '?', '\'', ',', ';', '.', '"']
        for symbol in symbols:
            paragraph = paragraph.replace(symbol, " ")
        words = paragraph.split()
        bannedSet = set(banned)
        wordFrequency = defaultdict(int)
        for word in words:
            if word not in bannedSet:
                wordFrequency[word] += 1
        wordFrequency = dict(sorted(wordFrequency.items(), key=lambda x:x[1], reverse=True))
        for word in wordFrequency:
            return word
