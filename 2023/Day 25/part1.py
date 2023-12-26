from collections import defaultdict, deque


with open('input.txt') as file:
    graph = defaultdict(list)
    for line in filter(None, map(str.strip, file)):
        source, destinations = line.split(':')
        for destination in destinations.split():
            graph[destination].append(source)
            graph[source].append(destination)

edge_visits = defaultdict(int)
for start in graph:
    visited = set([start])
    queue = deque([(start, [])])

    while queue:
        cur, path = queue.popleft()

        for edge in path:
            edge_visits[edge] += 1

        for neighbor in graph[cur]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [(min(cur, neighbor), max(cur, neighbor))]))

for node1, node2 in sorted(edge_visits, key=edge_visits.get)[-3:]:
    graph[node1].remove(node2)
    graph[node2].remove(node1)

visited = set([start])
queue = [start]
while queue:
    curr = queue.pop()
    for nxt in graph[curr]:
        if nxt not in visited:
            visited.add(nxt)
            queue.append(nxt)

print(len(visited) * (len(graph) - len(visited)))
