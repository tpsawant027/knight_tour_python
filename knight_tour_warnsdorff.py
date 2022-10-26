from collections import deque


def get_mat(n):
    return [[-1 for _ in range(n)] for _ in range(n)]

def get_moves(i, j, n):
    mvs_pos = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    mvs = []
    for di, dj in mvs_pos:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < n:
            mvs.append((ni, nj))
    return mvs

def next_moves(mvs, arr):
    fmvs = [get_moves(i, j, len(arr)) for i, j in mvs]
    mvq = deque()
    min_len = 9
    for i, mv in enumerate(fmvs):
        nmv = list(filter(lambda x: arr[x[0]][x[1]] == -1, mv))
        if len(nmv) <= min_len:
            min_len = len(nmv)
            mvq.appendleft(mvs[i])
        else:
            mvq.append(mvs[i])
    return mvq
    
def ktour(arr, i, j, n):
    if n == len(arr)**2 + 1:
        return True
    mvs = get_moves(i, j, len(arr))
    mvs = next_moves(mvs, arr)
    for di, dj in mvs:
        if arr[di][dj] == -1:
            arr[di][dj] = n
            if ktour(arr, di, dj, n+1):
                return True
            arr[di][dj] = -1
    return False        

def start_ktour(arr):
    arr[0][0] = 1
    if ktour(arr, 0, 0, 2):
        return True
    return False


if __name__ == '__main__':
  m = get_mat(8)
  start_ktour(m)
  print(m)
