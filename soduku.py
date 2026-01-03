import pygame
import random
import sys
import time

# =============================
# PYGAME SETUP
# =============================
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 700  # Increased height for better layout
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sudoku")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 26)
big_font = pygame.font.SysFont("arial", 48)
btn_font = pygame.font.SysFont("arial", 28)

# =============================
# COLORS
# =============================
BG_BLACK = (20, 20, 30)  # Slightly off-black for better contrast
GRID_WHITE = (255, 255, 255)
FIXED_GRAY = (180, 180, 180)
PLAYER_WHITE = (255, 255, 255)
SELECT_GREEN = (0, 255, 170)
ERROR_RED = (255, 80, 80)
OVERLAY_BLACK = (0, 0, 0, 180)

# =============================
# GRID CONSTANTS
# =============================
N = 9
CELL_SIZE = 50
GRID_SIZE = N * CELL_SIZE
BOX_SIZE = 3 * CELL_SIZE
UI_TOP_MARGIN = 80
OFFSET = UI_TOP_MARGIN

# =============================
# GAME STATE
# =============================
selected = None
error_cell = None
error_time = 0
error_count = 0

game_started = False
game_paused = False
start_time = None
paused_at = None
paused_duration = 0

won = False

# Precompute button rects (no drawing in event loop)
play_rect = pygame.Rect(WINDOW_WIDTH // 2 - 100,
                        OFFSET + GRID_SIZE + 20, 200, 50)
pause_rect = pygame.Rect(WINDOW_WIDTH - 120, 20, 100, 40)

# =============================
# SUDOKU LOGIC
# =============================


def isValid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(N)]:
        return False
    br, bc = (row // 3) * 3, (col // 3) * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if board[i][j] == num:
                return False
    return True


def find_empty(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return i, j
    return None


def generate_full_board():
    board = [[0] * N for _ in range(N)]

    def fill(pos):
        if pos == N * N:
            return True
        r, c = divmod(pos, N)
        nums = list(range(1, 10))
        random.shuffle(nums)
        for n in nums:
            if isValid(board, r, c, n):
                board[r][c] = n
                if fill(pos + 1):
                    return True
                board[r][c] = 0
        return False
    fill(0)
    return board


def count_solutions(board):
    temp = [row[:] for row in board]
    count = [0]

    def solve():
        empty = find_empty(temp)
        if not empty:
            count[0] += 1
            return
        r, c = empty
        for n in range(1, 10):
            if isValid(temp, r, c, n):
                temp[r][c] = n
                solve()
                temp[r][c] = 0
                if count[0] > 1:
                    return
    solve()
    return count[0]


def generate_puzzle(remove_count=50):
    full = generate_full_board()
    puzzle = [row[:] for row in full]
    cells = [(i, j) for i in range(N) for j in range(N)]
    random.shuffle(cells)

    removed = 0
    for r, c in cells:
        if removed >= remove_count:
            break

        temp_val = puzzle[r][c]
        puzzle[r][c] = 0  # Try removing it

        if count_solutions(puzzle) != 1:
            puzzle[r][c] = temp_val  # Put it back if it ruins uniqueness
        else:
            removed += 1

    return puzzle


def is_solved(board):
    return all(cell != 0 for row in board for cell in row)

# =============================
# DRAWING
# =============================


def draw_grid():
    # Thin lines for cells
    for i in range(0, GRID_SIZE + 1, CELL_SIZE):
        pygame.draw.line(screen, GRID_WHITE, (OFFSET + i, OFFSET),
                         (OFFSET + i, OFFSET + GRID_SIZE), 1)
        pygame.draw.line(screen, GRID_WHITE, (OFFSET, OFFSET + i),
                         (OFFSET + GRID_SIZE, OFFSET + i), 1)
    # Thick lines for boxes
    for i in range(0, GRID_SIZE + 1, BOX_SIZE):
        pygame.draw.line(screen, GRID_WHITE, (OFFSET + i, OFFSET),
                         (OFFSET + i, OFFSET + GRID_SIZE), 3)
        pygame.draw.line(screen, GRID_WHITE, (OFFSET, OFFSET + i),
                         (OFFSET + GRID_SIZE, OFFSET + i), 3)


def draw_numbers(board):
    for r in range(N):
        for c in range(N):
            if board[r][c] != 0:
                color = FIXED_GRAY if (r, c) in originals else PLAYER_WHITE
                text = font.render(str(board[r][c]), True, color)
                screen.blit(text, (OFFSET + c * CELL_SIZE +
                            16, OFFSET + r * CELL_SIZE + 10))


def draw_selection():
    if selected:
        r, c = selected
        pygame.draw.rect(screen, SELECT_GREEN,
                         (OFFSET + c * CELL_SIZE, OFFSET + r * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)


def draw_error_highlight():
    if error_cell:
        r, c = error_cell
        pygame.draw.rect(screen, ERROR_RED,
                         (OFFSET + c * CELL_SIZE, OFFSET + r * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)


def draw_timer():
    if not game_started:
        text = font.render("00:00", True, GRID_WHITE)
    else:
        now = time.time()
        elapsed = int(now - start_time - paused_duration)
        m, s = divmod(max(elapsed, 0), 60)
        text = font.render(f"{m:02}:{s:02}", True, GRID_WHITE)
    screen.blit(text, (20, 20))


def draw_errors():
    text = font.render(f"Errors: {error_count}", True, ERROR_RED)
    screen.blit(text, (20, 50))


def draw_play_button():
    pygame.draw.rect(screen, SELECT_GREEN, play_rect, border_radius=8)
    label = btn_font.render("PLAY", True, BG_BLACK)
    screen.blit(label, (play_rect.centerx - label.get_width() //
                2, play_rect.centery - label.get_height() // 2))


def draw_pause_button():
    label_text = "PAUSE" if not game_paused else "RESUME"
    pygame.draw.rect(screen, SELECT_GREEN, pause_rect, border_radius=6)
    label = btn_font.render(label_text, True, BG_BLACK)
    screen.blit(label, (pause_rect.centerx - label.get_width() //
                2, pause_rect.centery - label.get_height() // 2))


def draw_pause_overlay():
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
    overlay.fill(OVERLAY_BLACK)
    screen.blit(overlay, (0, 0))
    txt = big_font.render("PAUSED", True, GRID_WHITE)
    screen.blit(txt, (WINDOW_WIDTH // 2 - txt.get_width() //
                2, WINDOW_HEIGHT // 2 - 50))


def draw_win_overlay():
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
    overlay.fill(OVERLAY_BLACK)
    screen.blit(overlay, (0, 0))
    txt = big_font.render("YOU WON!", True, GRID_WHITE)
    screen.blit(txt, (WINDOW_WIDTH // 2 - txt.get_width() //
                2, WINDOW_HEIGHT // 2 - 50))
    # Final time
    now = time.time()
    elapsed = int(now - start_time - paused_duration)
    m, s = divmod(elapsed, 60)
    time_text = font.render(f"Time: {m:02}:{s:02}", True, GRID_WHITE)
    screen.blit(time_text, (WINDOW_WIDTH // 2 -
                time_text.get_width() // 2, WINDOW_HEIGHT // 2 + 50))


# =============================
# GAME SETUP
# =============================
board = generate_puzzle(40)
originals = {(r, c) for r in range(N) for c in range(N) if board[r][c] != 0}

# =============================
# MAIN LOOP
# =============================
running = True
while running:
    # Handle error flash timeout
    if error_time and time.time() - error_time > 0.5:
        error_cell = None
        error_time = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            if not game_started:
                if play_rect.collidepoint(mx, my):
                    game_started = True
                    start_time = time.time()
            else:
                if pause_rect.collidepoint(mx, my):
                    if not game_paused and not won:
                        game_paused = True
                        paused_at = time.time()
                    elif game_paused:
                        game_paused = False
                        paused_duration += time.time() - paused_at
                # Grid selection
                elif not game_paused and not won:
                    grid_x = mx - OFFSET
                    grid_y = my - OFFSET
                    if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
                        c = grid_x // CELL_SIZE
                        r = grid_y // CELL_SIZE
                        if 0 <= r < N and 0 <= c < N and board[r][c] == 0:
                            selected = (r, c)

        if event.type == pygame.KEYDOWN and game_started and not game_paused and not won and selected:
            r, c = selected
            if '1' <= event.unicode <= '9':
                n = int(event.unicode)
                if board[r][c] == 0 and isValid(board, r, c, n):
                    board[r][c] = n
                    if is_solved(board):
                        won = True
                else:
                    error_cell = (r, c)
                    error_time = time.time()
                    error_count += 1

    # Render
    screen.fill(BG_BLACK)
    draw_grid()
    draw_numbers(board)
    draw_timer()
    draw_errors()
    draw_selection()

    if error_cell and time.time() - error_time < 0.5:
        draw_error_highlight()

    if not game_started:
        draw_play_button()
    else:
        draw_pause_button()

    if game_paused:
        draw_pause_overlay()
    if won:
        draw_win_overlay()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
