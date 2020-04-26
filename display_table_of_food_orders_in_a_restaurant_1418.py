'''
1418. Display Table of Food Orders in a Restaurant
Medium

Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.

Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.


Example 1:

Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
Explanation:
The displaying table looks like:
Table,Beef Burrito,Ceviche,Fried Chicken,Water
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche".
For the table 5: Carla orders "Water" and "Ceviche".
For the table 10: Corina orders "Beef Burrito". 

https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/
'''
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = defaultdict(list)
        items, itemNo = set(), {}
        retVal = []
        for order in orders:
            if order[2] not in items:
                items.add(order[2])
            table[order[1]].append(order[2])
        retVal.append(['Table'])
        for i,item in enumerate(sorted(items)):
            itemNo[item] = i+1
            retVal[0].append(item)
        for k in sorted(table.keys(), key=lambda x: int(x)):
            retVal.append(["0"] * (len(items)+1))
            retVal[-1][0] = k
            for val in table[k]:
                retVal[-1][itemNo[val]] = str(int(retVal[-1][itemNo[val]]) + 1)
        return retVal
