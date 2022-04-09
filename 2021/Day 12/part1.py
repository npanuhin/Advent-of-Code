from collections import defaultdict


def traverse(cur_cave, visited):
    if cur_cave == "end":
        return 1

    answer = 0
    for next_cave in graph[cur_cave]:
        if 'a' <= next_cave[0] <= 'z' and visited[next_cave]:
            continue

        visited[next_cave] = True
        answer += traverse(next_cave, visited)
        visited[next_cave] = False

    return answer


graph = defaultdict(list)

with open("input.txt", 'r') as file:
    for line in file:
        cave1, cave2 = line.strip().split('-')
        graph[cave1].append(cave2)
        graph[cave2].append(cave1)

visited = {cave: False for cave in graph}
visited["start"] = True

print(traverse("start", visited))
