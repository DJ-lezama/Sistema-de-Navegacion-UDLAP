import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx
from graph import Graph
from data import places, distances

class GraphVisualizer:
    def __init__(self, graph):
        self.graph = graph
        self.selected_path = []  # To store the shortest path

    def visualize(self, highlight_path=None):
        G = nx.Graph()
        for from_node, neighbors in self.graph.items():
            for to_node, weight in neighbors.items():
                G.add_edge(from_node, to_node, weight=weight)

        plt.figure(figsize=(12, 8))
        pos = nx.kamada_kawai_layout(G, weight="weight")

        # Draw the graph
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d:.2f}" for u, v, d in G.edges(data="weight")})

        # Highlight the shortest path
        if highlight_path:
            path_edges = list(zip(highlight_path, highlight_path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=3)

        plt.title("Graph Visualization of UDLAP")
        plt.show()

    def reset_visualization(self):
        """
        Reset the visualization by clearing the selected path.
        """
        self.selected_path = []
        self.visualize()

# Create and Run the Tkinter GUI
def run_gui():
    udlap_graph = Graph()
    for place in places:
        udlap_graph.add_node(place)
    for (from_place, to_place), distance in distances.items():
        udlap_graph.add_edge(from_place, to_place, distance)

    visualizer = GraphVisualizer(udlap_graph.graph)

    # Tkinter GUI
    root = tk.Tk()
    root.title("UDLAP Navigation System")

    # Dropdown menus for start and end points
    tk.Label(root, text="Select Start Point:").grid(row=0, column=0)
    start_combo = ttk.Combobox(root, values=places)
    start_combo.grid(row=0, column=1)

    tk.Label(root, text="Select End Point:").grid(row=1, column=0)
    end_combo = ttk.Combobox(root, values=places)
    end_combo.grid(row=1, column=1)

    # Result label
    result_label = tk.Label(root, text="", wraplength=400, justify="left")
    result_label.grid(row=3, column=0, columnspan=2)

    # Actions
    def calculate_shortest_path():
        start = start_combo.get()
        end = end_combo.get()

        if start and end:
            path, distance = udlap_graph.dijkstra(start, end)
            result_label.config(text=f"Shortest Path: {' -> '.join(path)}\nDistance: {distance:.2f} meters")
            visualizer.visualize(highlight_path=path)
        else:
            result_label.config(text="Please select both start and end points.")

    def reset_graph():
        result_label.config(text="")
        start_combo.set("")
        end_combo.set("")
        visualizer.reset_visualization()

    # Buttons
    calculate_button = tk.Button(root, text="Calculate Path", command=calculate_shortest_path)
    calculate_button.grid(row=2, column=0, pady=10)

    reset_button = tk.Button(root, text="Reset", command=reset_graph)
    reset_button.grid(row=2, column=1, pady=10)

    # Initial Visualization
    visualizer.visualize()

    # Run the Tkinter main loop
    root.mainloop()
