'''
170. Two Sum III - Data structure design

Easy

Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.
 

Example 1:

Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false

https://leetcode.com/problems/two-sum-iii-data-structure-design/description/
'''
class TwoSum:

    def __init__(self):
        self.map = defaultdict(int)

    def add(self, number: int) -> None:
        self.map[number] += 1

    def find(self, value: int) -> bool:
        for num in self.map.keys():
            compliment = value - num
            if compliment in self.map:
                if compliment == num and self.map[num] == 1:
                    continue
                return True
        return False
    
    '''
    def __init__(self):
        self.data = []
        self.sumVals = set()

    def add(self, number: int) -> None:
        # print(self.sumVals)
        new_set = set()
        for val in self.data:
            new_set.add(val + number)
        self.data.append(number)
        self.sumVals = self.sumVals.union(new_set)
        # print(self.sumVals)
        

    def find(self, value: int) -> bool:
        return value in self.sumVals
    '''
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
