#!/usr/bin/python3
"""
challenge of placing N non-attacking queens on an N×N chessboard
"""
import sys


def retrack(r, n, cols, pos, neg, board):
    """
    challenge of placing N non-attacking queens on an N×N chessboard
    """
    if r == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for x in range(n):
        if x in cols or (r + x) in pos or (r - x) in neg:
            continue

        cols.add(x)
        pos.add(r + x)
        neg.add(r - x)
        board[r][x] = 1

        retrack(r+1, n, cols, pos, neg, board)

        cols.remove(x)
        pos.remove(r + x)
        neg.remove(r - x)
        board[r][x] = 0


def nqueens(n):
    """
    challenge of placing N non-attacking queens on an N×N chessboard
    Return:
        lists representing coordinates of each
        queen for all possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    retrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)