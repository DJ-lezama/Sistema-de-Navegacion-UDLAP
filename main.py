import tkinter as tk
from graph import Graph
from data import places, distances
from visualization import GraphVisualizerApp

def main():
    # Create the graph instance
    udlap_graph = Graph()
    for place in places:
        udlap_graph.add_node(place)
    for (from_place, to_place), distance in distances.items():
        udlap_graph.add_edge(from_place, to_place, distance)

    # Create and launch the GUI
    root = tk.Tk()
    app = GraphVisualizerApp(udlap_graph, places)
    app.create_gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
