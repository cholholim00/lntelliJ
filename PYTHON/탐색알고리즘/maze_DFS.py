# 미로 정의 (1은 길, 0은 벽)
maze = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1]
]

# 미로 크기
n = len(maze)
m = len(maze[0])

# 방문 여부를 저장하는 배열
visited = [[False] * m for _ in range(n)]

# 상, 하, 좌, 우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS 함수 정의
def dfs(x, y):
     # 함수 진입 시 출력
    print(f"DFS 진입: ({x}, {y})")
    
    # 도착지점에 도달하면 True 반환
    if x == n - 1 and y == m - 1:
        print(f"도착지점에 도달했습니다! ({x}, {y})")
        return True

    # 현재 위치 방문 처리
    visited[x][y] = True

    # 상, 하, 좌, 우로 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 이동 가능한지 확인 (경계 조건, 벽 여부, 방문 여부)
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and not visited[nx][ny]:
            if dfs(nx, ny):  # 재귀 호출
                return True
    print(f"DFS 종료: ({x}, {y}) - 더 이상 진행할 수 없습니다.")  # 막힌 경우 출력
    return False  # 모든 방향 탐색 후에도 도착하지 못한 경우

# 시작점이 막혀있는지 확인
if maze[0][0] == 0:
    print("출발지부터 막혀있습니다.")
else:
    # DFS 탐색 시작
    if dfs(0, 0):
        print("도착지점에 도달했습니다!")
    else:
        print("도착지점에 도달할 수 없습니다.")