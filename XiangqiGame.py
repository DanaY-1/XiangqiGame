# portfolio project

# Date: 3/1/2020
# Description: This project represents the game Xiangqi. It contains a class that represents the game and game board
#              itself. It also contains classes for the game pieces.

class XiangqiGame:
    """Represents the game Xiangqi and the game board."""
    def __init__(self):
        """Represents the game Xiangqi and the game board."""
        self._header_index = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9}
        self._game_state = "UNFINISHED" #states: 'UNFINISHED', 'RED_WON', 'BLACK_WON'
        self._is_in_check = False #states: False, 'RED', 'BLACK'
        self._track_turn = "RED" #states: 'RED', 'BLACK'
        # Coordinates on the board that make up the palace on the red side of the board: [row, column]
        self._red_palace = [[1,4],[1,5],[1,6],[2,4],[2,5],[2,6],[2,4],[2,5],[2,6]]
        # Coordinates on the board that make up the palace on the black side of the board: [row, column]
        self._black_palace = [[9,4],[9,5],[9,6],[10,4],[10,5],[10,6],[11,4],[11,5],[11,6]]
        # Store captured pieces
        self._captured_pieces = []
        self._temp_captured_pieces = []
        # Initialize red pieces
        self._red_general = General("RED",[1,7])
        self._red_advisor_1 = Advisor("RED",[1,4])
        self._red_advisor_2 = Advisor("RED", [1, 6])
        self._red_elephant_1 = Elephant("RED", [1, 3])
        self._red_elephant_2 = Elephant("RED", [1, 7])
        self._red_horse_1 = Horse("RED", [1, 2])
        self._red_horse_2 = Horse("RED", [1, 8])
        self._red_rook_1 = Rook("RED", [1, 1])
        self._red_rook_2 = Rook("RED", [1, 9])
        self._red_cannon_1 = Cannon("RED", [3, 2])
        self._red_cannon_2 = Cannon("RED", [3, 8])
        self._red_soldier_1 = Soldier("RED", [4, 1])
        self._red_soldier_2 = Soldier("RED", [4, 3])
        self._red_soldier_3 = Soldier("RED", [4, 5])
        self._red_soldier_4 = Soldier("RED", [4, 7])
        self._red_soldier_5 = Soldier("RED", [4, 9])
        # Initialize black pieces
        self._black_general = General("BLACK",[11,5])
        self._black_advisor_1 = Advisor("BLACK",[11,4])
        self._black_advisor_2 = Advisor("BLACK", [11, 6])
        self._black_elephant_1 = Elephant("BLACK", [11, 3])
        self._black_elephant_2 = Elephant("BLACK", [11, 7])
        self._black_horse_1 = Horse("BLACK", [11, 2])
        self._black_horse_2 = Horse("BLACK", [11, 8])
        self._black_rook_1 = Rook("BLACK", [11, 1])
        self._black_rook_2 = Rook("BLACK", [11, 9])
        self._black_cannon_1 = Cannon("BLACK", [9, 2])
        self._black_cannon_2 = Cannon("BLACK", [9, 8])
        self._black_soldier_1 = Soldier("BLACK", [8, 1])
        self._black_soldier_2 = Soldier("BLACK", [8, 3])
        self._black_soldier_3 = Soldier("BLACK", [8, 5])
        self._black_soldier_4 = Soldier("BLACK", [8, 7])
        self._black_soldier_5 = Soldier("BLACK", [8, 9])
        # Empty board
        self._empty_board = [
            ["    ", "  a  ", "  b  ", "  c  ", "  d  ", "  e  ", "  f  ", "  g  ", "  h  ", "  i  ",'\n'],  # Header Row
            [" 1  ", "[   ]", "[   ]", "[   ]", "<   >", "<   >", "<   >", "[   ]", "[   ]", "[   ]",'\n'],  # Row 1 (RED)
            [" 2  ", "[   ]", "[   ]", "[   ]", "<   >", "<   >", "<   >", "[   ]", "[   ]", "[   ]",'\n'],  # Row 2
            [" 3  ", "[   ]", "[   ]", "[   ]", "<   >", "<   >", "<   >", "[   ]", "[   ]", "[   ]",'\n'],  # Row 3
            [" 4  ", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]",'\n'],  # Row 4
            [" 5  ", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]",'\n'],  # Row 5
            ["    ", "~~~~~", "~~~~~", "~~~~~", "~~~~~", "~~~~~", "~~~~~", "~~~~~", "~~~~~", "~~~~~",'\n'],  # RIVER
            [" 6  ", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]",'\n'],  # Row 6 (i7)
            [" 7  ", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]", "[   ]",'\n'],  # Row 7 (i8)
            [" 8  ", "[   ]", "[   ]", "[   ]", "<   >", "<   >", "<   >", "[   ]", "[   ]", "[   ]",'\n'],  # Row 8 (i9)
            [" 9  ", "[   ]", "[   ]", "[   ]", "<   >", "<   >", "<   >", "[   ]", "[   ]", "[   ]",'\n'],  # Row 9 (i10)
            ["10  ", "[   ]", "[   ]", "[   ]", "<   >", "<   >", "<   >", "[   ]", "[   ]", "[   ]",'\n'],  # Row 10 (BLACK)
        ]
        # Initialize the board to it's initial state. Reference for board indices: board[row][column]
        self._board = [
            [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i",'\n'],  # Header Row
            ['1', self._red_rook_1, self._red_horse_1, self._red_elephant_1, self._red_advisor_1, self._red_general,
             self._red_advisor_2, self._red_elephant_2, self._red_horse_2, self._red_rook_2, '\n'],  # Row 1 (RED)
            ['2', '0', '0', '0', '0', '0', '0', '0', '0', '0','\n'],  # Row 2
            ['3', '0', self._red_cannon_1, '0', '0', '0', '0', '0', self._red_cannon_2, '0','\n'],  # Row 3
            ['4', self._red_soldier_1, '0', self._red_soldier_2, '0', self._red_soldier_3, '0', self._red_soldier_4,
             '0', self._red_soldier_5,'\n'],  # Row 4
            ['5', '0', '0', '0', '0', '0', '0', '0', '0', '0','\n'],  # Row 5
            ['', '~', '~', '~', '~', '~', '~', '~', '~', '~','\n'],  # RIVER
            ['6', '0', '0', '0', '0', '0', '0', '0', '0', '0','\n'],  # Row 6 (i7)
            ['7', self._black_soldier_1, '0', self._black_soldier_2, '0', self._black_soldier_3, '0',
             self._black_soldier_4, '0', self._black_soldier_5,'\n'],  # Row 7 (i8)
            ['8', '0', self._black_cannon_1, '0', '0', '0', '0', '0', self._black_cannon_2, '0','\n'],  # Row 8 (i9)
            ['9', '0', '0', '0', '0', '0', '0', '0', '0', '0','\n'],  # Row 9 (i10)
            ['10', self._black_rook_1, self._black_horse_1, self._black_elephant_1, self._black_advisor_1,
             self._black_general, self._black_advisor_2, self._black_elephant_2, self._black_horse_2,
             self._black_rook_2,'\n'],  # Row 10 (BLACK)
        ]

    def print_board(self):
        """Prints the board."""
        for x in range(0,12):
            for y in range(0,11):
                if type(self._board[x][y]) == str:
                    print(self._empty_board[x][y], end='')
                else:
                    print(self._empty_board[x][y][0], self._board[x][y]._acronym, self._empty_board[x][y][4], end='')

    def get_game_state(self):
        """Returns the current state of the game."""
        return self._game_state

    def get_piece(self, column_row):
        """Takes as a parameter the column_row dictionary location for a square on the board and returns the piece
        object occupying that square.
        """
        return self._board[column_row['row']][column_row['column']]

    def get_piece_rev1(self, column_row, board):
        """Takes as a parameter the column_row dictionary location for a square and a board and returns the piece
        object occupying that square.
        """
        return board[column_row['row']][column_row['column']]

    def player_in_check(self, board):
        """Takes as a parameter a temporary board (that is a separate instance from the game board) and check's to
        see if any player is currently in check. It will return the color of the side that is in check: 'RED' or
        'BLACK'. If the player whose turn it is makes a move that results in its own General being in check then it
        will return the string "Can't put your own General in check". Otherwise, if no player is in check it will
        return False.
        """
        # Find the location of the RED side's General
        for coordinate in self._red_palace:
            if type(board[coordinate[0]][coordinate[1]]) != str:
                if board[coordinate[0]][coordinate[1]].get_piece_type() == 'General':
                    red_generals_location = coordinate
        # Find the location of the BLACK side's General
        for coordinate in self._black_palace:
            if type(board[coordinate[0]][coordinate[1]]) != str:
                if board[coordinate[0]][coordinate[1]].get_piece_type() == 'General':
                    black_generals_location = coordinate
        # For every square on the board, check to see if it contains a piece. If it does, iterate through all
        # squares on the board and pass it to the piece's verify_legal_move to see if it is legal. If it lands on
        # the opposing color's General, then that team is in check.
        all_possible_rows = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
        for possible_row in all_possible_rows:
            for column in range(1, 10):
                from_sq_dict = {'column': column, 'row': possible_row}
                if type(board[from_sq_dict['row']][from_sq_dict['column']]) != str:
                    # Identify what piece is in that square
                    temp_piece = board[from_sq_dict['row']][from_sq_dict['column']]
                    # Iterate through all squares on the board to see if that piece is able to make a legal move
                    for possible_row_move in all_possible_rows:
                        for column_move in range(1, 10):
                            to_sq_dict = {'column': column_move, 'row': possible_row_move}
                            try:
                                legal_piece_move = temp_piece.verify_legal_move(from_sq_dict, to_sq_dict)
                            except TypeError:
                                legal_piece_move = temp_piece.verify_legal_move(from_sq_dict, to_sq_dict, board)
                            # If the move is legal and it lands on the opposing general, then the opposing side is in
                            # check.
                                if legal_piece_move is not False:
                                    # If it is RED's turn, and BLACK is able to make a legal move that puts RED in check
                                    # then the function will not allow the move to be made and will return a
                                    # string statement instead.
                                    if self._track_turn == 'RED' and temp_piece.get_color() == 'BLACK':
                                        if [to_sq_dict['row'], to_sq_dict['column']] == red_generals_location:
                                            #print("Can't put your own General in check")
                                            return "Can't put your own General in check"
                                    # If it is BLACK's turn, and RED is able to make a legal move that puts BLACK in
                                    # check then the function will not allow the move to be made and will return a
                                    # string statement instead.
                                    elif self._track_turn == 'BLACK' and temp_piece.get_color() == 'RED':
                                        if [to_sq_dict['row'], to_sq_dict['column']] == black_generals_location:
                                            #print("Can't put your own General in check")
                                            return "Can't put your own General in check"
                                    # Otherwise if RED is able to make a move that puts BLACK in check, then it will
                                    # return "BLACK"
                                    elif temp_piece.get_color() == 'RED':
                                        if [to_sq_dict['row'], to_sq_dict['column']] == black_generals_location:
                                            return "BLACK"
                                    # Otherwise if BLACK is able to make a move that puts RED in check, then it will
                                    # return "RED"
                                    elif temp_piece.get_color() == 'BLACK':
                                        if [to_sq_dict['row'], to_sq_dict['column']] == red_generals_location:
                                            return "RED"
        return False

    def temp_make_move_for_check(self, move_piece, to_sq_dict):
        """Takes as a parameters the piece being moved and the square it is being moved to and checks all possible
        moves that the piece being moved can make on it's next move. If the piece is able to land on the opposing
        side's General's square on it's next move, then the opposing side is in check and the function returns the
        color of the General that is in check.
        """
        # Find the location of the opposing side's General
        if move_piece.get_color() == 'BLACK':
            for coordinate in self._red_palace:
                if type(self._board[coordinate[0]][coordinate[1]]) != str:
                    if self._board[coordinate[0]][coordinate[1]].get_piece_type() == 'General':
                        generals_location = coordinate
                        generals_color = 'RED'
        else:
            for coordinate in self._black_palace:
                if type(self._board[coordinate[0]][coordinate[1]]) != str:
                    if self._board[coordinate[0]][coordinate[1]].get_piece_type() == 'General':
                        generals_location = coordinate
                        generals_color = 'BLACK'
        # Reassign the piece's current square to the potential from square.
        from_sq_dict = to_sq_dict
        # Iterate through all possible moves of the move piece
        # Create temporary board
        temp_board3 = []
        for row in self._board:
            temp_board3.append(row)
        all_possible_rows = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
        for possible_row in all_possible_rows:
            for column in range(1, 10):
                to_sq_dict = {'column': column, 'row': possible_row}
                # Check to see if the move is legal for that piece
                try:
                    legal_piece_move = move_piece.verify_legal_move(from_sq_dict, to_sq_dict)
                except TypeError:
                    legal_piece_move = move_piece.verify_legal_move(from_sq_dict, to_sq_dict, temp_board3)
                # If the move is legal and it lands on the opposing general, then the opposing side is in check.
                if legal_piece_move is not False and [to_sq_dict['row'], to_sq_dict['column']] == generals_location:
                    return generals_color
        return False

    def is_in_check(self, color):
        """Takes as a parameter 'red' or 'black' and returns True if that player is in check, but returns False
        otherwise.
        """
        color = color.upper()
        if color == self._is_in_check:
            return True
        else:
            return False

    def convert_sq_input(self, sq_input):
        """Takes as a parameter square coordinates ('h6') and maps the coordinates to their corresponding
         board indices (for example h6 = column:8, row:7). It returns the column and row indices as a dictionary.
         """
        try:
            column = self._header_index[sq_input[0]]
        except KeyError:
            column = -1
        # If either square entered is in row 6 or higher, add 1 to the row to skip the RIVER list
        row = int(sq_input[1:])
        if row >= 6:
            row += 1
        # Store the square's column and row in a dictionary
        column_row = {'column':column, 'row':row}
        #print('column_row', column_row)
        return column_row

    def temp_make_move_for_player_in_check_checkmate(self, from_sq_dict, to_sq_dict, board):
        """This function works with the function make_move_rev1 and player_in_check. The function make_move_rev1 passes
        parameters to this function to make a temporary move on a temporary board. This function is similar to make_move_rev1 but
        contains less restrictions on movement rules to allow greater ability to make pieces move temporarily.

        It does not check which player's turn it is and it does not check the game state.

        This function then passes the temporary board it has updated to the function player_in_check to check to see
        if the temporary move it just made gets the player out of check.

        Takes three parameters that represent the square moved from and the square moved to. If the indicated move is
        not legal, then it should return False. Otherwise, it should make the indicated move, on the temporary board
        that is passed to it, temporarily remove any captured pieces, and return False if the move is not legal or
        return "Not checkmate" if the player is in check, but it can make a move that results in it not being in check.
        """
        # Verify that the move is legal - If the square being moved from or the square being moved to is not within the
        # confines of the board then the return value should be False.
        if from_sq_dict['column'] < 1 or from_sq_dict['column'] > 9:
            return False
        if from_sq_dict['row'] < 1 or from_sq_dict['row'] > 11:
            return False
        if to_sq_dict['column'] < 1 or to_sq_dict['column'] > 9:
            return False
        if to_sq_dict['row'] < 1 or to_sq_dict['row'] > 11:
            return False
        # Verify that the square identified contains a piece object.
        if type(board[from_sq_dict['row']][from_sq_dict['column']]) == str:
            #print("must move a piece. Can't move an empty square")
            return False
        # Verify that the move is legal - check that the move is legal for that specific type of piece
        move_piece = self.get_piece_rev1(from_sq_dict, board)
        #print('move_piece is:', move_piece)
        # Some pieces require the board to be passed as a parameter, others do not. The try statement accounts for the
        # different number of parameters required to be passed for different pieces.
        try:
            legal_piece_move = move_piece.verify_legal_move(from_sq_dict, to_sq_dict)
        except TypeError:
            legal_piece_move = move_piece.verify_legal_move(from_sq_dict, to_sq_dict, board)
        if legal_piece_move is False:
            #print('move is not legal')
            return False
        # Verify that the move is legal - check that the to square for the move being made does not contain a piece
        # of the same color. If the piece is of the opponent's side, remove the piece from the board.
        to_sq_piece = self.get_piece_rev1(to_sq_dict, board)
        if type(to_sq_piece) != str:
            if move_piece.get_color() == to_sq_piece.get_color():
                #print("you can't move to a spot your color already occupies")
                return False
            else:
                captured_piece = True
                self._temp_captured_pieces.append(to_sq_piece)
                board[to_sq_dict['row']][to_sq_dict['column']] = move_piece
                board[from_sq_dict['row']][from_sq_dict['column']] = '0'
        else:
            captured_piece = False
            board[to_sq_dict['row']][to_sq_dict['column']] = move_piece
            board[from_sq_dict['row']][from_sq_dict['column']] = '0'
        # Verify that the move is legal - check that the to square for the move being made does not result in General's
        # of opposing sides facing each other in the same file/column. If the General's are facing each other, reset
        # the move to it's previous state and return False.
        if self.check_generals_see_each_other() is True:
            #print("generals_see_each_other")
            board[from_sq_dict['row']][from_sq_dict['column']] = move_piece
            if captured_piece is True:
                board[to_sq_dict['row']][to_sq_dict['column']] = self._temp_captured_pieces[-1]
                self._temp_captured_pieces = self._temp_captured_pieces[:-1]
            else:
                board[to_sq_dict['row']][to_sq_dict['column']] = '0'
                # Check to see if the new move puts it's own side in check. If so, reset the move to it's previous state
                # and return False
                is_in_check_color = self.player_in_check(board)
                if is_in_check_color == "Can't put your own General in check":
                    board[from_sq_dict['row']][from_sq_dict['column']] = move_piece
                    if captured_piece is True:
                        board[to_sq_dict['row']][to_sq_dict['column']] = self._temp_captured_pieces[-1]
                        self._temp_captured_pieces = self._captured_pieces[:-1]
                    else:
                        board[to_sq_dict['row']][to_sq_dict['column']] = '0'
                    return False
            # Check to see if the new move results in a check.
            is_in_check_color = self.player_in_check(board)
            if is_in_check_color == "Can't put your own General in check":
                board[from_sq_dict['row']][from_sq_dict['column']] = move_piece
                if captured_piece is True:
                    board[to_sq_dict['row']][to_sq_dict['column']] = self._temp_captured_pieces[-1]
                    self._temp_captured_pieces = self._temp_captured_pieces[:-1]
                else:
                    board[to_sq_dict['row']][to_sq_dict['column']] = '0'
                return False
            if is_in_check_color is not False:
                if move_piece.get_color() != is_in_check_color:
                    # If the temporary move doesn't result in getting the General out of check, then
                    # reset the temporary board
                    board[from_sq_dict['row']][from_sq_dict['column']] = move_piece
                    if captured_piece is True:
                        board[to_sq_dict['row']][to_sq_dict['column']] = self._temp_captured_pieces[-1]
                        self._temp_captured_pieces = self._temp_captured_pieces[:-1]
                    else:
                        board[to_sq_dict['row']][to_sq_dict['column']] = '0'
                    return "Not checkmate"

    def make_move_rev1(self, from_sq, to_sq):
        """This make_move_rev1 is a revision of the method make_move. This function tries to improve upon the
        function make_move by incorporating a checkmate determination and passing this to the parameter
        self._game_state to make a determination on the game state.

        From make_move:
        Takes two parameters that represent the square moved from and the square moved to. For example,
        make_move('b3, 'b10'). If the square being moved from does not contain a piece belonging to the player whose
        turn it is, or if the indicated move is not legal, or if the game has already been won, then it should return
        False. Otherwise, it should make the indicated move, remove any captured pieces, update the game state,
        update the player's turn, and return True.
        """
        # Check that the game has not already been won
        if self._game_state != 'UNFINISHED':
            #print('GAME STATE IS NOT UNFINISHED')
            return False
        # Convert the board square inputs from alphanumeric strings to be in terms of board indices
        from_sq_dict = self.convert_sq_input(from_sq)
        to_sq_dict = self.convert_sq_input(to_sq)
        # Store variable for Soldier crossed river check
        change_soldier_crossed_river = False
        # Verify that the move is legal - If the square being moved from or the square being moved to is not within the
        # confines of the board then the return value should be False.
        if from_sq_dict['column'] < 1 or from_sq_dict['column'] > 9:
            return False
        if from_sq_dict['row'] < 1 or from_sq_dict['row'] > 11:
            return False
        if to_sq_dict['column'] < 1 or to_sq_dict['column'] > 9:
            return False
        if to_sq_dict['row'] < 1 or to_sq_dict['row'] > 11:
            return False
        # Verify that the square identified contains a piece object.
        if type(self._board[from_sq_dict['row']][from_sq_dict['column']]) == str:
            #print("must move a piece. Can't move an empty square")
            return False
        # Verify that the move is legal - check that the move is legal for that specific type of piece
        move_piece = self.get_piece(from_sq_dict)
        #print('move_piece is:', move_piece)
        # Some pieces require the board to be passed as a parameter, others do not. The try statement accounts for the
        # different number of parameters required to be passed for different pieces.
        try:
            legal_piece_move = move_piece.verify_legal_move(from_sq_dict, to_sq_dict)
        except TypeError:
            legal_piece_move = move_piece.verify_legal_move(from_sq_dict, to_sq_dict, self._board)
        if legal_piece_move is False:
            #print('move is not legal')
            return False
        # Verify that the move is legal - check that the piece being moved is of the color for the given turn
        if move_piece.get_color() != self._track_turn:
            #print("It's not your turn! It's this person's turn:", self._track_turn)
            #print("This is your color:", move_piece.get_color())
            return False
        # Verify that the move is legal - check that the to square for the move being made does not contain a piece
        # of the same color. If the piece is of the opponent's side, remove the piece from the board.
        to_sq_piece = self.get_piece(to_sq_dict)
        if type(to_sq_piece) != str:
            if move_piece.get_color() == to_sq_piece.get_color():
                #print("you can't move to a spot your color already occupies")
                return False
            else:
                captured_piece = True
                self._captured_pieces.append(to_sq_piece)
                self._board[to_sq_dict['row']][to_sq_dict['column']] = move_piece
                self._board[from_sq_dict['row']][from_sq_dict['column']] = '0'
                # If the piece is a Soldier, set crossed_river state if it has crossed the river
                if move_piece.get_piece_type() == 'Soldier':
                    #print('The piece is a soldier')
                    if move_piece.get_color == 'RED' and to_sq_dict['row'] > 5:
                        changed_soldier_crossed_river = True
                        move_piece.set_crossed_river(True)
                    elif move_piece.get_color == 'BLACK' and to_sq_dict['row'] < 6:
                        move_piece.set_crossed_river(True)
                        changed_soldier_crossed_river = True
        else:
            captured_piece = False
            self._board[to_sq_dict['row']][to_sq_dict['column']] = move_piece
            self._board[from_sq_dict['row']][from_sq_dict['column']] = '0'
            # If the piece is a Soldier, set crossed_river state if it has crossed the river
            if move_piece.get_piece_type() == 'Soldier':
                #print('The piece is a soldier')
                if move_piece.get_color() == 'RED' and from_sq_dict['row'] > 5:
                    change_soldier_crossed_river = False
                elif move_piece.get_color() == 'RED' and to_sq_dict['row'] > 5:
                    change_soldier_crossed_river = True
                    move_piece.set_crossed_river(True)
                elif move_piece.get_color() == 'BLACK' and from_sq_dict['row'] < 6:
                    change_soldier_crossed_river = False
                elif move_piece.get_color() == 'BLACK' and to_sq_dict['row'] < 6:
                    change_soldier_crossed_river = True
                    move_piece.set_crossed_river(True)
        # Verify that the move is legal - check that the to square for the move being made does not result in General's
        # of opposing sides facing each other in the same file/column. If the General's are facing each other, reset
        # the move to it's previous state and return False.
        if self.check_generals_see_each_other() is True:
            #print("generals_see_each_other")
            self._board[from_sq_dict['row']][from_sq_dict['column']] = move_piece
            if captured_piece is True:
                self._board[to_sq_dict['row']][to_sq_dict['column']] = self._captured_pieces[-1]
                self._captured_pieces = self._captured_pieces[:-1]
            else:
                self._board[to_sq_dict['row']][to_sq_dict['column']] = '0'
            # If the Soldier's crossed_river state had been changed, reset it
            if change_soldier_crossed_river is True:
                move_piece.set_crossed_river(False)
                change_soldier_crossed_river = False
            return False
        # ----------------------------------------------------------------------------------------------------------
        # Check to see if the new move puts it's own side in check. If so, reset the move to it's previous state and
        # return False.
        # Create a temporary instance of the board to pass to the function. The function it is passed to makes
        # temporary moves on the temporary board to determine which player is in check.
        temp_board2 = []
        for row in self._board:
            temp_board2.append(row)
        is_in_check_color = self.player_in_check(temp_board2)
        # If the move puts its own General in check, reset the move to its previous state and return False.
        if is_in_check_color == "Can't put your own General in check":
            self._board[from_sq_dict['row']][from_sq_dict['column']] = move_piece
            # Return any captured pieces back to the board
            if captured_piece is True:
                self._board[to_sq_dict['row']][to_sq_dict['column']] = self._captured_pieces[-1]
                self._captured_pieces = self._captured_pieces[:-1]
            # If the square being moved to did not previously contain a piece, reset the square to '0'
            else:
                self._board[to_sq_dict['row']][to_sq_dict['column']] = '0'
            # If the Soldier's crossed_river state had been changed, reset it
            if change_soldier_crossed_river is True:
                move_piece.set_crossed_river(False)
                change_soldier_crossed_river = False
            return False
        # Check to see if the new move puts the opposing General in check and store it's color.
        if is_in_check_color is not False:
            self._is_in_check = is_in_check_color
            # If the move puts the opposing team in check, check to see if there is a checkmate.
            # First, identify which color is in check.
            if self._track_turn == 'RED':
                temp_move_color = 'BLACK'
            else:
                temp_move_color = 'RED'
            # Create a temporary board that refers to a separate object from the game's board
            temp_board = []
            for row in self._board:
                temp_board.append(row)
            # For every square on the board, check to see if it contains a piece of the color that is in check.
            all_possible_rows = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
            for possible_row in all_possible_rows:
                for column in range(1, 10):
                    temp_from_sq_dict = {'column': column, 'row': possible_row}
                    if type(temp_board[temp_from_sq_dict['row']][temp_from_sq_dict['column']]) != str:
                        temp_piece = temp_board[temp_from_sq_dict['row']][temp_from_sq_dict['column']]
                        if temp_piece.get_color() == temp_move_color:
                            # If it finds a piece of the color it is searching for, then iterate through all squares on
                            # the board and pass it to player_in_check to make a temporary move on a
                            # temporary version of the board. This is to see if the move is legal as well as to check
                            # if it removes the General from being in check.
                            for possible_row_move in all_possible_rows:
                                for column_move in range(1, 10):
                                    temp_to_sq_dict = {'column': column_move, 'row': possible_row_move}
                                    try_move = self.temp_make_move_for_player_in_check_checkmate(temp_from_sq_dict, temp_to_sq_dict, temp_board)
                                    if try_move != "Not checkmate":
                                        if self._track_turn == 'RED':
                                            self._game_state = 'BLACK_WON'
                                        else:
                                            self._game_state = 'RED_WON'
        # Update whose turn it is, and return True.
        if self._track_turn == 'RED':
            self._track_turn = 'BLACK'
        else:
            self._track_turn = 'RED'
        return True

    def make_move(self, from_sq, to_sq):
        """Takes two parameters that represent the square moved from and the square moved to. For example,
        make_move('b3, 'b10'). If the square being moved from does not contain a piece belonging to the player whose
        turn it is, or if the indicated move is not legal, or if the game has already been won, then it should return
        False. Otherwise, it should make the indicated move, remove any captured pieces, update the game state,
        update the player's turn, and return True.
        """
        # Check that the game has not already been won
        if self._game_state != 'UNFINISHED':
            #print('GAME STATE IS NOT UNFINISHED')
            return False
        # Convert the board square inputs from alphanumeric strings to be in terms of board indices
        from_sq_dict = self.convert_sq_input(from_sq)
        to_sq_dict = self.convert_sq_input(to_sq)
        # Store variable for Soldier crossed river check
        change_soldier_crossed_river = False
        # Verify that the move is legal - If the square being moved from or the square being moved to is not within the
        # confines of the board then the return value should be False.
        if from_sq_dict['column'] < 1 or from_sq_dict['column'] > 9:
            return False
        if from_sq_dict['row'] < 1 or from_sq_dict['row'] > 11:
            return False
        if to_sq_dict['column'] < 1 or to_sq_dict['column'] > 9:
            return False
        if to_sq_dict['row'] < 1 or to_sq_dict['row'] > 11:
            return False
        # Verify that the square identified contains a piece object.
        if type(self._board[from_sq_dict['row']][from_sq_dict['column']]) == str:
            #print("must move a piece. Can't move an empty square")
            return False
        # Verify that the move is legal - check that the move is legal for that specific type of piece
        move_piece = self.get_piece(from_sq_dict)
        #print('move_piece is:', move_piece)
        # Some pieces require the board to be passed as a parameter, others do not. The try statement accounts for the
        # different number of parameters required to be passed for different pieces.
        try:
            legal_piece_move = move_piece.verify_legal_move(from_sq_dict, to_sq_dict)
        except TypeError:
            legal_piece_move = move_piece.verify_legal_move(from_sq_dict, to_sq_dict, self._board)
        if legal_piece_move is False:
            #print('move is not legal')
            return False
        # Verify that the move is legal - check that the piece being moved is of the color for the given turn
        if move_piece.get_color() != self._track_turn:
            #print("It's not your turn! It's this person's turn:", self._track_turn)
            #print("This is your color:", move_piece.get_color())
            return False
        # Verify that the move is legal - check that the to square for the move being made does not contain a piece
        # of the same color. If the piece is of the opponent's side, remove the piece from the board.
        to_sq_piece = self.get_piece(to_sq_dict)
        if type(to_sq_piece) != str:
            if move_piece.get_color() == to_sq_piece.get_color():
                #print("you can't move to a spot your color already occupies")
                return False
            else:
                captured_piece = True
                self._captured_pieces.append(to_sq_piece)
                self._board[to_sq_dict['row']][to_sq_dict['column']] = move_piece
                self._board[from_sq_dict['row']][from_sq_dict['column']] = '0'
                # If the piece is a Soldier, set crossed_river state if it has crossed the river
                if move_piece.get_piece_type() == 'Soldier':
                    #print('The piece is a soldier')
                    if move_piece.get_color == 'RED' and to_sq_dict['row'] > 5:
                        changed_soldier_crossed_river = True
                        move_piece.set_crossed_river(True)
                    elif move_piece.get_color == 'BLACK' and to_sq_dict['row'] < 6:
                        move_piece.set_crossed_river(True)
                        changed_soldier_crossed_river = True
        else:
            captured_piece = False
            self._board[to_sq_dict['row']][to_sq_dict['column']] = move_piece
            self._board[from_sq_dict['row']][from_sq_dict['column']] = '0'
            # If the piece is a Soldier, set crossed_river state if it has crossed the river
            if move_piece.get_piece_type() == 'Soldier':
                #print('The piece is a soldier')
                if move_piece.get_color() == 'RED' and from_sq_dict['row'] > 5:
                    change_soldier_crossed_river = False
                elif move_piece.get_color() == 'RED' and to_sq_dict['row'] > 5:
                    change_soldier_crossed_river = True
                    move_piece.set_crossed_river(True)
                elif move_piece.get_color() == 'BLACK' and from_sq_dict['row'] < 6:
                    change_soldier_crossed_river = False
                elif move_piece.get_color() == 'BLACK' and to_sq_dict['row'] < 6:
                    change_soldier_crossed_river = True
                    move_piece.set_crossed_river(True)
        # Verify that the move is legal - check that the to square for the move being made does not result in General's
        # of opposing sides facing each other in the same file/column. If the General's are facing each other, reset
        # the move to it's previous state and return False.
        if self.check_generals_see_each_other() is True:
            #print("generals_see_each_other")
            self._board[from_sq_dict['row']][from_sq_dict['column']] = move_piece
            if captured_piece is True:
                self._board[to_sq_dict['row']][to_sq_dict['column']] = self._captured_pieces[-1]
                self._captured_pieces = self._captured_pieces[:-1]
            else:
                self._board[to_sq_dict['row']][to_sq_dict['column']] = '0'
            # If the Soldier's crossed_river state had been changed, reset it
            if change_soldier_crossed_river is True:
                move_piece.set_crossed_river(False)
                change_soldier_crossed_river = False
            return False
        # Check to see if the new move puts the opposing General in check and store it's color.
        is_in_check_color = self.temp_make_move_for_check(move_piece, to_sq_dict)
        if is_in_check_color is not False:
            self._is_in_check = is_in_check_color

        # Update the game state if necessary.

        # Update whose turn it is, and return True.
        if self._track_turn == 'RED':
            self._track_turn = 'BLACK'
        else:
            self._track_turn = 'RED'
        return True

    def check_generals_see_each_other(self):
        """Takes no parameters. Verifies that General's on the board do not "see" each other. That is, General's of
        opposing sides are not in the same file unless another piece is blocking them.
        """
        generals_in_same_column = False
        # Find the location of the General in the red palace
        for point in self._red_palace:
            if type(self._board[point[0]][point[1]]) != str and \
                    self._board[point[0]][point[1]].get_piece_type() == 'General':
                red_general_pos = point
        # Check to see if the Black General is in the same column as the Red General
        for row in range(9, 12):
            if type(self._board[row][red_general_pos[1]]) != str and \
                    self._board[row][red_general_pos[1]].get_piece_type() == 'General':
                black_general_pos = [row, red_general_pos[1]]
                generals_in_same_column = True
        if generals_in_same_column is False:
            return False
        # If Generals are in the same column check to see if another piece is blocking them in that column
        elif generals_in_same_column is True:
            for row in range(red_general_pos[0]+1, black_general_pos[0]):
                if type(self._board[row][red_general_pos[1]]) != str:
                    #print("The Generals do not see each other. A piece is blocking.")
                    return False
            return True

class Piece:
    """Represents a piece on the game board."""
    def __init__(self, _color, _position, _acronym, _piece_type):
        """Returns a piece with the specified attributes."""
        self._color = _color #states: "RED", "BLACK"
        self._position = _position
        self._acronym = _acronym
        self._piece_type = _piece_type

    def get_color(self):
        """Returns the color of the game piece."""
        return self._color

    def get_piece_type(self):
        """Returns the type of the game piece."""
        return self._piece_type

class General(Piece):
    """Represents a piece of type General."""

    def __init__(self, _color, _position):
        """Returns a piece of type General with the specified attributes."""
        super().__init__(_color, _position, _acronym='G', _piece_type='General')

    def verify_legal_move(self, from_sq_dict, to_sq_dict):
        """Takes two parameters that represent the square moved from and the square moved to. General's may move and
        capture one point orthogonally and must stay within the palace (confined to 5 points on the board). If the move
        being made does not follow the rules for the General's movement and capture abilities the method will return
        False.
        """
        # Verify that the to square for the move being made is within the confines of the palace columns (d:4 to f:6)
        if to_sq_dict['column'] < 4 or to_sq_dict['column'] > 6:
            return False
        # Verify that the to square for the move being made is within the confines of the palace rows for that color
        if self._color == "RED":
            if to_sq_dict['row'] < 1 or to_sq_dict['row'] > 3:
                return False
        if self._color == "BLACK":
            if to_sq_dict['row'] < 9:
                return False
        # Verify that the move being made is orthogonal to it's previous position.
        # If the move being made changes the column by 1, verify that it is moving within the same row.
        if to_sq_dict['column'] == from_sq_dict['column'] + 1 or to_sq_dict['column'] == from_sq_dict['column'] - 1:
            if to_sq_dict['row'] != from_sq_dict['row']:
                return False
            else:
                return True
        # If the move being made changes the row by 1, verify that it is moving within the same column.
        if to_sq_dict['row'] == from_sq_dict['row'] + 1 or to_sq_dict['row'] == from_sq_dict['row'] - 1:
            if to_sq_dict['column'] != from_sq_dict['column']:
                return False
            else:
                return True
        # If none of the above conditions are True, then the move being made is not orthogonal and should return False.
        else:
            return False

class Advisor(Piece):
    """Represents a piece of type Advisor."""

    def __init__(self, _color, _position):
        """Returns a piece of type Advisor with the specified attributes."""
        super().__init__(_color, _position, _acronym='A', _piece_type='Advisor')

    def verify_legal_move(self, from_sq_dict, to_sq_dict):
        """Takes two parameters that represent the square moved from and the square moved to. Advisor's may move and
        capture one point diagonally and must stay within the palace (confined to 5 points on the board). If the move
        being made does not follow the rules for the Advisor's movement and capture abilities the method will return
        False.
        """
        # Verify that the to square for the move being made is within the confines of the palace columns (d:4 to f:6)
        if to_sq_dict['column'] < 4 or to_sq_dict['column'] > 6:
            return False
        # Verify that the to square for the move being made is within the confines of the palace rows for that color
        if self._color == "RED":
            if to_sq_dict['row'] < 1 or to_sq_dict['row'] > 3:
                return False
        if self._color == "BLACK":
            if to_sq_dict['row'] < 9:
                return False
        # Verify that the move being made is diagonal to it's previous position.
        if to_sq_dict['row'] != from_sq_dict['row']+1 and to_sq_dict['row'] != from_sq_dict['row']-1:
            #print("move isn't diagonal for row")
            return False
        if to_sq_dict['column'] != from_sq_dict['column']+1 and to_sq_dict['column'] != from_sq_dict['column']-1:
            #print("move isn't diagonal for column")
            return False
        # If none of the above conditions are true, then the move is legal
        else:
            return True

class Elephant(Piece):
    """Represents a piece of type Elephant."""

    def __init__(self, _color, _position):
        """Returns a piece of type Elephant with the specified attributes."""
        super().__init__(_color, _position, _acronym='E', _piece_type='Elephant')

    def verify_legal_move(self, from_sq_dict, to_sq_dict, board):
        """Takes three parameters that represent the square moved from, the square moved to, and the boad.
        Elephant's may move and capture two points diagonally (exactly) and may not jump over intervening pieces or
        cross the river (confined to 7 board positions). If the move being made does not follow the rules for the
        Elephant's movement and capture abilities the method will return False.
        """
        # Verify that the to square for the move being made does not cross the river (row 6)
        if self._color == 'RED':
            if to_sq_dict['row'] > 5:
                return False
        elif self._color == 'BLACK':
            if to_sq_dict['row'] < 6:
                return False
        # Verify that the move being made is two points diagonal to it's previous position.
        if to_sq_dict['row'] != from_sq_dict['row']+2 and to_sq_dict['row'] != from_sq_dict['row']-2:
            #print("move isn't 2 points diagonal for row")
            return False
        if to_sq_dict['column'] != from_sq_dict['column']+2 and to_sq_dict['column'] != from_sq_dict['column']-2:
            #print("move isn't 2 points diagonal for column")
            return False
        # Verify that a piece is not being jumped - First, check which direction the piece is being moved on the board.
        if to_sq_dict['row'] - from_sq_dict['row'] == 2:
            row_direction = 'south'
        else:
            row_direction = 'north'
        if to_sq_dict['column'] - from_sq_dict['column'] == 2:
            column_direction = 'east'
        else:
            column_direction = 'west'
        # Once the direction is known, check if the point along the diagonal does not contain a piece.
        if row_direction == 'south' and column_direction == 'east':
            if type(board[from_sq_dict['row'] + 1][from_sq_dict['column'] + 1]) != str:
                #print("1 - cannot jump over another piece")
                return False
        elif row_direction == 'south' and column_direction == 'west':
            if type(board[from_sq_dict['row'] + 1][from_sq_dict['column'] - 1]) != str:
                #print("2 - cannot jump over another piece")
                return False
        elif row_direction == 'north' and column_direction == 'east':
            if type(board[from_sq_dict['row'] - 1][from_sq_dict['column'] + 1]) != str:
                #print("3 - cannot jump over another piece")
                return False
        elif row_direction == 'north' and column_direction == 'west':
            if type(board[from_sq_dict['row'] - 1][from_sq_dict['column'] - 1]) != str:
                #print("4 - cannot jump over another piece")
                return False
        # If none of the above conditions are true, then the move is legal
        else:
            return True

class Horse(Piece):
    """Represents a piece of type Horse."""

    def __init__(self, _color, _position):
        """Returns a piece of type Horse with the specified attributes."""
        super().__init__(_color, _position, _acronym='H', _piece_type='Horse')

    def verify_legal_move(self, from_sq_dict, to_sq_dict, board):
        """Takes three parameters that represent the square moved from, the square moved to, and the board.
        Horse's may move and capture one point orthogonally and one point diagonally and may not jump over intervening
        pieces. That is if another piece is located horizontally or vertically adjacent to the horse, the horse is
        blocked in that direction. If the move being made does not follow the rules for the Horse's movement and
        capture abilities the method will return False.
        """
        # These are the possible combinations for row and column deltas that a Horse may move
        possible_row_column_deltas = [[1, 2],[1, -2],[-1, 2],[-1, -2],
                                      [2, 1],[2, -1],[-2, -1],[-2, 1]]
        # Calculate row_delta. Adjust for moves that cross the river
        if to_sq_dict['row'] < 6 and from_sq_dict['row'] < 6:
            row_delta = to_sq_dict['row'] - from_sq_dict['row']
        elif to_sq_dict['row'] > 5 and from_sq_dict['row'] > 5:
            row_delta = to_sq_dict['row'] - from_sq_dict['row']
        elif from_sq_dict['row'] < 6 and to_sq_dict['row'] > 5:
            row_delta = to_sq_dict['row'] - from_sq_dict['row'] - 1
        elif from_sq_dict['row'] > 5 and to_sq_dict['row'] < 6:
            row_delta = to_sq_dict['row'] - from_sq_dict['row'] + 1
        #row_delta = to_sq_dict['row'] - from_sq_dict['row']
        column_delta = to_sq_dict['column'] - from_sq_dict['column']
        # If the specified move is not within the legal possible moves for the Horse return False
        if [row_delta, column_delta] not in possible_row_column_deltas:
            return False
        # Check that another piece is not located within the orthogonal path of movement of the Horse
        # If the specified move increases the row by 2, make sure there is not a piece blocking movement to the south
        if row_delta == 2:
            if type(board[from_sq_dict['row'] + 1][from_sq_dict['column']]) != str:
                return False
        # If the specified move decreases the row by 2, make sure there is not a piece blocking movement to the north
        elif row_delta == -2:
            if type(board[from_sq_dict['row'] - 1][from_sq_dict['column']]) != str:
                return False
        # If the specified move increases the column by 2, make sure there is not a piece blocking movement to the east
        elif column_delta == 2:
            if type(board[from_sq_dict['row']][from_sq_dict['column'] + 1]) != str:
                return False
        # If the specified move decreases the column by 2, make sure there is not a piece blocking movement to the west
        elif column_delta == -2:
            if type(board[from_sq_dict['row']][from_sq_dict['column'] - 1]) != str:
                return False
        return True

class Rook(Piece):
    """Represents a piece of type Rook."""

    def __init__(self, _color, _position):
        """Returns a piece of type Rook with the specified attributes."""
        super().__init__(_color, _position, _acronym='R', _piece_type='Rook')

    def verify_legal_move(self, from_sq_dict, to_sq_dict, board):
        """Takes three parameters that represent the square moved from, the square moved to, and the board. Rook's may
        move and capture any number of points orthogonally. Rook's may not jump over intervening pieces. If the move
        being made does not follow the rules for the Rook's movement and capture abilities the method will return False.
        """
        row_delta = to_sq_dict['row'] - from_sq_dict['row']
        column_delta = to_sq_dict['column'] - from_sq_dict['column']
        # If the piece is moving to the north or south, make sure it is not moving east or west
        if abs(row_delta) > 0 and abs(column_delta) > 0:
            return False
        # If the piece is moving to the south, check that no intervening pieces are in the path of movement
        if row_delta > 0:
            for x in range(from_sq_dict['row'] + 1, to_sq_dict['row']):
                if type(board[x][from_sq_dict['column']]) != str:
                    return False
        # If the piece is moving to the north, check that no intervening pieces are in the path of movement
        elif row_delta < 0:
            for x in range(to_sq_dict['row'], from_sq_dict['row']):
                if type(board[x][from_sq_dict['column']]) != str:
                    return False
        # If the piece is moving to the east, check that no intervening pieces are in the path of movement
        elif column_delta > 0:
            for y in range(from_sq_dict['column'] + 1, to_sq_dict['column']):
                if type(board[from_sq_dict['row']][y]) != str:
                    return False
        # If the piece is moving to the west, check that no intervening pieces are in the path of movement
        elif column_delta < 0:
            for y in range(to_sq_dict['column'], from_sq_dict['column']):
                if type(board[from_sq_dict['row']][y]) != str:
                    return False

class Cannon(Piece):
    """Represents a piece of type Cannon."""

    def __init__(self, _color, _position):
        """Returns a piece of type Cannon with the specified attributes."""
        super().__init__(_color, _position, _acronym='C', _piece_type='Cannon')

    def verify_legal_move(self, from_sq_dict, to_sq_dict, board):
        """Takes three parameters that represent the square moved from, the square moved to, and the board. Cannon's
        may move any number of points orthogonally. Cannon's may only capture by jumping a single piece (friend or foe)
        along the path of attack and land on the point containing the piece of capture. If the move being made does not
        follow the rules for the Cannon's movement and capture abilities the method will return False.
        """
        row_delta = to_sq_dict['row'] - from_sq_dict['row']
        column_delta = to_sq_dict['column'] - from_sq_dict['column']
        # If the piece is moving to the north or south, make sure it is not moving east or west
        if abs(row_delta) > 0 and abs(column_delta) > 0:
            return False
        # If the square being moved to contains a piece type, set check_capture_rules to True
        if type(board[to_sq_dict['row']][to_sq_dict['column']]) != str:
            check_capture_rules = True
        else:
            check_capture_rules = False
        # Determine which direction on the board the piece is moving
        if row_delta > 0:
            direction = 'south'
        elif row_delta < 0:
            direction = 'north'
        elif column_delta > 0:
            direction = 'east'
        elif column_delta < 0:
            direction = 'west'
        # If the square being moved to contains a piece type, verify that the piece is of the opposing color and
        # the piece next to the square along the path of movement contains a piece.
        if check_capture_rules is True:
            if self._color == board[to_sq_dict['row']][to_sq_dict['column']].get_color():
                return False
            # If the piece is moving to the south check that the square one point to the north contains a piece
            # and that the piece is not itself
            if direction == 'south':
                if type(board[to_sq_dict['row'] - 1][to_sq_dict['column']]) == str:
                    return False
                elif board[to_sq_dict['row'] - 1][to_sq_dict['column']] == self:
                    return False
            # If the piece is moving to the north check that the square one point to the south contains a piece
            # and that the piece is not itself
            elif direction == 'north':
                if type(board[to_sq_dict['row'] + 1][to_sq_dict['column']]) == str:
                    return False
                elif board[to_sq_dict['row'] + 1][to_sq_dict['column']] == self:
                    return False
            # If the piece is moving to the east check that the square one point to the west contains a piece
            # and that the piece is not itself
            elif direction == 'east':
                if type(board[to_sq_dict['row']][to_sq_dict['column'] - 1]) == str:
                    return False
                elif board[to_sq_dict['row']][to_sq_dict['column'] - 1] == self:
                    return False
            # If the piece is moving to the west check that the square one point to the west contains a piece
            # and that the piece is not itself
            elif direction == 'west':
                if type(board[to_sq_dict['row']][to_sq_dict['column'] - 1]) == str:
                    return False
                elif board[to_sq_dict['row']][to_sq_dict['column'] - 1] == self:
                    return False
        # If the piece is moving to the south, check that no intervening pieces are in the path of movement or capture
        if direction == 'south':
            if check_capture_rules is True:
                check_to_row = to_sq_dict['row'] - 1
            else:
                check_to_row = to_sq_dict['row']
            for x in range(from_sq_dict['row'] + 1, check_to_row):
                if type(board[x][from_sq_dict['column']]) != str:
                    return False
        # If the piece is moving to the north, check that no intervening pieces are in the path of movement
        elif direction == 'north':
            if check_capture_rules is True:
                check_to_row = to_sq_dict['row'] + 1
            else:
                check_to_row = to_sq_dict['row']
            for x in range(check_to_row, from_sq_dict['row']):
                if type(board[x][from_sq_dict['column']]) != str:
                    return False
        # If the piece is moving to the east, check that no intervening pieces are in the path of movement
        elif direction == 'east':
            if check_capture_rules is True:
                check_to_column = to_sq_dict['column'] - 1
            else:
                check_to_column = to_sq_dict['column']
            for y in range(from_sq_dict['column'] + 1, check_to_column):
                if type(board[from_sq_dict['row']][y]) != str:
                    return False
        # If the piece is moving to the west, check that no intervening pieces are in the path of movement
        elif direction == 'west':
            if check_capture_rules is True:
                check_to_column = to_sq_dict['column'] + 1
            else:
                check_to_column = to_sq_dict['column']
            for y in range(check_to_column, from_sq_dict['column']):
                if type(board[from_sq_dict['row']][y]) != str:
                    return False

class Soldier(Piece):
    """Represents a piece of type Soldier."""

    def __init__(self, _color, _position):
        """Returns a piece of type Soldier with the specified attributes."""
        super().__init__(_color, _position, _acronym='S', _piece_type='Soldier')
        self._crossed_river = False

    def set_crossed_river(self, state):
        """Sets crossed river variable to True if the Soldier has crossed the river."""
        self._crossed_river = state

    def verify_legal_move(self, from_sq_dict, to_sq_dict):
        """Takes two parameters that represent the square moved from and the square moved to. Soldier's may move and
        capture one point forward if they have not yet crossed the river. Once they have crossed the river, they
        may move and capture one point forward or horizontally.
        If the move being made does not follow the rules for the Soldier's movement and capture abilities the method
        will return False.
        """
        # Calculate row_delta. Adjust for moves that cross the river
        if to_sq_dict['row'] < 6 and from_sq_dict['row'] < 6:
            row_delta = to_sq_dict['row'] - from_sq_dict['row']
        elif to_sq_dict['row'] > 5 and from_sq_dict['row'] > 5:
            row_delta = to_sq_dict['row'] - from_sq_dict['row']
        elif from_sq_dict['row'] < 6 and to_sq_dict['row'] > 5:
            row_delta = to_sq_dict['row'] - from_sq_dict['row'] - 1
        elif from_sq_dict['row'] > 5 and to_sq_dict['row'] < 6:
            row_delta = to_sq_dict['row'] - from_sq_dict['row'] + 1
        if self.get_color() == 'RED':
            if self._crossed_river is False:
                #print("row_delta:", row_delta)
                # If the move is not one point to the south then it is an illegal move
                if row_delta != 1:
                    #print("row_delta:", row_delta)
                    return False
                # If the move changes the column and the Soldier has not crossed the river it is an illegal move
                if to_sq_dict['column'] - from_sq_dict['column'] != 0:
                    #print("step 2")
                    return False
            # If the Soldier has crossed the river, it may only move one point south or one point horizontally
            elif self._crossed_river is True:
                #print("row_delta:", row_delta)
                #print("column delta:", abs(to_sq_dict['column'] - from_sq_dict['column']))
                if row_delta == 1 and abs(to_sq_dict['column'] - from_sq_dict['column']) != 0:
                    #print("1 soldier has crossed the river and is not following the rules")
                    return False
                if row_delta == 0 and abs(to_sq_dict['column'] - from_sq_dict['column']) != 1:
                    #print("2 soldier has crossed the river and is not following the rules")
                    return False
                if row_delta < 0:
                    return False
        if self.get_color() == 'BLACK':
            if self._crossed_river is False:
                # If the move is not one point to the north then it is an illegal move
                #print("has not crossed river")
                if row_delta != -1:
                    return False
                # If the move changes the column and the soldier has not crossed the river it is an illegal move
                if to_sq_dict['column'] - from_sq_dict['column'] != 0:
                    return False
            # If the Soldier has crossed the river, it may only move one point north or one point horizontally
            elif self._crossed_river is True:
                #print("has crossed the river but is not following the rules")
                if row_delta == -1 and abs(to_sq_dict['column'] - from_sq_dict['column']) != 0:
                    return False
                if row_delta == 0 and abs(to_sq_dict['column'] - from_sq_dict['column']) != 1:
                    return False
                if row_delta > 0:
                    return False