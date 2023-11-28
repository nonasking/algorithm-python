# 이웃한 칸(프로그래머스)
# https://school.programmers.co.kr/learn/courses/30/lessons/250125


def solution(board, h, w):
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    result = 0
    for i in range(4):
        if 0 <= h + dh[i] < len(board) and 0 <= w + dw[i] < len(board):
            if board[h + dh[i]][w + dw[i]] == board[h][w]:
                result += 1
    return result