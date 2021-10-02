import pyautogui as pag
import time
import copy

sudoku =    [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

time.sleep(2)

topleftx = 975
toplefty = 507
bottomrightx = 1307
bottomrighty = 846

boxwidth = (bottomrightx - topleftx)/8
boxheight = (bottomrighty - toplefty)/8


def findNextCellToFill(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                return x, y
    return -1, -1


def isValid(sudoku, i, j, e):
    rowOk = all([e != sudoku[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != sudoku[x][j] for x in range(9)])
        if columnOk:
            secTopX, secTopY = 3*(i//3), 3*(j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if sudoku[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(sudoku, i=0, j=0):
    global backtracks
    i, j = findNextCellToFill(sudoku)
    if i == -1:
        return True

    for e in range(1, 10):
        if isValid(sudoku, i, j, e):
            sudoku[i][j] = e
            if solveSudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False


def printsudoku():
    print("\n\n\n\n\n")
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j])+" "
        print(line)


def fillsudoku(nr, pos):
    global sudoku
    indexlocx = int((pos[0] - topleftx + boxwidth/2)//boxwidth)
    indexlocy = int((pos[1] - toplefty + boxheight/2)//boxwidth)
    sudoku[indexlocy][indexlocx] = nr


def fillcell(nr, x, y):
    xcoord = topleftx + boxwidth * x
    ycoord = toplefty + boxheight * y
    pag.click(xcoord, ycoord)
    pag.press(str(nr))


for i in range(1, 10):
    for pos in pag.locateAllOnScreen(str(i)+'.png'):
        fillsudoku(i, pos)

sudokucopy = copy.deepcopy(sudoku)
solveSudoku(sudoku)
