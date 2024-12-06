def can_win_game(board):
    farthest = 0
    for i in range(len(board)):
        if i > farthest:
            return False
        farthest = max(farthest, i + board[i])
    return farthest >= len(board) - 1