def count_changes(board, start_row, start_col, pattern):
    changes = 0
    for i in range(8):
        for j in range(8):
            if board[start_row + i][start_col + j] != pattern[i][j]:
                changes += 1
    return changes

def min_changes_to_chessboard(board):
    pattern1 = [
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
    ]

    pattern2 = [
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"
    ]
    
    n = len(board)
    m = len(board[0])
    min_changes = float('inf')

    for i in range(n - 7):
        for j in range(m - 7):
            changes1 = count_changes(board, i, j, pattern1)
            changes2 = count_changes(board, i, j, pattern2)
            min_changes = min(min_changes, changes1, changes2)
    
    return min_changes

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

print(min_changes_to_chessboard(board))