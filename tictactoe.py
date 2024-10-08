
class Square:
    #sqaures have x or o or starting number
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str("[" + str(self.value) + "]")
    
    def change_value(self, value) -> bool:
        if self.value != "X" and self.value != "O":
            self.value = value
            return True
        else:
            print("Invalid move. Try again:")
            return False

class Board:
    #board has 9 squares
    #board needs to be printed
    def __init__(self):
        self.row = range(0,3)
        self.col = range(0,3)
        self.board = [[Square(3*j+i) for i in self.col] for j in self.row]
        self.player = False

    def print_board(self):
        for j in self.row:
            for i in self.col:
                print(self.board[j][i], end="")
            print()

    def take_turn(self, square):
        if square < 0 or square > 8:
            print("Invalid entry. Try again.")
            return
        row = square // 3
        col = square % 3
        if self.board[row][col].change_value("O" if self.player else "X"):
            self.player = not self.player
            
    def test_win(self) -> bool:
        if self.check_row() or self.check_col() or self.check_diag():
            print("Winner!")
            return True
        return False
        
    def check_row(self) -> bool:
        for row in self.board:
            if row[0].value == row[1].value == row[0].value == row[2].value:
                return True
        return False
    
    def check_col(self) -> bool:
        for col in self.col:
            if self.board[0][col].value == self.board[1][col].value == self.board[2][col].value:
                return True
        return False
    
    def check_diag(self) -> bool:
        if self.board[0][0].value == self.board[1][1].value == self.board[2][2].value:
            return True
        elif self.board[2][0].value == self.board[1][1].value == self.board[0][2].value:
            return True
        return False
    
    def get_player(self) -> str:
        if self.player:
            return "O"
        else:
            return "X"


def main():
    board = Board()
    num_turns = 0
    while not board.test_win() and num_turns < 9:
        player = board.get_player()
        print(player + "'s turn:")
        board.print_board()
        square = int(input())
        board.take_turn(square)
        num_turns += 1
    print("Game Over")

    

if __name__ == "__main__":
    main()