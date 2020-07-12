import numpy as np

curr_board_id = 0
game_id = 0

class Game:
    """Make a new game with 2 players and a board. Store the
        information associated with the game."""
    def __init__(self):
        global game_id
        self.game_id = game_id
        game_id += 1
        self.player_white = Player()
        self.player_black = Player()
        self.board = Board()


class Player:
    def __init__(self,board_id = 0):
        self.name = input("What is your name? ")
        self.color = input("Do you want to be black or white? ")
        self.player_type = 'Human'
        self.board_id = board_id

    def give_up(self):
        """Give up playing and throw the board"""
        self.throw_board()
        print("Player {0} of color {1} has given up!".format(self.name, self.color))

    def throw_board(self):
        for spot in self.board.spots:
            if spot.piece:
                spot.piece.location = [np.random.randint(8), np.random.randint(8)]


class Board:
    def __init__(self):
        global curr_board_id
        curr_board_id += 1
        self.id = curr_board_id
        self.color = 'Pink'
        self.spots = [[BoardSpot((row,col)) for row in range(8)] for col in range(8)]

    def reset_board(self):
        for piece in

class BoardSpot:
    def __init__(self,loc):
        self.location = loc
        self.piece = None

    def get_piece(self):
        return self.piece

    def change_piece(self, piece):
        self.piece = piece

class Piece:
    def __init__(self,piece_type):
        self.piece_type = piece_type
        self.color = 'Black'
        self.location = [0, 0]
        self.status = 'Alive'

    def move(self, new_loc):
        """Move the piece to another location on the map. """

        # Check to make sure this is a viable move
        if new_loc in self.get_move_options():
            self.location = new_loc
        else:
            print("That does not appear to be a viable option.")

    def kill(self):
        """When a player loses a piece, that piece is removed from the board. """
        self.status = 'Dead'
        self.location = [-1, -1]

    def get_move_options(self):
        """Get a list of current places this player could potentially move to. """
        list_of_options = [[0, 1], [4, 2]]
        return [list_of_options]


"""Run the script only when it's being called by this file"""
if __name__ == "__main__":
    Game()