'''
966. Vowel Spellchecker
Medium

Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

 

Example 1:

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

https://leetcode.com/problems/vowel-spellchecker/
'''
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact_word = set(wordlist)
        words_case = {}
        words_vowels = {}

        for word in wordlist:
            wordlower = word.lower()
            words_case.setdefault(wordlower, word)
            wordMasked = "".join('*' if c in 'aeiou' else c
                           for c in wordlower)
            words_vowels.setdefault(wordMasked, word)
        # print(words_case,words_vowels)
        retVal = []
        for query in queries:
            # print(retVal)
            if query in exact_word:
                retVal.append(query)
                # print(query)
                continue
            wordlower = query.lower()
            if wordlower in words_case:
                # print(wordlower)
                retVal.append(words_case[wordlower])
                continue
            wordMasked = "".join('*' if c in 'aeiou' else c
                           for c in wordlower)
            if wordMasked in words_vowels:
                # print(wordMasked)
                retVal.append(words_vowels[wordMasked])
                continue
            retVal.append("")
        return retVal
