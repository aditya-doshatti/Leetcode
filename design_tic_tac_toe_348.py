'''
348. Design Tic-Tac-Toe

Medium

Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
0 if there is no winner after the move,
1 if player 1 is the winner after the move, or
2 if player 2 is the winner after the move.
 

Example 1:

Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]

Explanation
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|

https://leetcode.com/problems/design-tic-tac-toe/description/
'''
class TicTacToe:
    def __init__(self, n: int):
        self.row = [0] *n
        self.col = [0] *n
        self.diag = 0
        self.anti_diag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        current_player = 1 if player == 1 else -1

        self.row[row] += current_player
        self.col[col] += current_player

        if row == col:
            self.diag += current_player
        if col == self.n - row - 1:
            self.anti_diag += current_player

        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diag) == self.n or abs(self.anti_diag) == self.n:
            return player
        return 0
    
    '''
    Accepted
    
    def __init__(self, n: int):
        self.n = n
        self.row = {}
        self.col = {}
        self.diag1 = defaultdict(int)
        self.diag2 = defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        if row not in self.row.keys():
            self.row[row] = [0, 0]
        self.row[row][player - 1] += 1
        if col not in self.col.keys():
            self.col[col] = [0, 0]
        self.col[col][player - 1] += 1
        if row == col:
            self.diag1[player] += 1
        if row + col == self.n - 1:
            self.diag2[player] += 1
        return self._checkWinner()
    
    def _checkWinner(self):
        # print(self.row, self.col, self.diag1, self.diag2)
        for key, val in self.row.items():
            if val[0] >= self.n:
                return 1
            if val[1] >= self.n:
                return 2
        for key, val in self.col.items():
            if val[0] >= self.n:
                return 1
            if val[1] >= self.n:
                return 2
        if self.diag1[1] >= self.n:
            return 1
        elif self.diag1[2] >= self.n:
            return 2
        if self.diag2[1] >= self.n:
            return 1
        elif self.diag2[2] >= self.n:
            return 2
        return 0
    '''


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
