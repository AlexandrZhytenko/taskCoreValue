# to write given information into txt file

from networkx_tools import *
from draw_graph import G

with open("results.txt", "w") as file:
    file.write("Results of the task:" + "\n")
    file.write("\r")
    file.write("Open 'graph.png' file where you can see the input graph." + "\n")
    file.write("\r")
    file.write("At first I started using standard tools:" + "\n")
    file.write("*It's from 'networkx' library, so I have this results:" + "\n")
    file.write("\t" + "Is there path from start to finish: {}"\
        .format(algorithms.shortest_paths.generic.has_path(G, source="start", target="finish")) + "\n")
    file.write("\t" + "Available probable paths:" + "\n")
    for path in simple_paths_all_simple_paths():
        file.write("\t")
        file.write(str(path))
        file.write("\n")
    file.write("\t" + "The shortest path length is: {}".format(shortest_path_length) + " step")
    file.write("\n")
    file.write("\t" + "The shortest_path: {}".format(shortest_paths_generic_shortest_path()))
    file.write("\n")
    file.write("\t" + "All shortest paths are: {}".format(shortest_paths_generic_all_shortest_paths()))

