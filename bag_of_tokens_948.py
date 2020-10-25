'''
948. Bag of Tokens
Medium

You have an initial power of P, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.

 

Example 1:

Input: tokens = [100], P = 50
Output: 0
Explanation: Playing the only token in the bag is impossible because you either have too little power or too little score.

https://leetcode.com/problems/bag-of-tokens/
'''
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        i, score = 0, 0
        while tokens:
            # print(tokens, P, score)
            if tokens[0] <= P:
                curr = tokens.pop(0)
                score += 1
                P -= curr
            elif score >= 1 and len(tokens) > 1:
                score -= 1
                curr = tokens.pop()
                P += curr
            else:
                return score
        return score
