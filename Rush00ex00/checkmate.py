def checkmate(board_string):
    board = [list(row) for row in board_string.splitlines()]
    n = len(board)
    if n == 0 or any(len(row) != n for row in board):
        return 

    king_pos = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        return  

    ki, kj = king_pos

    linear_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dx, dy in linear_dirs:
        x, y = ki + dx, kj + dy
        while 0 <= x < n and 0 <= y < n:
            cell = board[x][y]
            if cell != '.':
                if cell in ('R', 'Q'):
                    print("Success")
                    return
                break
            x += dx
            y += dy

    for dx, dy in diag_dirs:
        x, y = ki + dx, kj + dy
        while 0 <= x < n and 0 <= y < n:
            cell = board[x][y]
            if cell != '.':
                if cell in ('B', 'Q'):
                    print("Success")
                    return
                break
            x += dx
            y += dy

    for dx, dy in [(-1, -1), (-1, 1)]:
        x, y = ki + dx, kj + dy
        if 0 <= x < n and 0 <= y < n and board[x][y] == 'P':
            print("Success")
            return

    print("Fail")
