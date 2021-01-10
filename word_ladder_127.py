'''
127. Word Ladder
Hard

Given two words beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Return 0 if there is no such transformation sequence.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

https://leetcode.com/problems/word-ladder/
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        L = len(beginWord)
        word_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                word_dict[word[:i] + "*" + word[i+1:]].append(word)
        q = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        while q:
            curr, level = q.popleft()      
            for i in range(L):
                temp = curr[:i] + "*" + curr[i+1:]
                for word in word_dict[temp]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        q.append((word, level + 1))
                word_dict[temp] = []
        return 0
