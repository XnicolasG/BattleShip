class Ship:
    def __init__(self,name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0
        
    def place_ship(self,board, start_col, start_row, direction):
        rows = len(board) #horizontal length
        cols = len(board[0]) #vertical length
        
        # detecting if the ship can't fit in the board
        if direction == 'h':
            if start_col + self.size > cols:
                return False
        elif direction =='v':
            if start_row + self.size > rows:
                return False
        
        # create variable to avoid handle directly the main property self.postitons
        positions = []
        # iterate the size of the ship to verify if the position is free
        for i in range(self.size):
            if direction == 'h':
                if board[start_row][start_col + i] != '':
                    return False
                positions.append((start_row, start_col + i))
            elif direction == 'v':
                if board[start_row + i][start_col] != '':
                    return False
                positions.append((start_row + i, start_col))
        
        for row, col in positions:
            board[row][col] = self.name[0]
        self.positions = positions
        return True

    def hit(self):
        self.hits += 1
        if self.hits == self.size:
            print(f"el barco: {self.name} ha sido hundido !")        
            return True
        return False

class Destroyer(Ship):
    def __init__(self):
        super().__init__('Destructor', 2)

class Submarine(Ship):
    def __init__(self):
        super().__init__('Submarino', 3)

class Battlership(Ship):
    def __init__(self):
        super().__init__('Battleship', 4)
