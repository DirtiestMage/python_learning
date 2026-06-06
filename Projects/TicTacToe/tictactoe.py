class Player:
    def __init__(self,symbol):
        self.name = 'name'
        self.symbol = symbol
        self.score = 0
        self.positions = set()
    def __str__(self):
        return self.name
    def __int__(self):
        return self.score

def displayGrid(grid):
    print()
    for row in range(0,3):
        for col in range(0,3):
            print(grid[3*row+col],end='  ')
        print('\n')
def gameStart(p1,p2):
    print(f"{p1}: {int(p1)}")
    print(f"{p2}: {int(p2)}")
    grid = []
    p1.positions.clear()
    p2.positions.clear()
    grid = list(range(1,10))
    gameLoop(p1,p2,grid)

def gameLoop(p1,p2,grid):
    #actual game loop
    while gameNotOver(p1,p2):
        displayGrid(grid)
        playerTurn(p1,p1,p2,grid)
        if gameNotOver(p1,p2):
            displayGrid(grid)
            playerTurn(p2,p1,p2,grid)

    getWinner(p1,p2)
    retry(p1,p2,grid)

    
          
def playerTurn(p,p1,p2,grid):
    while True:
        try:
            position = int(input("Enter Position: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if position in (p1.positions | p2.positions):
            print("Please enter a valid location")
            continue

        if position not in range(1,10):
            print("Please enter a valid location")
            continue

        break

    grid[position-1]= p.symbol
    p.positions.add(position)

def getWinner(p1,p2):
    winconditions = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
    for wincon in winconditions:
        if wincon.issubset(p1.positions):
            win(p1)
            return
          
        elif wincon.issubset(p2.positions):
            win(p2)
            return

    if len(p1.positions) + len(p2.positions) == 9:
        print('The game is a Draw! ')

def gameNotOver(p1,p2):
    #checks if game is over or not
    winconditions = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
    for wincon in winconditions:
        if wincon.issubset(p1.positions):
            return False
        elif wincon.issubset(p2.positions):
            return False
    if len(p1.positions) + len(p2.positions) == 9:
        return False
    else: 
        return True
def win(p):
    print(f'{p} wins!')
    p.score += 1
def retry(p1,p2,grid):
    displayGrid(grid)
    print(f"{p1}: {int(p1)}")
    print(f"{p2}: {int(p2)}")
    rematch = input('Rematch? Y/N ')
    if rematch=='Y' or rematch == 'y':
        gameStart(p1,p2)
    elif rematch=='N' or rematch=='n':
        print('Thanks for playing! ')
    else:
        print('Invalid Input! Please try again ')
        retry(p1,p2,grid)

def main():
    #initialization of p1 and p2
    print('Welcome to TicTacToe!')
    p1 = Player('X')
    p2 = Player('O')

    p1.name = input('Enter name of Player 1: ')
    p2.name = input('Enter name of Player 2: ')
    
    gameStart(p1,p2) #game starts here
    
    
main()