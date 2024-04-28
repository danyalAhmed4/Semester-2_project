from report import Report
from heapq import *

MAP = {'a' : [(2, 'm'), (3, 'p'), (1, 'j')],
       'm' : [(2, 'a'), (2, 'n')],
       'b' : [(4, 'p'), (2, 'n'), (5, 'station')],
       'n' : [(2, 'm'), (2, 'b')],
       'p' : [(3, 'a'), (4, 'b'), (3, 'j')],
       'j' : [(1, 'a'), (3, 'p'), (15, 'station')],
       'station' : [(15, 'j'), (5, 'b')]}

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
            
class station:
    def __init__(self) -> None:
        self.file_path = "report.txt"
                
    def file_report(self, REPORT: Report):
        
        x = REPORT.location
        
        lines = ['-------------------------------------\n',
                 f'{REPORT.timestamp} \n',
                 f'Reporter Name     : {REPORT.Name} \n',
                 f'Reporter Cnic     : {REPORT.Cnic} \n',
                 f'Reporter Contact  : {REPORT.contact}\n',
                 f'Emergency Location: {REPORT.location} \n',
                 f'Emergency Type    : {REPORT.type} \n',
                 '-------------------------------------\n']
        
        with open(self.file_path, 'a') as file:
            file.writelines(lines)  
            
        self.dispatch(x)
            
    def read_file(self):
        with open(self.file_path, 'r') as file:
            report = file.read()
            
        print(report)
        
    def dispatch(self, location):
        start = 'station'
        goal =  location

        visited = dijkstra(start=start, end=goal, MAP=MAP)
        cur_node = goal
        print(f'\nShortest Path from {goal} to {start}: \n {goal} ', end='')
        while cur_node !=  start:
            cur_node = visited[cur_node]
            print(f'---> {cur_node} ', end='')
            
def main():
    obj = Report('Umer', '12400982', 'j', '03132271030', 'Fire')
    
    a = station()
    a.file_report(obj)
    
if __name__ == "__main__":
    main()
    
