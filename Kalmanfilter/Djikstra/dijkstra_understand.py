'''
Part 1: Understand Dijkstra Shortest Path Planning
 ----------------------------------------------------------
'''

from dijkstra_module import *

g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ] 
paths = g.dijkstra(0)


def shortest_path(paths, v_destination):

    possible_paths = []

    for section in paths:
        v_source, v_dest, dist_btwn_vertices, path_length = section[:4]
        if v_destination == v_dest:
            possible_paths.append(section)
    
    return min(possible_paths, key = lambda t: t[3])


def find_visited_vertices(paths, v_destination):

    visited_vertices = []
    visited_vertices.append(v_destination)

    while v_destination !=0:
        
        path = shortest_path(paths,v_destination)
        visited_vertices.append(path[0])
        v_destination = path[0]

    #print(visited_vertices)

    return visited_vertices



def understand_graph():

    print("\nAll Possible Paths list: ")
    #Print all possible paths
    for section in paths:
        v_source, v_dest, dist_btwn_vertices = section[:3]
        print(v_source, v_dest, dist_btwn_vertices)

    #Sort paths in order of vertices
    print("\nPaths list sorted")
    paths.sort(key= lambda t: t[1])
    for section in paths:
        v_source, v_dest, dist_btwn_vertices = section[:3]
        print(v_source, v_dest, dist_btwn_vertices)

    print("\nShortest Path to destination vertix")
    #print shortest path from V0 to V1,V2,..V8
    for i in range(1,9):
        print(shortest_path(paths,i))

    
    print("\nSequence to reach vertice destination")
    #print the sequence to reach vertice destination
    for i in range(1,9):
        print(find_visited_vertices(paths, i))
    
        

if __name__ == "__main__":
    understand_graph()
    
