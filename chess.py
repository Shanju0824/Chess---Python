import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (245, 245, 220)
BLACK = (139, 69, 19)
BLUE = (50, 50, 255)

# Load piece images
PIECES = {}
PIECE_NAMES = ['wp', 'wr', 'wn', 'wb', 'wq', 'wk',
               'bp', 'br', 'bn', 'bb', 'bq', 'bk']
for name in PIECE_NAMES:
    PIECES[name] = pygame.transform.scale(
        pygame.image.load(f"https://upload.wikimedia.org/wikipedia/commons/{{
            'wp': '4/45/Chess_plt45.svg',
            'wr': '7/72/Chess_rlt45.svg',
            'wn': '7/70/Chess_nlt45.svg',
            'wb': 'b/b1/Chess_blt45.svg',
            'wq': '1/15/Chess_qlt45.svg',
            'wk': '4/42/Chess_klt45.svg',
            'bp': 'c/c7/Chess_pdt45.svg',
            'br': 'f/ff/Chess_rdt45.svg',
            'bn': 'e/ef/Chess_ndt45.svg',
            'bb': '9/98/Chess_bdt45.svg',
            'bq': '4/47/Chess_qdt45.svg',
            'bk': 'f/f0/Chess_kdt45.svg'
        }[name]}"), (SQUARE_SIZE, SQUARE_SIZE)
    )

# Create window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Starting board layout
board = [
    ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
    ['bp'] * 8,
    [''] * 8,
    [''] * 8,
    [''] * 8,
    [''] * 8,
    ['wp'] * 8,
    ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']
]

selected = None

def draw_board():
    win.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            color = BLACK if (row + col) % 2 else WHITE
            pygame.draw.rect(win, color, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece:
                win.blit(PIECES[piece], (col*SQUARE_SIZE, row*SQUARE_SIZE))

def get_square(pos):
    x, y = pos
    return y // SQUARE_SIZE, x // SQUARE_SIZE

def main():
    global selected
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        draw_board()
        draw_pieces()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_square(pygame.mouse.get_pos())

                if selected:
                    # Move piece
                    sel_row, sel_col = selected
                    board[row][col] = board[sel_row][sel_col]
                    board[sel_row][sel_col] = ''
                    selected = None
                elif board[row][col] != '':
                    # Select a piece
                    selected = (row, col)

    pygame.quit()
    sys.exit()

main()
