def can_win_game(board):
    farthest = 0
    for i in range(len(board)):
        if i > farthest:
            return False
        farthest = max(farthest, i + board[i])
    return farthest >= len(board) - 1


def can_reach_end(A):
    farthest = 0  # Tracks the furthest point we can reach
    n = len(A)  # Number of elements in the array

    for i in range(n):
        if i > farthest:  # If we can't reach this index
            return False
        farthest = max(farthest, i + A[i])  # Update the farthest reachable point
        if farthest >= n - 1:  # If we can reach or surpass the last index
            return True

    return False  # If we finish the loop without reaching the end


def can_reach_end2(A):
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0

    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1

    return furthest_reach_so_far >= last_index
