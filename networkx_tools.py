# to use networkx tools

from draw_graph import G
from networkx import algorithms

def shortest_paths_generic_shortest_path():
    list_step = algorithms.shortest_paths.generic.shortest_path(G, source="start", target="finish")
    return list_step

def shortest_paths_generic_all_shortest_paths():
    list_step = algorithms.shortest_paths.generic.all_shortest_paths(G, source="start", target="finish")
    return [i for i in list_step]

def simple_paths_all_simple_paths():
    list_step = list(algorithms.simple_paths.all_simple_paths(G, source="start", target="finish"))
    return list_step

shortest_path_length = algorithms.shortest_paths.generic.shortest_path_length(G, source="start", target="finish")

if __name__ == "__main__":
    print "Is there path from start to finish: {}"\
        .format(algorithms.shortest_paths.generic.has_path(G, source="start", target="finish"))
    print "Available probable paths:"
    for path in simple_paths_all_simple_paths():
        print path
    print "The shortest path length is: {}".format(shortest_path_length)
    print "shortest_path:"
    print shortest_paths_generic_shortest_path()
    print "all_shortest_path:"
    print shortest_paths_generic_all_shortest_paths()
