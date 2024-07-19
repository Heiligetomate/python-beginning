import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen_size = 1000
field_dimension = screen_size / 3
offset = field_dimension / 2
screen = pygame.display.set_mode((screen_size, screen_size))
line_color = (255, 255, 255)
round_count = 0
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
win_sets = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def draw_x(center):
    pygame.draw.line(screen, line_color, (center[0] - screen_size / 6, center[1] - offset), (center[0] + offset, center[1] + offset))
    pygame.draw.line(screen, line_color, (center[0] - offset, center[1] + offset), (center[0] + offset, center[1] - offset))


def draw_o(center):
    pygame.draw.circle(screen, line_color, center, field_dimension / 2, width=1)


def draw_lines():
    for i in range(1, 3):
        pygame.draw.line(screen, line_color, (field_dimension * i, 0), (field_dimension * i, screen_size))
    for i in range(1, 3):
        pygame.draw.line(screen, line_color, (0, field_dimension * i), (screen_size, field_dimension * i))


def reset_board():
    global board
    global round_count
    round_count = 0
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    screen.fill((0, 0, 0))
    draw_lines()


def check_for_win():
    for j in range(len(win_sets)):
        if board[win_sets[j][0]] == "X" and board[win_sets[j][1]] == "X" and board[win_sets[j][2]] == "X":
            print("Team X wins")
            sys.exit()
        elif board[win_sets[j][0]] == "O" and board[win_sets[j][1]] == "O" and board[win_sets[j][2]] == "O":
            print("Team O wins")
            sys.exit()


# screen.fill((255, 0, 100))
draw_lines()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos_y = pygame.mouse.get_pos()[1]
            mouse_pos_x = pygame.mouse.get_pos()[0]
            res_x = mouse_pos_x - (mouse_pos_x % field_dimension) + offset
            res_y = mouse_pos_y - (mouse_pos_y % field_dimension) + offset
            x_index = int(res_x / screen_size * 3)
            y_index = int(res_y / screen_size * 3)
            total_index = x_index + y_index * 3
            if board[total_index] == " ":
                if round_count % 2 == 1:
                    draw_x((res_x, res_y))
                    board[total_index] = "X"
                else:
                    draw_o((res_x, res_y))
                    board[total_index] = "O"
                round_count += 1

    check_for_win()
    if round_count == 9:
        reset_board()
    pygame.display.update()
    clock.tick(100)
