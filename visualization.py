import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx


class GraphVisualizerApp:
    def __init__(self, graph, places):
        self.graph = graph
        self.places = places
        self.selected_path = []  # Store the calculated shortest path

    def create_gui(self, root):
        # Main layout: divide into left panel and graph container
        self.left_panel = tk.Frame(root, width=200, bg="lightgray")
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y)

        self.graph_container = tk.Frame(root, bg="white")
        self.graph_container.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Add dropdowns and buttons to the left panel
        tk.Label(self.left_panel, text="Start Point:").pack(pady=10)
        self.start_combo = ttk.Combobox(self.left_panel, values=self.places)
        self.start_combo.pack()

        tk.Label(self.left_panel, text="End Point:").pack(pady=10)
        self.end_combo = ttk.Combobox(self.left_panel, values=self.places)
        self.end_combo.pack()

        self.result_label = tk.Label(self.left_panel, text="", wraplength=180, justify="left", bg="lightgray")
        self.result_label.pack(pady=20)

        self.calculate_button = tk.Button(self.left_panel, text="Calculate Path", command=self.calculate_shortest_path)
        self.calculate_button.pack(pady=10)

        self.reset_button = tk.Button(self.left_panel, text="Reset Graph", command=self.reset_graph)
        self.reset_button.pack(pady=10)

    def visualize_graph(self, highlight_path=None):
        G = nx.Graph()
        for from_node, neighbors in self.graph.graph.items():
            for to_node, weight in neighbors.items():
                G.add_edge(from_node, to_node, weight=weight)

        # Create figure
        plt.figure(figsize=(8, 6))
        pos = nx.kamada_kawai_layout(G, weight="weight")
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d:.2f}" for u, v, d in G.edges(data="weight")})

        # Highlight shortest path if provided
        if highlight_path:
            path_edges = list(zip(highlight_path, highlight_path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=3)

        # Embed the plot into the Tkinter graph container
        figure = plt.gcf()
        for widget in self.graph_container.winfo_children():
            widget.destroy()  # Clear any existing graph
        canvas = FigureCanvasTkAgg(figure, self.graph_container)
        canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)
        canvas.draw()

    def calculate_shortest_path(self):
        start = self.start_combo.get()
        end = self.end_combo.get()
        if start and end:
            path, distance = self.graph.dijkstra(start, end)
            self.result_label.config(text=f"Shortest Path: {' -> '.join(path)}\nDistance: {distance:.2f} meters")
            self.visualize_graph(highlight_path=path)
        else:
            self.result_label.config(text="Please select both start and end points.")

    def reset_graph(self):
        self.result_label.config(text="")
        self.start_combo.set("")
        self.end_combo.set("")
        self.visualize_graph()
