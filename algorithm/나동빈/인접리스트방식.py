
graph =  [
  [], [2,3,8], [1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]
]

from collections import deque

def bfs(graph, start, visited):


  queue = deque([start])
  while queue:
    v = queue.popleft()
    for e in graph[v]:
      if not visited[e]:
        visited[e] = True
        queue.append(e)
        print(visited[e])
visited = [False] * 9
bfs(graph, 1, visited)
a = deque([2])
b = a.pop()
print(b)








# def bfs(graph, start, visited):
#   queue = deque([start])
  
#   while queue:
#     v = queue.popleft()
#     for i in graph[v]:
#       if not visited[i]:
#         queue.append(i)
#         visited[i] = True
#     print(v)
#   print(visited)

# visited = [False]*9
# bfs(graph, 1, visited)


  # queue = deque([start])
  # visited[start] = True
  # while queue:
  #   v = queue.popleft()
  #   print(v, end = ' ')
  #   for i in graph[v]:
  #     if not visited[i]:
  #       queue.append(i)
  #       visited[i] = True