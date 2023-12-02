from collections import defaultdict


def traverse(cur_cave, visited, small_twice):
    if cur_cave == "end":
        return 1

    answer = 0
    for next_cave in graph[cur_cave]:
        new_small_twice = small_twice

        if 'a' <= next_cave[0] <= 'z' and visited[next_cave] > 0:
            if small_twice or next_cave == "start" or next_cave == "end":
                continue
            new_small_twice = True

        visited[next_cave] += 1
        answer += traverse(next_cave, visited, new_small_twice)
        visited[next_cave] -= 1

    return answer


graph = defaultdict(list)

with open("input.txt") as file:
    for line in file:
        cave1, cave2 = line.strip().split('-')
        graph[cave1].append(cave2)
        graph[cave2].append(cave1)

visited = {cave: 0 for cave in graph}
visited["start"] = 1

print(traverse("start", visited, False))
