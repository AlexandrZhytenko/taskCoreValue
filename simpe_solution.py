from draw_graph import G

# The function defines the path between two nodes. It takes a graph G from draw_graph.py,
# the start and end nodes as arguments. Returns the list of nodes
# (including the beginning and ending nodes) that are included in the search path.
# If no path can be found, it returns None.
# The same node will enter no more than once in the return path.

def find_path(graph=G, start="start", end="end", path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph=G, start=node, end="finish", path=path)
            if newpath:
                return newpath
    return None

def find_all_paths(graph=G, start="start", end="finish", path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph=G, start=node, end="finish", path=path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def sort_by_length(input_list):
    return len(input_list)

def find_shortest_path(all_paths=find_all_paths(), key_sort=sort_by_length):
    return sorted(find_all_paths(), key=sort_by_length)[0]

def find_all_shortest_paths(all_paths=find_all_paths(),\
                            shortest_path=find_shortest_path()):
    return [path for path in find_all_paths() if len(path) == len(find_shortest_path())]

if __name__ == "__main__":
    print "Available probable paths:"
    for path in find_all_paths():
        print path
    print "The shortest path length is: {}".format(len(find_shortest_path()) - 1)
    print "shortest_path:"
    print find_shortest_path()
    print "all_shortest_path:"
    print find_all_shortest_paths()

