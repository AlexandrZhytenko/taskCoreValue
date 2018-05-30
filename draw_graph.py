# to draw graph

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
elist = [("start", "1"),
         ("start", "2"),
         ("1", "2"),
         ("2", "7"),
         ("2", "3"),
         ("2", "8"),
         ("8", "9"),
         ("1", "4"),
         ("4", "5"),
         ("5", "finish"),
         ("finish", "6"),
         ("6", "7"),
         ("7", "8")]
G.add_edges_from(elist)


if __name__ == "__main__":
    print G.number_of_edges()
    print G.number_of_nodes()
    nx.draw(G, with_labels=True, font_weight='bold')
    # plt.savefig("graph.png")
    plt.show()
    plt.close()

