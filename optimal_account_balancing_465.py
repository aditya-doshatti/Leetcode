'''
465. Optimal Account Balancing

Hard

You are given an array of transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

Return the minimum number of transactions required to settle the debt.

 

Example 1:

Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

https://leetcode.com/problems/optimal-account-balancing/description/
'''
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        data = defaultdict(int)
        for sender, receiver, amount in transactions:
            data[sender] -= amount
            data[receiver] += amount
        def dfs(index, values):
            while index < len(values) and values[index] == 0:
                index += 1
            
            if index == len(values):
                return 0
            
            cur_val = values[index]
            min_transaction = float('inf')
            for next_ind in range(index+1, len(values)):
                next_val = values[next_ind]
                if cur_val * next_val > 0:
                    continue
                values[next_ind] += cur_val
                min_transaction = min(min_transaction, dfs(index+1, values) + 1) 
                values[next_ind] -= cur_val 
            return min_transaction
        return dfs(0, list(data.values()))
        '''
        46/55 Test passed
        data = defaultdict(int)
        for sender, receiver, amount in transactions:
            data[sender] -= amount
            data[receiver] += amount
        values = sorted(data.values())
        retVal = 0
        # print(data, values)
        for val in values:
            if val != 0 and (val * -1 in values):
                values.remove(val)
                values.remove(val * -1)
                retVal += 1
        # print(data, values)
        i, j = 0, len(values) - 1
        while i < j:
            # print(values, retVal)
            if values[i] != 0 or values[j] != 0:
                retVal += 1
            tmp = values[i] + values[j]
            if tmp < 0:
                values[i] = tmp
                values[j] = 0
                j -= 1
            elif tmp > 0:
                values[j] = tmp
                values[i] = 0
                i += 1
            else:
                i += 1
                j -= 1
        return retVal
        '''
