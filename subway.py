# Imagine subway system as a graph
# Adding lines is equal to adding edges and nodes
# Use Dijkstra's algorithm to calculate the shortest paths
# In the end, use back-trace to find out shortest path
# Date: 2016-09-04 
# Authour: ay701@nyu.edu

import sys
import heapq

class Subway_system:
    
    default_interval = 1
    
    def __init__(self, name):
        self.lines = []
        self.stop_dict = {}  #stop name as key, object as value
        self.name = name
        self.num_stops = 0
        
    def get_stop(self,name):
        if name in self.stop_dict:
            return self.stop_dict[name]
        else:
            return None
        
    def add_train_line(self, stops, name, time_between_stations=None):
        
        if len(set(stops))!=len(stops):
            print "Stops are not unique!" 
            sys.exit()
        
        previous = new_stop = None
        
        for ind, stop in enumerate(stops):
            if stop not in self.stop_dict:            
                self.num_stops += 1
                new_stop = Stop(stop,name)
                self.stop_dict[stop] = new_stop
            else:
                self.stop_dict[stop].add_line(name)
                new_stop = self.stop_dict[stop]
            
            if previous:
                
                previous_name = previous.get_name()
                
                if time_between_stations:
                    interval = time_between_stations[ind-1][2]
                else:
                    interval = Subway_system.default_interval
                
                self.stop_dict[stop].add_neighbor(previous,interval)
                self.stop_dict[previous_name].add_neighbor(new_stop,interval)
            
            previous = new_stop
            
    # "top" object as iteration result
    def __iter__(self):
        return iter(self.stop_dict.values())
            
    # return optimal stop list
    def take_train(self, origin, destination):
        
        if not self.get_stop(origin) or not self.get_stop(destination):
            print("Origin or destination does not exist.")
            sys.exit()
        
        start_stop = self.get_stop(origin)
        start_stop.set_distance(0)
        
        unvisited_stops = [(stop.get_distance(),stop) for stop in self]
        heapq.heapify(unvisited_stops)
        
        while len(unvisited_stops):
            
            # Pops a stop with the smallest distance 
            current = heapq.heappop(unvisited_stops)[1]
            current_stop_name = current.get_name()
            current.set_visited()
            
            for next in current.neighbors:
                
                # if visited, skip
                if next.visited:
                    continue
                
                new_dist = current.get_distance() + current.get_interval(next)   
                next_stop_name = next.get_name()
                
                if new_dist < next.get_distance():
                    next.set_distance(new_dist)
                    next.set_previous(current)
                    
            # Clean the heap
            while len(unvisited_stops):
                heapq.heappop(unvisited_stops)
                
            # Put unvisited stops into the list
            unvisited_stops = [(stop.get_distance(),stop) for stop in self if not stop.visited]
            heapq.heapify(unvisited_stops)
        
        last_stop = self.get_stop(destination)
        path = [last_stop.get_name()]
        total_distance = last_stop.get_distance()
        self.shortest(last_stop, path, total_distance)
    
        # Reverse order
        print (path[::-1], total_distance)
    
    @staticmethod 
    def shortest(stop, path, total_distance):
        ''' make shortest path from stop.previous'''
        if stop.previous:
            path.append(stop.previous.get_name())
            total_distance += stop.previous.get_distance()
            Subway_system.shortest(stop.previous, path,total_distance)
        return
    
    def print_stops(self):
        for stop,obj in self.stop_dict.iteritems():
            obj.print_neighbors()

        
class Stop(object):

    def __init__(self,name,line):
        self.name = name
        self.neighbors = {}
        self.distance = sys.maxint
        self.visited = False
        self.previous = None
        self.lines = [line]
            
    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

    def get_interval(self, neighbor):
        return self.neighbors[neighbor]
        
    def set_visited(self):
        self.visited = True
            
    def get_name(self):
        return self.name
    
    def add_line(self,line):
        self.lines.append(line)
    
    def get_neighbors(self):
        return self.neighbors.keys()
                    
    def add_neighbor(self,neighbor,interval=1):
        self.neighbors[neighbor] = interval

    def print_neighbors(self):
        for neighbor, interval in self.neighbors.iteritems():
            print self.name + "-->" + neighbor.name + " (" + str(interval) + ")"
        
    def set_previous(self, prev):
        self.previous = prev
        
    def __str__(self):
        return str(self.name) + ' adjacent: ' + str([x.name for x in self.neighbors])
        
        
if __name__ == '__main__':
    
    subway_system = Subway_system(name="NYC MTA Subway")
    
    # subway_system.add_train_line(stops=["Rockaway","Nostrand Ave","Utica Ave"],name="A")
    # subway_system.add_train_line(stops=["8th Ave","Atlantic Ave","Canal St","42th St Time Square","57th St","Columbia University"],name="N")
    # subway_system.add_train_line(stops=["Atlantic Ave","Columbia University","Forest Hill"],name="Q",time_between_stations=[("Atlantic Av", "Columbia Universit", 1),
    #                              ("Columbia Universit", "Forest Hill", 1)
    #                              ])
    # # print subway_system.take_train("Rockaway","Nostrand Ave")
    # subway_system.take_train("8th Ave","Columbia University")
    # system.print_stops()
    
    subway_system.add_train_line(stops=["Canal", "Houston", "Christopher", "14th"], name="1",
          time_between_stations=[("Canal", "Houston", 3),
                                 ("Houston", "Christopher", 7),
                                 ("Christopher", "14th", 2),
                                 ])
    subway_system.add_train_line(stops=["Spring", "West 4th", "14th", "23rd"], name="E",
          time_between_stations=[("Spring", "West 4th", 1),
                                 ("West 4th", "14th", 5),
                                 ("14th", "23rd", 2),
                                 ])
    
    print "\nShortest Path from '%s' to '%s' " % ("Houston", "23rd") 
    subway_system.take_train(origin="Houston", destination="23rd")
    # returns (["Houston", "Christopher", "14th", "23rd"], 11)

