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

class Battleship(Ship):
    def __init__(self):
        super().__init__('Battleship', 4)

class Player:
    def __init__(self,name):
        self.name = name
        self.board = [['' for _ in range(10)] for _ in range(10)]
        self.ships = []
        self.hits = [['' for _ in range(10)] for _ in range(10)]
        
    def place_boats(self):
        destroyer = Destroyer()
        submarine = Submarine()
        battleship = Battleship()
        
        self.ships.extend([destroyer,submarine,battleship])
        
        for ship in self.ships:
            direction_options = ["h", "v"]
            placed = False
            while not placed:
                direction = input(f'{self.name}, the size of this ship is {ship.size}, choose the direction for "{ship.name}" ship, type "h" for horizontal or "v" for vertical: ').strip().lower()
                if direction not in direction_options:
                    print('Please type "h" or "v" other input it is not allowed')
                else:
                    row = int(input(f'{self.name}, choose the initial row to place the ship "{ship.name}" : '))
                    column = int(input(f'{self.name},choose the initial column to place the ship "{ship.name}": '))
                    placed = ship.place_ship(self.board,column, row, direction)
                    self.print_boats()       
                    
                
                if not placed:
                    print("remember board it's just 10x10, with that postion the ship will not fit on it")
                
    def print_boats(self):
        for row in self.board:
            print(' '.join(row))
    
    def attack(self, oponent):
        valid = False
        while not valid:
            try:
                row = int(input(f"Please select a row from 0 to 9 to attack"))           
                column = int(input(f"Please select a column from 0 to 9 to attack"))  
                if 0 <= row < 10 and 0 <= column < 10:
                    valid = True 
                else:
                    print('Remember values can only be 0 to 9')  
            except ValueError:    
                print('Invalid input, Please enter a numeric value')
        if oponent.board[row][column] != ' ':
            print('HIT 💥')
            self.hits[row][column] = '✅'      
        else:
            print(' Water 🌊')
            self.hits[row][column] = '❌'      
        

player1 = Player('SrPizza')

player1.place_boats()
player1.print_boats()