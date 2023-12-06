import pygame
from dokusan import generators
import numpy as np
from copy import deepcopy
'''here I use dokusan library, which can generate random sudoku table'''
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Sudoku")
dif = 500 / 9
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

'''end_game is a function which creates a window of the end of the game'''
def end_game(flag):
    color = (255, 255, 255)
    if flag == 1:
        '''if you won the game'''
        text1 = font1.render('YOU WON!!!', True, color)
        text2 = font1.render('RESTART', True, color)
        text3 = font1.render('QUIT', True, color)
        run = True
        while run:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 175 <= mouse[0] <= 375 and 250 <= mouse[1] <= 300:
                        level()
                    if 175 <= mouse[0] <= 375 and 350 <= mouse[1] <= 400:
                        pygame.quit()
                        run = False
            screen.fill((60, 25, 60))
            '''higlight the necessary button'''
            if 175 <= mouse[0] <= 375 and 250 <= mouse[1] <= 300:
                pygame.draw.rect(screen, (170, 170, 170), [175, 250, 200, 50])
                pygame.draw.rect(screen, (100, 100, 100), [175, 350, 200, 50])
            elif 175 <= mouse[0] <= 375 and 350 <= mouse[1] <= 400:
                pygame.draw.rect(screen, (100, 100, 100), [175, 250, 200, 50])
                pygame.draw.rect(screen, (170, 170, 170), [175, 350, 200, 50])
            else:
                pygame.draw.rect(screen, (100, 100, 100), [175, 250, 200, 50])
                pygame.draw.rect(screen, (100, 100, 100), [175, 350, 200, 50])
            '''write a text of the button'''
            screen.blit(text1, (175, 100))
            screen.blit(text2, (175, 250))
            screen.blit(text3, (175, 350))
            pygame.display.update()
    else:
        '''if you lost the game'''
        text1 = font1.render('YOU LOSE', True, color)
        text2 = font1.render('RESTART', True, color)
        text3 = font1.render('QUIT', True, color)
        run = True
        while run:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 175 <= mouse[0] <= 375 and 250 <= mouse[1] <= 320:
                        level()
                    if 175 <= mouse[0] <= 375 and 350 <= mouse[1] <= 420:
                        pygame.quit()
                        run = False
            screen.fill((60, 25, 60))
            if 175 <= mouse[0] <= 375 and 250 <= mouse[1] <= 300:
                pygame.draw.rect(screen, (170, 170, 170), [175, 250, 200, 50])
                pygame.draw.rect(screen, (100, 100, 100), [175, 350, 200, 50])
            elif 175 <= mouse[0] <= 375 and 350 <= mouse[1] <= 400:
                pygame.draw.rect(screen, (100, 100, 100), [175, 250, 200, 50])
                pygame.draw.rect(screen, (170, 170, 170), [175, 350, 200, 50])
            else:
                pygame.draw.rect(screen, (100, 100, 100), [175, 250, 200, 50])
                pygame.draw.rect(screen, (100, 100, 100), [175, 350, 200, 50])
            screen.blit(text1, (175, 100))
            screen.blit(text2, (175, 250))
            screen.blit(text3, (175, 350))
            pygame.display.update()


def play(avg):
    '''solve is a function which solves a sudoku grid with backtracking algorithm'''
    def solve(grid, row, col, num):
        for x in range(9):
            if grid[row][x] == num:
                return False
        for x in range(9):
            if grid[x][col] == num:
                return False
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False
        return True

    '''def Sudoku generates solved grid'''
    def Sudoku(grid, row, col):
        if (row == 8 and col == 9):
            return True
        if col == 9:
            row += 1
            col = 0
        if grid[row][col] > 0:
            return Sudoku(grid, row, col + 1)
        for num in range(1, 10, 1):
            if solve(grid, row, col, num):
                grid[row][col] = num
                if Sudoku(grid, row, col + 1):
                    return True
            grid[row][col] = 0
        return False

    '''def iszero checks if sudoku is already solved'''
    def iszero():
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return False
        return True

    k = 0
    arr = np.array(list(str(generators.random_sudoku(avg_rank=avg))))  #generators.random_sudoku generates the table with difficulty - avg_rank = avg
    grid = []
    for i in range(9):
        t = []
        for j in range(9):
            t.append(int(arr[k]))
            k += 1
        grid.append(t)
    solved_grid = deepcopy(grid)
    pygame.font.init()
    Sudoku(solved_grid, 0, 0)
    dif = 500/9 #dif is average value of the cell

    '''def get_cord gives coordinates of chosen cell'''
    def get_cord(pos):
        global x
        x = pos[0] // dif
        global y
        y = pos[1] // dif

    '''def draw_box highlights selected cell'''
    def draw_box():
        for i in range(2):
            pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
            pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)

    '''def draw draws our table'''
    def draw():
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    pygame.draw.rect(screen, (0, 150, 150), (
                    i * dif, j * dif, dif + 1, dif + 1))  #makes a cell blue-colored if value is already in it
                    text1 = font1.render(str(grid[i][j]), True, (0, 0, 0))
                    screen.blit(text1, (i * dif + 15, j * dif))
        for i in range(10):
            if i % 3 == 0:
                thick = 7
            else:
                thick = 1
            pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
            pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

    '''writes a value in cell'''
    def draw_val(val):
        text1 = font1.render(str(val), False, (0, 0, 0))
        screen.blit(text1, (x * dif + 15, y * dif))

    '''raise_error1 shows the error if value is incorrect'''
    def raise_error1():
        screen.fill((255, 255, 255))
        text1 = font1.render("WRONG VALUE !!!", False, (255, 0, 0))
        screen.blit(text1, (100, 250))
        pygame.display.update()
        pygame.time.delay(1000)

    '''raise_error2 shows error if the input data is not valid, i.e. spacebar was pressed'''
    def raise_error2():
        screen.fill((255, 255, 255))
        text1 = font1.render("INVALID DATA!", True, (255, 0, 0))
        screen.blit(text1, (100, 250))
        pygame.display.update()
        pygame.time.delay(1000)

    '''valid checks input for correctness'''
    def valid(val, i, j):
        if solved_grid[i][j] == val:
            return True
        return False

    run = True
    flag1 = 0
    errors = 0
    val = 0
    while run:
        screen.fill((255, 255, 255))
        t = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                flag1 = 1
                pos = pygame.mouse.get_pos()
                get_cord(pos)
            if event.type == pygame.KEYDOWN:
                t += 1
                if event.key == pygame.K_1:
                    val = 1
                if event.key == pygame.K_2:
                    val = 2
                if event.key == pygame.K_3:
                    val = 3
                if event.key == pygame.K_4:
                    val = 4
                if event.key == pygame.K_5:
                    val = 5
                if event.key == pygame.K_6:
                    val = 6
                if event.key == pygame.K_7:
                    val = 7
                if event.key == pygame.K_8:
                    val = 8
                if event.key == pygame.K_9:
                    val = 9
        if val != 0:
            if valid(val, int(x), int(y)) == True and grid[int(x)][int(y)] == 0:
                draw_val(val)
                grid[int(x)][int(y)] = val
                flag1 = 0
            elif not valid(val, int(x), int(y)) and grid[int(x)][int(y)] == 0:
                raise_error1()
                errors += 1
            val = 0
            t = 0
        elif val == 0 and t > 0:
            raise_error2()
            t = 0
        draw()
        if flag1 == 1:
            draw_box()
        if errors >= 3:  #condition for end of the game
            end_game(0)
        elif iszero():  #condition if sudoku is solved
            end_game(1)
        text = font1.render(f'MISTAKES {errors} / 3', True, (0, 0, 0))
        screen.blit(text, (50, 510))
        pygame.display.update()

def level():
    '''a menu of levels'''
    color = (255, 255, 255)
    text1 = font1.render('EASY', True, color)
    text2 = font1.render('MEDIUM', True, color)
    text3 = font1.render('HARD', True, color)
    run = True
    while run:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 175 <= mouse[0] <= 375 and 50 <= mouse[1] <= 100:
                    play(100)
                if 175 <= mouse[0] <= 375 and 150 <= mouse[1] <= 200:
                    play(150)
                if 175 <= mouse[0] <= 375 and 250 <= mouse[1] <= 300:
                    play(200)
        screen.fill((60, 25, 60))
        if 175 <= mouse[0] <= 375 and 50 <= mouse[1] <= 100:
            pygame.draw.rect(screen, (170, 170, 170), [175, 50, 200, 50])
            pygame.draw.rect(screen, (100, 100, 100), [175, 150, 200, 50])
            pygame.draw.rect(screen, (100, 100, 100), [175, 250, 200, 50])
        elif 175 <= mouse[0] <= 375 and 150 <= mouse[1] <= 200:
            pygame.draw.rect(screen, (100, 100, 100), [175, 50, 200, 50])
            pygame.draw.rect(screen, (170, 170, 170), [175, 150, 200, 50])
            pygame.draw.rect(screen, (100, 100, 100), [175, 250, 200, 50])
        elif 175 <= mouse[0] <= 375 and 250 <= mouse[1] <= 300:
            pygame.draw.rect(screen, (100, 100, 100), [175, 50, 200, 50])
            pygame.draw.rect(screen, (100, 100, 100), [175, 150, 200, 50])
            pygame.draw.rect(screen, (170, 170, 170), [175, 250, 200, 50])
        else:
            pygame.draw.rect(screen, (100, 100, 100), [175, 50, 200, 50])
            pygame.draw.rect(screen, (100, 100, 100), [175, 150, 200, 50])
            pygame.draw.rect(screen, (100, 100, 100), [175, 250, 200, 50])
        screen.blit(text1, (175, 50))
        screen.blit(text2, (175, 150))
        screen.blit(text3, (175, 250))
        pygame.display.update()

def menu():
    '''main menu'''
    color = (255, 255, 255)
    text1 = font1.render('QUIT', True, color)
    text2 = font1.render('START', True, color)
    run = True
    while run:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 175 <= mouse[0] <= 325 and 200 <= mouse[1] <= 250:
                    pygame.quit()
                    run = False
                if 175 <= mouse[0] <= 325 and 50 <= mouse[1] <= 100:
                    level()
        screen.fill((60, 25, 60))
        if 175 <= mouse[0] <= 325 and 200 <= mouse[1] <= 250:
            pygame.draw.rect(screen, (170, 170, 170), [175, 200, 150, 50])
            pygame.draw.rect(screen, (100, 100, 100), [175, 50, 150, 50])
        elif 175 <= mouse[0] <= 325 and 50 <= mouse[1] <= 100:
            pygame.draw.rect(screen, (100, 100, 100), [175, 200, 150, 50])
            pygame.draw.rect(screen, (170, 170, 170), [175, 50, 150, 50])
        else:
            pygame.draw.rect(screen, (100, 100, 100), [175, 50, 150, 50])
            pygame.draw.rect(screen, (100, 100, 100), [175, 200, 150, 50])
        screen.blit(text1, (175, 200))
        screen.blit(text2, (175, 50))
        pygame.display.update()
menu()
pygame.quit()
