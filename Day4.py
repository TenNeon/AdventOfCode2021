import collections
import math

def get_draws(line):
    draws_str = line.strip('\n').split(',')
    draws = []
    for i in draws_str:
        draws.append(int(i))   
    return draws

class Board:
    cells = []
    last = 0
    
    def __init__(self,rows):
        self.cells = []
        for row in rows:
            row_str = row.strip('\n').split(' ')
            if row_str == ['']: continue
            row_int = []
            for cell in row_str:
                if not cell == '':
                    row_int.append(int(cell))
            self.cells.append(row_int)
    
    def __str__(self):
        board_str = ""
        for line in self.cells:
            for cell in line:
                board_str += "{0:2} ".format(cell)
            board_str += '\n'
        return board_str
    
    def mark(self, num):
        print(num)
        for row in self.cells:
            for cell in row:
                if cell == num:
                    cell = num+100
                    last = num
                    return self.checkBingo()
        return False
                    
    def checkBingo(self):
        # check rows
        for row in self.cells:
            rowBingo = True
            for cell in row:
                if cell < 100: 
                    rowBingo = False
                    break
            if rowBingo:
                return self.score()
        
        # check cols
        for col in range(0,5):
            colBingo = True
            for row in self.cells:
                if row[col] < 100:
                    colBingo = False
                    break
            if colBingo:
                return self.score()
                
        return False
    
    def score(self):
        unmarked = 0
        for row in cells:
            for cell in row:
                if cell < 100:
                    unmarked += cell
        return unmarked * self.last
                

    
# boards are 5x5 with a space after
def get_boards(lines):
    boards = []
    count = 0
    rows = []
    lines = lines[1:]
    for i in lines:
        rows.append(i)
        if count%6 == 5:
            boards.append(Board(rows))
            rows = []
        count += 1
    boards.append(Board(rows))
    return boards
        
def day4a(file = "Input/4A.txt"):
    if file == "test":
        file = "Input/4A_test.txt"
        
    lines = []
    with open(file) as f:
        lines = f.readlines()
    
    draws = get_draws(lines[0])
    boards = get_boards(lines)

    print(draws)
    
    for board in boards:
        print(board)
        
    for draw in draws:
        for board in boards:
            val = board.mark(draw) 
            if(val != False):
                print("Win:",val)
                return
                
    for board in boards:
        print(board) 












        
def day3b(file = "Input/4A.txt"):
    if file == "test":
        file = "Input/4A_test.txt"

    lines = []
    with open(file) as f:
        lines = f.readlines()
    
    draws = get_draws(lines[0])

        
