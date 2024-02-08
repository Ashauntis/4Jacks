import pygame
from scene import Scene
import random


class GameBoard(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.key_color = (123, 231, 132)  # some random garbage color
        self.board = pygame.Surface((400, 280)).convert()
        self.board.set_colorkey(self.key_color)
        self.board.fill((33, 33, 255))
        self.colors = ["RED", "YELLOW"]
        self.current_turn = 0

        rows, cols = (6, 7)
        self.board_map = [[0 for i in range(cols)] for j in range(rows)]
        self.board_score = [[0 for i in range(cols)] for j in range(rows)]

        self.selected_column = 0

        print(self.board_map)

    def update_player_turn(self):

        # move the selected column
        if pygame.K_LEFT in self.game.just_pressed:
            self.selected_column -= 1
        if pygame.K_RIGHT in self.game.just_pressed:
            self.selected_column += 1

        # drop a piece
        if pygame.K_SPACE in self.game.just_pressed:
            col = self.selected_column
            row = 5
            searching = True

            while searching:
                if self.board_map[row][col] != 0:
                    row -= 1
                    if row < 0:
                        searching = False
                else:

                    self.board_map[row][col] = self.colors[self.current_turn]
                    self.board_score = self.score_board(self.board_map)
                    self.current_turn += 1
                    searching = False

        # pop a piece
        if pygame.K_RETURN in self.game.just_pressed:
            col = self.selected_column
            row = 5

            if self.board_map[row][col] == self.colors[self.current_turn]:
                while row > 0:
                    self.board_map[row][col] = self.board_map[row - 1][col]
                    row -= 1
                self.board_map[0][col] = 0
                self.board_score = self.score_board(self.board_map)

                self.current_turn += 1

    def get_move_list(self, board, color):
        # create a possible list of 14 moves available
        # first 7 are drops and the second 7 are pops
        move_list = []

        for col in range(7):
            # check the top of each column to see if a piece can be dropped
            if board[0][col] == 0:
                move_list.append("d" + str(col))

            # check if we can pop a piece by checking the bottom of each column
            # to see if the bottom piece matches the color provided
            if board[5][col] == color:
                move_list.append("p" + str(col))

        return move_list


    def update_ai_turn(self):

        # generate the list of possible moves this turn
        move_list = self.get_move_list(self.board_map, self.colors[self.current_turn])

        # chose a random element from the move list
        move = random.choice(move_list)

        # if the move is a drop
        if move[0] == "d":
            col = int(move[1])
            row = 5
            searching = True

            while searching:
                if self.board_map[row][col] != 0:
                    row -= 1
                    if row < 0:
                        searching = False
                else:
                    self.board_map[row][col] = self.colors[self.current_turn]
                    searching = False

        # if the move is a pop
        if move[0] == "p":
            col = int(move[1])
            row = 5

            while row > 0:
                self.board_map[row][col] = self.board_map[row - 1][col]
                row -= 1
            self.board_map[0][col] = 0

        self.board_score = self.score_board(self.board_map)
        self.current_turn += 1

                

    def update(self):

        self.check_winner()
        if self.game.winner is not None:
            self.game.scene_push = "GameOver"


        if self.game.ai == self.current_turn:
            self.update_ai_turn()
        else:
            self.update_player_turn()

        # modulo are turn and column so they wrap around
        self.selected_column = self.selected_column % 7
        self.current_turn = self.current_turn % 2

    def check_winner(self):
        player_1 = [0]
        player_2 = [0]

        # add up all game winning scores
        for row in range(6):
            for col in range(7):
                if self.board_score[row][col] >= 4:
                    if self.board_map[row][col] == self.colors[0]:
                        player_1.append(self.board_score[row][col])
                    else:
                        player_2.append(self.board_score[row][col])

        # sort player in descending order
        player_1.sort(reverse=True)
        player_2.sort(reverse=True)

        # did anyone have enough points to win?
        if player_1[0] >= 4 or player_2[0] >= 4:
            # if so, who won?

            # was there a tie?
            if player_1[0] == player_2[0]:
                self.game.winner = "T I E ! !"

            # did player 1 win?
            if player_1[0] > player_2[0]:
                self.game.winner = "Player 1 Wins!"

            # did player 2 win?
            if player_1[0] < player_2[0]:
                self.game.winner = "Player 2 Wins!"

    def score_board(self, board):
        rows, cols = (6, 7)
        scores = [[0 for i in range(cols)] for j in range(rows)]
        for row in range(6):
            for col in range(7):
                if board[row][col] == 0:
                    scores[row][col] = 0
                else:
                    scores[row][col] = self.score_position(row, col, board)

        return scores

    def score_position(self, row, col, board):
        score = 0

        score = max(self.score_horizontal(row, col, board), score)
        score = max(self.score_vertical(row, col, board), score)
        score = max(self.score_diagonal1(row, col, board), score)
        score = max(self.score_diagonal2(row, col, board), score)

        return score

    def score_diagonal1(self, row, col, board):
        # starting top left and going to bottom right
        score = 1

        base_color = board[row][col]
        streak_plus = True
        streak_minus = True

        for n in range(1, 7):
            if row + n < 6 and col + n < 7 and streak_plus:
                if board[row + n][col + n] == base_color:
                    score += 1
                else:
                    streak_plus = False

            if row - n >= 0 and col - n >= 0 and streak_minus:
                if board[row - n][col - n] == base_color:
                    score += 1
                else:
                    streak_minus = False

        return score

    def score_diagonal2(self, row, col, board):
        # starting top right and going to bottom left
        score = 1

        base_color = board[row][col]
        streak_plus = True
        streak_minus = True

        for n in range(1, 7):
            if row + n < 6 and col - n >= 0 and streak_plus:
                if board[row + n][col - n] == base_color:
                    score += 1
                else:
                    streak_plus = False

            if row - n >= 0 and col + n < 7 and streak_minus:
                if board[row - n][col + n] == base_color:
                    score += 1
                else:
                    streak_minus = False

        return score

    def score_horizontal(self, row, col, board):
        score = 1

        base_color = board[row][col]
        streak_plus = True
        streak_minus = True

        for c in range(1, 7):
            if col + c < 7 and streak_plus:
                if board[row][col + c] == base_color:
                    score += 1
                else:
                    streak_plus = False

            if col - c >= 0 and streak_minus:
                if board[row][col - c] == base_color:
                    score += 1
                else:
                    streak_minus = False

        return score

    def score_vertical(self, row, col, board):
        score = 1
        streak_plus = True
        streak_minus = True
        base_color = board[row][col]

        for r in range(1, 6):
            if row + r < 6 and streak_plus:
                if board[row + r][col] == base_color:
                    score += 1
                else:
                    streak_plus = False

            if row - r >= 0 and streak_minus:
                if board[row - r][col] == base_color:
                    score += 1
                else:
                    streak_minus = False

        return score

    def draw(self):
        self.game.screen.fill((80, 80, 80))

        # draw the game board
        self.board.fill((33, 33, 255))
        for row in range(6):
            for col in range(7):
                if self.board_map[row][col] != 0:
                    pygame.draw.circle(
                        self.board,
                        self.board_map[row][col],
                        (50 * col + 50, 40 * row + 40),
                        18,
                    )
                else:
                    pygame.draw.circle(
                        self.board, self.key_color, (50 * col + 50, 40 * row + 40), 18
                    )

        # draw the scores over each piece (for debugging)
        for row in range(6):
            for col in range(7):
                if self.board_score[row][col] != 0:
                    # make text of the score
                    text = self.game.make_text(
                        str(self.board_score[row][col]), (255, 255, 255), 16
                    )

                    # overlay the score onto the board
                    self.board.blit(text, (50 * col + 40, 40 * row + 35))

        # overlay the game board onto the screen
        self.game.blit_centered(self.board, self.game.screen, (0.5, 0.56))

        # draw a piece hovering over the selected column
        pygame.draw.circle(
            self.game.screen,
            self.colors[self.current_turn],
            (50 * self.selected_column + 170, 32),
            18,
        )
