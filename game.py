from enum import Enum, auto
import pygame as pg
from pieces import Advisor, Canon, Chariot, Elephant, General, Horse, Pawn


class State(Enum):
    STARTMENU = auto()
    SHOWINGMOVES = auto()
    PICKINGPIECES = auto()
    PAUSE = auto()
    ENDSCREEN = auto()


class Game:
    def __init__(self):
        pg.init()
        SCREEN_WIDTH = 600
        SCREEN_HEIGHT = 650
        size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.size = size
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption('Chinese Chess')

        # STATE
        self.clock = pg.time.Clock()
        self.running = False
        self.state = State.STARTMENU

        # DRAW DATA
        self.bg = pg.transform.scale(
            pg.image.load('assets/chess_board.png'), size)
        self.buttonImg = pg.transform.scale(
            pg.image.load('assets/button.png'), (180, 60))

        # GAME DATA
        self.turn = 'red'
        self.clickedPiece = None
        self.piecesMoves = []
        self.clickedPos = None
        self.winner = 'red'

    def start(self):
        # Clear board - Setup
        self.board = [[None for j in range(9)] for i in range(10)]
        # Put pieces on board
        for i in range(0, 9, 2):
            self.board[3][i] = Pawn('red')

        self.board[0][0] = Chariot('red')
        self.board[0][1] = Horse('red')
        self.board[0][2] = Elephant('red')
        self.board[0][3] = Advisor('red')
        self.board[0][4] = General('red')
        self.board[0][5] = Advisor('red')
        self.board[0][6] = Elephant('red')
        self.board[0][7] = Horse('red')
        self.board[0][8] = Chariot('red')

        self.board[2][1] = Canon('red')
        self.board[2][7] = Canon('red')

        for i in range(0, 9, 2):
            self.board[6][i] = Pawn('black')

        self.board[9][0] = Chariot('black')
        self.board[9][1] = Horse('black')
        self.board[9][2] = Elephant('black')
        self.board[9][3] = Advisor('black')
        self.board[9][4] = General('black')
        self.board[9][5] = Advisor('black')
        self.board[9][6] = Elephant('black')
        self.board[9][7] = Horse('black')
        self.board[9][8] = Chariot('black')

        self.board[7][1] = Canon('black')
        self.board[7][7] = Canon('black')

    def main_run_loop(self):
        self.running = True
        while self.running:
            self.main_events_handler()
            self.main_draw()
            # DEBUG
            self.clock.tick(60)
        pg.quit()

    def main_draw(self):
        if self.state == State.STARTMENU:
            self.screen.blit(self.bg, (0, 0))
            overLay = pg.Surface(self.size, pg.SRCALPHA)
            overLay.fill((0, 0, 0, 200))
            self.screen.blit(overLay, (0, 0))
            # DRAW PAUSE
            font = pg.font.SysFont('Ariel', 80)
            text = font.render('CHING-CHONG', False, (255, 255, 255))
            self.screen.blit(text, (95, 250))
            text = font.render('CHESS', False, (255, 255, 255))
            self.screen.blit(text, (205, 325))
            # DRAW BUTTON
            self.screen.blit(self.buttonImg, (210, 400))
            font = pg.font.SysFont('Ariel', 50)
            text = font.render('START', False, (255, 255, 255))
            self.screen.blit(text, (245, 415))

            pg.display.update()
            return
        elif self.state == State.SHOWINGMOVES:
            self.screen.blit(self.bg, (0, 0))
            for i, row in enumerate(self.board):
                for j, piece in enumerate(row):
                    if piece != None:
                        self.screen.blit(
                            piece.img, (int(34 + 66*j-55/2), int(30+66*i-55/2)))
            for move in self.piecesMoves:
                pg.draw.circle(self.screen, (255, 0, 0),
                               (34 + 66*move[1], 30+66*move[0]), 15)
            pg.display.update()
            return
        elif self.state == State.PICKINGPIECES:
            self.screen.blit(self.bg, (0, 0))

            # DRAW TURN TEXT
            font = pg.font.SysFont('Ariel', 50)
            color = (255, 0, 0) if self.turn == 'red' else (0, 0, 0)
            text = font.render(f'{self.turn}'.upper(), False, color)
            pos = (265, 310) if self.turn == 'red' else (245, 310)
            self.screen.blit(text, pos)
            # DRAW PIECES
            for i, row in enumerate(self.board):
                for j, piece in enumerate(row):
                    if piece != None:
                        self.screen.blit(
                            piece.img, (int(34 + 66*j-55/2), int(30+66*i-55/2)))

            pg.display.update()
            return
        elif self.state == State.PAUSE:
            self.screen.blit(self.bg, (0, 0))
            overLay = pg.Surface(self.size, pg.SRCALPHA)
            overLay.fill((0, 0, 0, 200))
            self.screen.blit(overLay, (0, 0))
            # DRAW PAUSE
            font = pg.font.SysFont('Ariel', 80)
            text = font.render('PAUSED', False, (255, 255, 255))
            self.screen.blit(text, (185, 300))
            font = pg.font.SysFont('Ariel', 40)
            text = font.render('PRESS SPACE TO CONTINUE',
                               False, (255, 255, 255))
            self.screen.blit(text, (100, 520))

            # DRAW BUTTON
            self.screen.blit(self.buttonImg, (210, 400))
            font = pg.font.SysFont('Ariel', 50)
            text = font.render('MENU', False, (255, 255, 255))
            self.screen.blit(text, (250, 415))
            pg.display.update()
            return

        elif self.state == State.ENDSCREEN:
            self.screen.blit(self.bg, (0, 0))
            overLay = pg.Surface(self.size, pg.SRCALPHA)
            overLay.fill((0, 0, 0, 200))
            self.screen.blit(overLay, (0, 0))
            # DRAW WINNER
            font = pg.font.SysFont('Ariel', 80)
            if self.winner == 'red':
                text = font.render('!RED WIN!', False, (255, 0, 0))
                self.screen.blit(text, (160, 200))
            if self.winner == 'black':
                text = font.render('!BLACK WIN!', False, (255, 255, 255))
                self.screen.blit(text, (125, 200))
            # DRAW BUTTON
            self.screen.blit(self.buttonImg, (210, 400))
            font = pg.font.SysFont('Ariel', 50)
            text = font.render('MENU', False, (255, 255, 255))
            self.screen.blit(text, (250, 415))
            pg.display.update()
            return

    def game_logic_handler(self, chosen_move):
        if self.state == State.SHOWINGMOVES:
            if chosen_move in self.piecesMoves:
                self.movePiece(
                    self.board, self.clickedPiece, chosen_move, self.clickedPos)
                self.turn = 'red' if self.turn == 'black' else 'black'
                self.state = State.PICKINGPIECES
                if self.checkingVerifier(self.board, self.turn):
                    print(f'{self.turn.capitalize()} is being checked')
                if self.checkMateVerifier(self.board, self.turn):
                    print(
                        f'{self.opponent(self.turn).capitalize()} checkmate {self.turn.capitalize()}')
                    self.winner = self.opponent(self.turn)
                    self.state = State.ENDSCREEN
            else:
                self.state = State.PICKINGPIECES
            return
        elif self.state == State.PICKINGPIECES:
            pos_on_board = chosen_move
            if self.board[pos_on_board[0]][pos_on_board[1]] != None:
                if self.board[pos_on_board[0]][pos_on_board[1]].side == self.turn:
                    self.clickedPiece = self.board[pos_on_board[0]
                                                   ][pos_on_board[1]]
                    self.clickedPos = pos_on_board
                    self.piecesMoves = self.clickedPiece.returnMoves(
                        self.board, self.clickedPos)
                    self.state = State.SHOWINGMOVES
            return

    def main_events_handler(self):
        for event in pg.event.get():
            # CLICK ON CLOSE
            if event.type == pg.QUIT:
                self.running = False
                return

            # CLICK
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                # print('Mouse position:', mouse_pos)
                if self.state == State.STARTMENU:
                    if mouse_pos[0] > 210 and mouse_pos[0] < 390 and mouse_pos[1] > 400 and mouse_pos[1] < 460:
                        self.start()
                        self.state = State.PICKINGPIECES
                    return
                elif self.state == State.SHOWINGMOVES:
                    chosen_move = self.pixelPosToBoardPos(mouse_pos)
                    self.game_logic_handler(chosen_move)
                    return
                elif self.state == State.PICKINGPIECES:
                    pos_on_board = self.pixelPosToBoardPos(mouse_pos)
                    self.game_logic_handler(pos_on_board)
                    return
                elif self.state == State.PAUSE:
                    # Click on Menu Button
                    if mouse_pos[0] > 210 and mouse_pos[0] < 390 and mouse_pos[1] > 400 and mouse_pos[1] < 460:
                        self.state = State.STARTMENU
                    return
                elif self.state == State.ENDSCREEN:
                    if mouse_pos[0] > 210 and mouse_pos[0] < 390 and mouse_pos[1] > 400 and mouse_pos[1] < 460:
                        self.state = State.STARTMENU
                    return

            # KEY PRESSED

            if event.type == pg.KEYDOWN:
                key_pressed = event.key
                if self.state == State.STARTMENU:
                    return
                elif self.state == State.SHOWINGMOVES:
                    if key_pressed == pg.K_SPACE or key_pressed == pg.K_ESCAPE:
                        self.state = State.PAUSE
                    return
                elif self.state == State.PICKINGPIECES:
                    if key_pressed == pg.K_SPACE or key_pressed == pg.K_ESCAPE:
                        self.state = State.PAUSE
                    return
                elif self.state == State.PAUSE:
                    if key_pressed == pg.K_SPACE or key_pressed == pg.K_ESCAPE:
                        self.state = State.PICKINGPIECES
                    return
                elif self.state == State.ENDSCREEN:
                    return

    # Helper function

    def movePiece(self, board, pieceToMove, move_pos, piece_pos):
        pieceToMove.moveCount += 1
        board[piece_pos[0]][piece_pos[1]] = None
        board[move_pos[0]][move_pos[1]] = pieceToMove

    def pixelPosToBoardPos(self, mouse_pos):
        return [int((mouse_pos[1]+55/2-32)/66), int((mouse_pos[0]+55/2-30)/66)]

    def checkingVerifier(self, board, current_turn):
        # Cheeck if 'black' being checkmate or not
        # Current turn = 'black'
        op = 'red' if current_turn == 'black' else 'black'
        yourGeneralPos = None
        for i in range(len(board)):
            for j in range(len(board[0])):
                piece = board[i][j]
                if isinstance(piece, General):
                    if piece.side == current_turn:
                        yourGeneralPos = [i, j]
                        break

        for i in range(len(board)):
            for j in range(len(board[0])):
                piece = board[i][j]
                if piece != None:
                    if piece.side == op:
                        if yourGeneralPos in piece.returnMoves(board, [i, j]):
                            return True
        return False

    def checkMateVerifier(self, board, current_turn):
        for i in range(len(board)):
            for j in range(len(board[0])):
                piece = board[i][j]
                if piece != None:
                    if piece.side == current_turn:
                        moves = piece.returnMoves(board, [i, j])
                        for move in moves:
                            testBoard = [[piece for piece in row]
                                         for row in board]
                            self.movePiece(testBoard, piece, move, [i, j])
                            if not self.checkingVerifier(testBoard, current_turn):
                                return False
        return True

    def opponent(self, you):
        return 'red' if you == 'black' else 'red'


game = Game()
game.main_run_loop()
