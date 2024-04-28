from heapq import *

MAP = {'a' : [(2, 'm'), (3, 'p'), (1, 'j'), (4, 'hospital')],
       'm' : [(2, 'a'), (2, 'n'), (7, 'hospital')],
       'b' : [(4, 'p'), (2, 'n'), (5, 'firestation')],
       'n' : [(2, 'm'), (2, 'b'), (6, 'firestation')],
       'p' : [(3, 'a'), (4, 'b'), (3, 'j'), (7, 'policestation')],
       'j' : [(1, 'a'), (3, 'p'), (15, 'policestation')],
       'hospital' : [(4, 'a'), (7, 'm')],
       'firestation' : [(5, 'b'), (6, 'n')],
       'policestation' : [(7, 'p'), (15, 'j')]}


def dijkstra(start, end, MAP=MAP):
    queue = []
    heappush(queue, (0, start))
    cost_visited = {start: 0}
    visited = {start: None}
    
    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == end:
            break
        
        next_nodes = MAP[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost
            
            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                heappush(queue, (new_cost, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node
                
    return visited

start = 'policestation'
goal =  'a'

visited = dijkstra(start=start, end=goal, MAP=MAP)
cur_node = goal
        
print(f'\nShortest Path from {goal} to {start}: \n {goal} ', end='')
while cur_node !=  start:
    cur_node = visited[cur_node]
    print(f'---> {cur_node} ', end='')