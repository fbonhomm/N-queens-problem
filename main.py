# @Author: fbonhomm
# @Date:   Saturday, March-11-2017, 18:45:19
# @Email:  flo-github@outlook.fr
# @Filename: main.py
# @Last modified by:   flo
# @Last modified time: Sunday, March-12-2017, 22:28:01

import setting as s

nbSolution = 0


def getRow(chess, row):
    """
        getRow(chess, row)
        - chess = matrice chess
        - row = row
    """
    for col in range(0, len(chess)):
        if chess[row][col]:
            return False
    return True


def getColumns(chess, col):
    """
        getColumns(chess, col)
        - chess = matrice chess
        - col = columns
    """
    for row in range(0, len(chess)):
        if chess[row][col]:
            return False
    return True


def getDiagonal(chess, row, col):
    """
        getDiagonal(chess, row, col)
        - chess = matrice chess
        - col = columns
        - row = row
    """
    tmpX = row
    tmpY = col
    while tmpX and tmpY:
        tmpX -= 1
        tmpY -= 1
        if chess[tmpX][tmpY]:
            return False

    tmpX = row
    tmpY = col
    while tmpX < len(chess) - 1 and tmpY:
        tmpX += 1
        tmpY -= 1
        if chess[tmpX][tmpY]:
            return False
    return True


def backtrakSolve(chess, col):
    """
        backtrakSolve(chess, col)
        - chess = matrice chess
        - col = numbers of columns
        function recursif
    """

    if (col >= len(chess)):
        global nbSolution
        for i in range(0, len(chess)):
            tmp = ''
            for j in range(0, len(chess)):
                if j == 0:
                    tmp += '|Q|' if chess[i][j] else '|.|'
                else:
                    tmp += 'Q|' if chess[i][j] else '.|'
            print(tmp)
        print('')
        nbSolution += 1
        return

    for row in range(0, len(chess)):
        if (getDiagonal(chess, row, col) and getColumns(chess, col) and getRow(chess, row)):
            chess[row][col] = 1
            backtrakSolve(chess, col + 1)
            chess[row][col] = 0


def main():
    """
        main()
        main define
    """

    # initialize matrice in setiing all element at 0
    chess = [[0 for j in range(0, s.nbQueen)] for i in range(0, s.nbQueen)]
    # call function recursif
    backtrakSolve(chess, 0)
    # print numbers of solutions
    print ('Found solutions: ', nbSolution)


if __name__ == '__main__':
    main()
