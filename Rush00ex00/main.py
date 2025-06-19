import sys

def read_board(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        if len(lines) != 4 or any(len(row) != 4 for row in lines):
            return None
        return lines
    except:
        return None

def find_king(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 'K':
                return i, j
    return None

def is_rook_attacking(board, kx, ky):
    for y in range(4):
        if y != ky:
            if board[kx][y] == 'R':
                between = board[kx][min(y, ky)+1:max(y, ky)]
                if all(cell == '.' for cell in between):
                    return True
    for x in range(4):
        if x != kx:
            if board[x][ky] == 'R':
                between = [board[i][ky] for i in range(min(x, kx)+1, max(x, kx))]
                if all(cell == '.' for cell in between):
                    return True
    return False

def is_pawn_attacking(board, kx, ky):
    if kx + 1 < 4:
        if ky - 1 >= 0 and board[kx + 1][ky - 1] == 'P':
            return True
        if ky + 1 < 4 and board[kx + 1][ky + 1] == 'P':
            return True
    return False

def validate_and_check(file_path):
    board = read_board(file_path)
    if not board:
        return "Error"
    king_pos = find_king(board)
    if not king_pos:
        return "Error"
    kx, ky = king_pos
    if is_rook_attacking(board, kx, ky) or is_pawn_attacking(board, kx, ky):
        return "Error"
    return "Success"

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(validate_and_check(arg))
