'''
288. Unique Word Abbreviation
Medium

The abbreviation of a word is a concatenation of its first letter, the number of characters between the first and last letter, and its last letter. If a word has only two characters, then it is an abbreviation of itself.

For example:

dog --> d1g because there is one letter between the first letter 'd' and the last letter 'g'.
internationalization --> i18n because there are 18 letters between the first letter 'i' and the last letter 'n'.
it --> it because any word with only two characters is an abbreviation of itself.
Implement the ValidWordAbbr class:

ValidWordAbbr(String[] dictionary) Initializes the object with a dictionary of words.
boolean isUnique(string word) Returns true if either of the following conditions are met (otherwise returns false):
There is no word in dictionary whose abbreviation is equal to word's abbreviation.
For any word in dictionary whose abbreviation is equal to word's abbreviation, that word and word are the same.
 

Example 1:

Input
["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique", "isUnique"]
[[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"], ["cake"]]
Output
[null, false, true, false, true, true]

Explanation
ValidWordAbbr validWordAbbr = new ValidWordAbbr(["deer", "door", "cake", "card"]);
validWordAbbr.isUnique("dear"); // return false, dictionary word "deer" and word "dear" have the same abbreviation "d2r" but are not the same.
validWordAbbr.isUnique("cart"); // return true, no words in the dictionary have the abbreviation "c2t".
validWordAbbr.isUnique("cane"); // return false, dictionary word "cake" and word "cane" have the same abbreviation  "c2e" but are not the same.
validWordAbbr.isUnique("make"); // return true, no words in the dictionary have the abbreviation "m2e".
validWordAbbr.isUnique("cake"); // return true, because "cake" is already in the dictionary and no other word in the dictionary has "c2e" abbreviation.

https://leetcode.com/problems/unique-word-abbreviation/
'''
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dic = defaultdict(set)
        for word in dictionary:
            abbrevatedWord = self.abbrevation(word)
            self.dic[abbrevatedWord].add(word)
            
    def abbrevation(self, word):
        fchar, lchar = word[0], word[-1]
        intVal = ''
        if len(word) > 2:
            intVal = len(word) - 2
        abbrevatedWord = fchar + str(intVal) + lchar
        return abbrevatedWord

    def isUnique(self, word: str) -> bool:
        abbrevatedWord = self.abbrevation(word)
        #print(abbrevatedWord, word, self.dic, len(self.dic[abbrevatedWord]) == 1, word, self.dic[abbrevatedWord])
        if abbrevatedWord in self.dic:
            return len(self.dic[abbrevatedWord]) == 1 and (word in self.dic[abbrevatedWord])
        return True


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
