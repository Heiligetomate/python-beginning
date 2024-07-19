import pygame
import sys


class TicTacToeView:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_size = 1000
        self.field_dimension = self.screen_size / 3
        self.offset = self.field_dimension / 2
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        self.line_color = (255, 255, 255)
        self.round_count = 0
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.win_sets = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def draw_x(self, center):
        pygame.draw.line(self.screen, self.line_color, (center[0] - self.screen_size / 6, center[1] - self.offset),
                         (center[0] + self.offset, center[1] + self.offset))
        pygame.draw.line(self.screen, self.line_color, (center[0] - self.offset, center[1] + self.offset),
                         (center[0] + self.offset, center[1] - self.offset))

    def draw_o(self, center):
        pygame.draw.circle(self.screen, self.line_color, center, self.offset, width=1)

    def draw_lines(self):
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.line_color, (self.field_dimension * i, 0),
                             (self.field_dimension * i, self.screen_size))
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.line_color, (0, self.field_dimension * i),
                             (self.screen_size, self.field_dimension * i))

    def reset_board(self):
        self.round_count = 0
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.screen.fill((0, 0, 0))
        self.draw_lines()

    def check_for_win(self):
        for j in range(len(self.win_sets)):
            if (self.board[self.win_sets[j][0]] == "X"
                    and self.board[self.win_sets[j][1]] == "X"
                    and self.board[self.win_sets[j][2]] == "X"):
                print("Team X wins")
                sys.exit()
            elif (self.board[self.win_sets[j][0]] == "O"
                  and self.board[self.win_sets[j][1]] == "O"
                  and self.board[self.win_sets[j][2]] == "O"):
                print("Team O wins")
                sys.exit()

    # self.screen.fill((255, 0, 100))

    def run(self):
        self.draw_lines()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos_y = pygame.mouse.get_pos()[1]
                    mouse_pos_x = pygame.mouse.get_pos()[0]
                    res_x = mouse_pos_x - (mouse_pos_x % self.field_dimension) + self.offset
                    res_y = mouse_pos_y - (mouse_pos_y % self.field_dimension) + self.offset
                    x_index = int(res_x / self.screen_size * 3)
                    y_index = int(res_y / self.screen_size * 3)
                    total_index = x_index + y_index * 3
                    if self.board[total_index] == " ":
                        if self.round_count % 2 == 1:
                            self.draw_x((res_x, res_y))
                            self.board[total_index] = "X"
                        else:
                            self.draw_o((res_x, res_y))
                            self.board[total_index] = "O"
                        self.round_count += 1

            self.check_for_win()
            if self.round_count == 9:
                self.reset_board()
            pygame.display.update()
            self.clock.tick(100)
