'''
299. Bulls and Cows
Easy

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

https://leetcode.com/problems/bulls-and-cows/
'''
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        for i in range(len(secret)):
            bulls += int(secret[i] == guess[i])
        for c in set(secret):
            cows += min(secret.count(c), guess.count(c))
        return str(bulls)+"A"+str(cows-bulls)+"B"
        
        # bull, cow, cowed = 0,0, []
        # sdict, gdict = defaultdict(int), defaultdict(int)
        # orig = {}
        # for i in range(len(secret)):
        #     if secret[i] == guess[i]:
        #         bull += 1
        #     else:
        #         if sdict[guess[i]]:
        #             sdict[guess[i]] -= 1
        #             cow += 1
        #         else:
        #             gdict[guess[i]] += 1
        #         if gdict[secret[i]]:
        #             gdict[secret[i]] -= 1
        #             cow += 1
        #         else:
        #             sdict[secret[i]] += 1
        # return str(bull)+"A"+str(cow)+"B"
        
        # cntS = Counter(secret)
        # cntG = Counter(guess)
        # bulls, cows = 0, 0
        # for i in range(len(guess)):
        #     if i > len(secret):
        #         break
        #     else:
        #         if guess[i] == secret[i]:
        #             cntS[secret[i]] -=1
        #             cntG[guess[i]] -= 1
        #             bulls += 1
        # for val in cntG:
        #     if val in cntS:
        #         if cntG[val] >= cntS[val] and cntG[val] != 0:
        #             if cntG[val] > cntS[val]:
        #                 cows = cows + (cntG[val] - cntS[val])
        #             else:
        #                 cows += 1
        # return str(bulls)+"A"+str(cows)+"B"
