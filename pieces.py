import pygame as pg


class Piece:
    def __init__(self, side):
        self.side = side
        self.moveCount = 0

    def set_img(self, name):
        self.img = pg.transform.scale(pg.image.load(
            f'assets/{self.side}/{name.lower()}_{self.side}.png'), (55, 55))
    # CELL WIDTH - 55
    # CELL HEIGHT- 67


class Advisor(Piece):
    def __init__(self,  side):
        super().__init__(side)
        self.set_img(type(self).__name__)

    def returnMoves(self, board, current_pos):
        allMoves = [[current_pos[0]+1, current_pos[1]+1], [current_pos[0]-1, current_pos[1]-1],
                    [current_pos[0]+1, current_pos[1]-1], [current_pos[0]-1, current_pos[1]+1]]
        moves = []
        if self.side == 'red':
            for move in allMoves:
                if not (move[0] < 0 or move[0] > 2 or move[1] < 3 or move[1] > 5):
                    if board[move[0]][move[1]] == None:
                        moves.append(move)
                    elif board[move[0]][move[1]].side != self.side:
                        moves.append(move)
        elif self.side == 'black':
            for move in allMoves:
                if not (move[0] < 7 or move[0] > 9 or move[1] < 3 or move[1] > 5):
                    if board[move[0]][move[1]] == None:
                        moves.append(move)
                    elif board[move[0]][move[1]].side != self.side:
                        moves.append(move)
        return moves


class Canon(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.set_img(type(self).__name__)

    def returnMoves(self, board, current_pos):
        moves = []

        # UP
        r = current_pos[0]
        c = current_pos[1]
        while True:
            r = r - 1
            if r < 0:
                break
            if board[r][c] == None:
                moves.append([r, c])
            else:
                while True:
                    r = r - 1
                    if r < 0:
                        break
                    if board[r][c] != None:
                        if board[r][c].side != self.side:
                            moves.append([r, c])
                        break

                break
        # DOWN
        r = current_pos[0]
        c = current_pos[1]
        while True:
            r = r + 1
            if r > 9:
                break
            if board[r][c] == None:
                moves.append([r, c])
            else:
                while True:
                    r = r + 1
                    if r > 9:
                        break
                    if board[r][c] != None:
                        if board[r][c].side != self.side:
                            moves.append([r, c])
                        break

                break

        # RIGHT
        r = current_pos[0]
        c = current_pos[1]
        while True:
            c = c + 1
            if c > 8:
                break
            if board[r][c] == None:
                moves.append([r, c])
            else:
                while True:
                    c = c + 1
                    if c > 8:
                        break
                    if board[r][c] != None:
                        if board[r][c].side != self.side:
                            moves.append([r, c])
                        break

                break

        # LEFT
        r = current_pos[0]
        c = current_pos[1]
        while True:
            c = c - 1
            if c < 0:
                break
            if board[r][c] == None:
                moves.append([r, c])
            else:
                while True:
                    c = c - 1
                    if c < 0:
                        break
                    if board[r][c] != None:
                        if board[r][c].side != self.side:
                            moves.append([r, c])
                        break

                break

        return moves


class Chariot(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.set_img(type(self).__name__)

    def returnMoves(self, board,  current_pos):
        moves = []
        # UP
        r = current_pos[0]
        c = current_pos[1]
        while True:
            r = r - 1
            if r < 0:
                break
            if board[r][c] == None:
                moves.append([r, c])
            else:
                if board[r][c].side != self.side:
                    moves.append([r, c])
                break

        # DOWN
        r = current_pos[0]
        c = current_pos[1]
        while True:
            r = r + 1
            if r > 9:
                break
            if board[r][c] == None:
                moves.append([r, c])
            else:
                if board[r][c].side != self.side:
                    moves.append([r, c])
                break

        # RIGHT
        r = current_pos[0]
        c = current_pos[1]
        while True:
            c = c + 1
            if c > 8:
                break
            if board[r][c] == None:
                moves.append([r, c])
            else:
                if board[r][c].side != self.side:
                    moves.append([r, c])
                break

        # LEFT
        r = current_pos[0]
        c = current_pos[1]
        while True:
            c = c - 1
            if c < 0:
                break
            if board[r][c] == None:
                moves.append([r, c])
            else:
                if board[r][c].side != self.side:
                    moves.append([r, c])
                break

        return moves


class Elephant(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.set_img(type(self).__name__)

    def returnMoves(self, board,  current_pos):
        allMoves = [[current_pos[0]+2, current_pos[1]+2], [current_pos[0]-2, current_pos[1]-2],
                    [current_pos[0]+2, current_pos[1]-2], [current_pos[0]-2, current_pos[1]+2]]
        l = []
        if self.side == 'red':
            for move in allMoves:
                if not (move[0] > 4 or move[0] < 0 or move[1] < 0 or move[1] > 8):
                    if board[move[0]][move[1]] == None:
                        l.append(move)
                    elif board[move[0]][move[1]].side != self.side:
                        l.append(move)
        elif self.side == 'black':
            for move in allMoves:
                if not (move[0] < 5 or move[0] > 9 or move[1] < 0 or move[1] > 8):
                    if board[move[0]][move[1]] == None:
                        l.append(move)
                    elif board[move[0]][move[1]].side != self.side:
                        l.append(move)
        moves = []
        for move in l:

            centerPos = [(current_pos[0]+move[0])//2,
                         (current_pos[1]+move[1])//2]
            if board[centerPos[0]][centerPos[1]] == None:
                moves.append(move)
        return moves


class General(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.set_img(type(self).__name__)

    def returnMoves(self, board,  current_pos):
        allMoves = [[current_pos[0]+1, current_pos[1]], [current_pos[0]-1, current_pos[1]],
                    [current_pos[0], current_pos[1]-1], [current_pos[0], current_pos[1]+1]]
        moves = []
        if self.side == 'red':
            for move in allMoves:
                if not (move[0] < 0 or move[0] > 2 or move[1] < 3 or move[1] > 5):
                    if board[move[0]][move[1]] == None:
                        moves.append(move)
                    elif board[move[0]][move[1]].side != self.side:
                        moves.append(move)
        elif self.side == 'black':
            for move in allMoves:
                if not (move[0] < 7 or move[0] > 9 or move[1] < 3 or move[1] > 5):
                    if board[move[0]][move[1]] == None:
                        moves.append(move)
                    elif board[move[0]][move[1]].side != self.side:
                        moves.append(move)
        return moves


class Horse(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.set_img(type(self).__name__)

    def returnMoves(self, board,  current_pos):
        moves = []
        front, back = ([current_pos[0]+1, current_pos[1]],
                       [current_pos[0]-1, current_pos[1]])
        right, left = ([current_pos[0], current_pos[1]-1],
                       [current_pos[0], current_pos[1]+1])

        if front[0] + 1 <= 9:
            if board[front[0]][front[1]] == None:
                if front[1] - 1 >= 0:
                    if board[front[0]+1][front[1]-1] == None:
                        moves.append([front[0]+1, front[1]-1])
                    elif board[front[0]+1][front[1]-1].side != self.side:
                        moves.append([front[0]+1, front[1]-1])

                if front[1] + 1 <= 8:
                    if board[front[0]+1][front[1]+1] == None:
                        moves.append([front[0]+1, front[1]+1])
                    elif board[front[0]+1][front[1]+1].side != self.side:
                        moves.append([front[0]+1, front[1]+1])

        if back[0] - 1 >= 0:
            if board[back[0]][back[1]] == None:
                if back[1] - 1 >= 0:
                    if board[back[0]-1][back[1]-1] == None:
                        moves.append([back[0]-1, back[1]-1])
                    elif board[back[0]-1][back[1]-1].side != self.side:
                        moves.append([back[0]-1, back[1]-1])

                if back[1] + 1 <= 8:
                    if board[back[0]-1][back[1]+1] == None:
                        moves.append([back[0]-1, back[1]+1])
                    elif board[back[0]-1][back[1]+1].side != self.side:
                        moves.append([back[0]-1, back[1]+1])

        if right[1] - 1 >= 0:
            if board[right[0]][right[1]] == None:
                if right[0] - 1 >= 0:
                    if board[right[0]-1][right[1]-1] == None:
                        moves.append([right[0]-1, right[1]-1])
                    elif board[right[0]-1][right[1]-1].side != self.side:
                        moves.append([right[0]-1, right[1]-1])

                if right[0] + 1 <= 9:
                    if board[right[0]+1][right[1]-1] == None:
                        moves.append([right[0]+1, right[1]-1])
                    elif board[right[0]+1][right[1]-1].side != self.side:
                        moves.append([right[0]+1, right[1]-1])

        if left[1] + 1 <= 8:
            if board[left[0]][left[1]] == None:
                if left[0] - 1 >= 0:
                    if board[left[0]-1][left[1]+1] == None:
                        moves.append([left[0]-1, left[1]+1])
                    elif board[left[0]-1][left[1]+1].side != self.side:
                        moves.append([left[0]-1, left[1]+1])

                if left[0] + 1 <= 9:
                    if board[left[0]+1][left[1]+1] == None:
                        moves.append([left[0]+1, left[1]+1])
                    elif board[left[0]+1][left[1]+1].side != self.side:
                        moves.append([left[0]+1, left[1]+1])

        return moves


class Pawn(Piece):
    def __init__(self,  side):
        super().__init__(side)
        self.set_img(type(self).__name__)

    def returnMoves(self, board,  current_pos):
        moves = []
        front = [current_pos[0] + 1 if self.side ==
                 'red' else current_pos[0] - 1, current_pos[1]]
        left, right = ([current_pos[0], current_pos[1]-1],
                       [current_pos[0], current_pos[1]+1])
        if not (front[0] < 0 or front[0] > 9):
            if board[front[0]][front[1]] == None:
                moves.append(front)
            elif board[front[0]][front[1]].side != self.side:
                moves.append(front)

        if self.moveCount >= 2:
            if not (left[1] < 0 or left[1] > 8):
                if board[left[0]][left[1]] == None:
                    moves.append(left)
                elif board[left[0]][left[1]].side != self.side:
                    moves.append(left)
            if not (right[1] < 0 or right[1] > 8):
                if board[right[0]][right[1]] == None:
                    moves.append(right)
                elif board[right[0]][right[1]].side != self.side:
                    moves.append(right)

        return moves
