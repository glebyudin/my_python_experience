import pygame
import random
pygame.init()
def draw_grid(scr):
    pygame.draw.line(scr, (0, 0, 0), (100, 0), (100, 300))
    pygame.draw.line(scr, (0, 0, 0), (200, 0), (200, 300))
    pygame.draw.line(scr, (0, 0, 0), (0, 100), (300, 100))
    pygame.draw.line(scr, (0, 0, 0), (0, 200), (300, 200))

def draw_tictactoe(scr, items):
    for i in range(3):
        for j in range(3):
            if items[i][j] == "o":
                pygame.draw.circle(scr, (255, 0, 0), (j * 100 + 50, i * 100 + 50), 45)
            elif items[i][j] == "x":
                pygame.draw.line(scr, (0, 0, 255), (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 3)
                pygame.draw.line(scr, (0, 0, 255), (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 3)
def get_win_check(fd, symbol):
    flag_win = False
    for line in fd:
        if line.count(symbol) ==3:
            flag_win = True
    for i in range(3):
        if fd[1][i] == fd[0][i] == fd[2][i] == symbol:
            flag_win = True
    if fd[0][0] == fd[1][1] == fd[2][2] == symbol:
        flag_win = True
    if fd[0][2] == fd[1][1] == fd[2][0] == symbol:
        flag_win = True
    return flag_win
screen_size = (300, 300)
window = pygame.display.set_mode(screen_size)
screen = pygame.Surface(screen_size)
pygame.display.set_caption('TicTacToe')
screen.fill((255, 255, 255))
field = [["","",""],
        ["","",""],
        ["","",""]]
mainloop = True
game_over = False
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            if field[pos[1] // 100][pos[0] // 100] == "":
                field[pos[1] // 100][pos[0] // 100] = "x"
                x, y = random.randint(0, 2), random.randint(0, 2)
                while field[x][y] != "":
                    x, y = random.randint(0, 2), random.randint(0, 2)
                field[x][y] = "o"

            player_win= get_win_check(field, "x")
            ai_win = get_win_check(field, "o")
            if player_win or ai_win:
                game_over = True
                if player_win:
                    pygame.display.set_caption("You WIN!")
                else:
                    pygame.display.set_caption("PC WIN!")
            elif field[0].count("x") + field[0].count("o") + field[1].count("x") + \
                    field[1].count("o") + field[2].count("x") + field[2].count("o") == 8:
                    game_over = True
                    pygame.display.set_caption("together WIN")

    draw_tictactoe(screen, field)
    draw_grid(screen)
    window.blit(screen, (0, 0))
    pygame.display.update()

