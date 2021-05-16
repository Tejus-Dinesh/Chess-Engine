from typing import Dict


class GameState():
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteMove = True
        self.moveLog = []

    def MovePiece(self, move):
        if move.pieceMoved != '--':
            self.board[move.startRow][move.startCol] = '--'
            self.board[move.endRow][move.endCol] = move.pieceMoved
            self.moveLog.append(move)
            self.whiteMove = not self.whiteMove


class Moves():
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRank = {v: k for k, v in ranksToRows.items()}
    colToFiles = {0: "a", 1: "b", 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
    filesToCol = {v: k for k, v in colToFiles.items()}

    def __init__(self, start, end, board):
        self.startRow = start[0]
        self.startCol = start[1]
        self.endRow = end[0]
        self.endCol = end[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCap = board[self.endRow][self.endCol]

    def Notation(self):
        symbol = {"wp": '', "bp": '', "bR": "R", 'wR': "R", "wN": "N", "bN": "N", "wB": "B", "bB": "B", 'wQ': "Q",
                  'bQ': "Q", "wK": "K", "bK": "K"}
        if self.pieceMoved != '--':
            if self.pieceCap == '--':
                return symbol[self.pieceMoved] + self.rankFile(self.endRow, self.endCol)
            elif (self.pieceMoved == 'wp' or self.pieceCap == 'bp') and self.pieceCap != '--':
                return self.colToFiles[self.startCol] + "x" + self.rankFile(self.endRow, self.endCol)
            else:
                return symbol[self.pieceMoved] + "x" + self.rankFile(self.endRow, self.endCol)

    def rankFile(self, r, c):
        return self.colToFiles[c] + self.rowsToRank[r]
