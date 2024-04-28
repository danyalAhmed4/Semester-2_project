from report import Report
from heapq import *
import time


#this is the map that the djikstra's algorithm will be applied to.
#it is a dictionary where each key represents a node and it's adjacent nodes along with the cost of going to that node.
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
    #this algo uses a priority queue implemented with heaps.
    queue = []
    heappush(queue, (0, start))
    #the cost_visited dictionary is used to keep track of the lowest cost it has taken till it is updated of reaching every node.
    cost_visited = {start: 0}
    #the visited dictionary keeps track of what nodes have been visited and by what previous node was used to reach it.
    #when it is updated, if a lower cost way was found to reach it, the predecessor node will be changed
    visited = {start: None}
    
    #this while loop runs untill the queue is empty or the node has been found.    
    while queue:
        #the reason heap is used is because as a priority queue 
        #the top element will always be the one with the most priority or in terms related to our code, least cost.
        cur_cost, cur_node = heappop(queue)
        if cur_node == end:
            break
        
        #the next_nodes finds the value of the key-value pair in the MAP dictionary.
        next_nodes = MAP[cur_node]
        #we now loop over each adjacent node, present in the next_nodes and calculate the cost.
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost
                
            #we now check if the node is visited and if it is visited, we check if the new cost is less than the previous calculated cost.
            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                #if the check returns true, we push this cost and node to the queue and then update the cost_visited and visited dictionary.
                heappush(queue, (new_cost, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node
    #we now return the visited dictionary which has the individual nodes shortest path.
    return visited
            
class station:
    def __init__(self) -> None:
        self.file_path = "report.txt"
        self.hospital: hospital = hospital()
        self.policestation: policestation = policestation()
        self.firestation: firestation = firestation()
                
    def file_report(self, REPORT: Report):
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
            
        if REPORT.type == 'Fire':
            self.firestation.dispatch(REPORT.location)
            
        elif REPORT.type == 'Injury':
            self.hospital.dispatch(REPORT.location)
            
        else:
            self.policestation.dispatch(REPORT.location)
            
    def read_file(self):
        with open(self.file_path, 'r') as file:
            report = file.read()
            
        print(report)
        
    def dispatch(self, REPORT: Report):
        pass
    
class hospital(station):
    
    def __init__(self) -> None:
        ...
        
    def dispatch(self, location):
        
        start = 'hospital'
        goal =  location

        visited = dijkstra(start=start, end=goal, MAP=MAP)
        cur_node = goal
        
        print(f'Dispatching Medical Team')
        print(f'Calculating Shortest Path.....')
        time.sleep(2)
        
        #we loop over the dictionary and keep getting the values from the key-value pairs until we reach the starting point.
        #and if we reach it, that is our shortest path.
        print(f'\nShortest Path from {location} to {start}: \n {location} ', end='')
        while cur_node !=  start:
            cur_node = visited[cur_node]
            print(f'---> {cur_node} ', end='')
            
class policestation(station):
    def __init__(self) -> None:
        ...
    
    def dispatch(self, location):
        
        start = 'policestation'
        goal =  location

        visited = dijkstra(start=start, end=goal, MAP=MAP)
        cur_node = goal
        
        print(f'Dispatching Police')
        print(f'Calculating Shortest Path.....')
        time.sleep(2)
        print(f'\nShortest Path from {location} to {start}: \n {location} ', end='')
        while cur_node !=  start:
            cur_node = visited[cur_node]
            print(f'---> {cur_node} ', end='')
            
class firestation(station):

    def __init__(self) -> None:
        ...
    
    def dispatch(self, location):
        start = 'policestation'
        goal =  location

        visited = dijkstra(start=start, end=goal, MAP=MAP)
        cur_node = goal
        
        print(f'Dispatching Firefighters')
        print(f'Calculating Shortest Path.....')
        time.sleep(2)
        print(f'\nShortest Path from {location} to {start}: \n {location} ', end='')
        while cur_node !=  start:
            cur_node = visited[cur_node]
            print(f'---> {cur_node} ', end='')
        
def main():
    obj = station()
    x = input('Do you wish to see the emergency report: ')
    if x == 'yes':
        print('')
        obj.read_file()
        print('')
        
    else:
        print('')
        print('closing')
    
if __name__ == "__main__":
    main()
    
