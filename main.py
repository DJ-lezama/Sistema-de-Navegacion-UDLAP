import tkinter as tk
from graph import Graph
from data import places, distances
from visualization import GraphVisualizerApp
from evaluation import evaluate_system, display_evaluation_results

def main():
    # Create the graph instance
    udlap_graph = Graph()
    for place in places:
        udlap_graph.add_node(place)
    for (from_place, to_place), distance in distances.items():
        udlap_graph.add_edge(from_place, to_place, distance)

    # Test Cases for Evaluation
    test_cases = [
        ("CE", "AU", ["CE", "AU"], 101.86),
        ("CE", "CS", ["CE", "CS"], 52.93),
        ("SL", "TD", ["SL", "TD"], 42.79),
        ("IA", "LB", ["IA", "LB"], 21.4),
        ("CE", "HU", ["CE", "AU", "HA", "HU"], 280.33),
        ("CE", "LB", ["CE", "AU", "IA", "LB"], 263.26),
    ]

    # Evaluate the system
    evaluation_results = evaluate_system(udlap_graph, test_cases)
    display_evaluation_results(evaluation_results)

    # Create and launch the GUI
    root = tk.Tk()
    root.geometry("1000x700")
    app = GraphVisualizerApp(udlap_graph, places)
    app.create_gui(root)
    app.visualize_graph()
    root.mainloop()

if __name__ == "__main__":
    main()
