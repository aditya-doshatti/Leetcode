'''
412. Fizz Buzz
Easy

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

https://leetcode.com/problems/fizz-buzz/
'''
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        retVal = []
        for a in range(1,n+1):
            if a%3 == 0 and a%5 == 0:
                retVal.append("FizzBuzz")
            elif a%3 == 0:
                retVal.append("Fizz")
            elif a%5 == 0:
                retVal.append("Buzz")
            else:
                retVal.append(str(a))
        return retVal
