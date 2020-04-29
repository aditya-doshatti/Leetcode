'''
First Unique Number
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
 

Example 1:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3313/
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.head = Node('head')
        self.head.prev = None
        self.tail = Node('tail')
        self.tail.prev = self.head
        self.tail.next = None
        self.unique = {}
        self.duplicates = set()
        for num in nums:
            self.add(num)
        

    def showFirstUnique(self) -> int:
        return self.head.next.value if self.head.next.value != 'tail' else -1

    def add(self, value: int) -> None:
        if value in self.duplicates:
            return
        elif value in self.unique:
            tempNode = self.unique[value]
            tempPrev = tempNode.prev
            tempPrev.next = tempNode.next
            tempNode.next.prev = tempPrev
            tempNode.next = tempNode.prev = None
            del(self.unique[value])
            self.duplicates.add(value)
            return
        else:
            newNode = Node(value)
            end = self.tail.prev
            end.next = newNode
            newNode.prev = end
            newNode.next = self.tail
            self.tail.prev = newNode
            self.unique[value] = newNode
            return


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
