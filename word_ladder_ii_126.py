'''
126. Word Ladder II
Hard

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

https://leetcode.com/problems/word-ladder-ii/
'''
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList: return []
        found, q, nq = False, {beginWord}, set()
        while q and not found:
            words -= set(q)
            for x in q:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y == endWord: 
                            found = True
                        else: 
                            nq.add(y)
                        tree[x].add(y)
            q, nq = nq, set()
        def bt(x): 
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
        return bt(beginWord)

#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         dic =defaultdict(set)
#         graph = defaultdict(set)
#         for word in wordList:
#             for i in range(len(word)):
#                 if i < len(word)-1:
#                     temp = word[:i] + '*' + word[i+1:]
#                 else:
#                     temp = word[:i] + '*'
#                 dic[temp].add(word)
#         #print(dic)
#         new , tempq = set(), {beginWord}
#         self.helper(new, tempq, endWord, dic, graph)
#         print(graph)
#         listVal = self.traverse(beginWord, endWord, graph)
#         minLen, retVal = float('inf'), []
#         for i in listVal:
#             if len(i) < minLen:
#                 minLen = len(i)
        
#         print(graph, listVal, minLen)
#         for i in listVal:
#             if len(i) == minLen:
#                 retVal.append(i)
#         return retVal

#     def traverse(self, b, e, graph):
#         temp , retVal = [b], []
#         q = list(graph[b])
#         while q:
#             word = q.pop()
#             temp.append(word)
#             if word == b:
#                 retVal.append(temp)
#             else:
#                 tempq = graph[word]
#                 for val in tempq:
#                     if val not in temp:
#                         q.append(val)
#         return retVal
#         #return [[b]] if b == e else [[b] + rest for y in graph[b] for rest in self.traverse(y, e, graph)]
        
#     def helper(self, new, tempq, e, dic, graph):
#         #print(new, tempq, e, graph)
#         for b in tempq:
#             for i in range(len(b)):
#                 if i < len(b)-1:
#                     temp = b[:i] + '*' + b[i+1:]
#                 else:
#                     temp = b[:i] + '*'
#                 iSet = dic[temp]
#                 for item in iSet:
#                     if item != b and item not in graph[b]:
#                         new.add(item)
#                         graph[b].add(item)
#             tempq = set()
#             self.helper(tempq, new, e, dic, graph)
#         return
