def evaluate_system(graph, test_cases):
    """
    Evaluate the graph system by comparing the calculated shortest paths
    and distances to expected results.
    Parameters:
        graph (Graph): The graph instance.
        test_cases (list): A list of test cases, each as a tuple:
                           (start, end, expected_path, expected_distance).
    """
    results = []
    for start, end, expected_path, expected_distance in test_cases:
        actual_path, actual_distance = graph.dijkstra(start, end)
        is_path_correct = actual_path == expected_path
        is_distance_correct = abs(actual_distance - expected_distance) < 1e-2  # Allow small float error
        results.append({
            "start": start,
            "end": end,
            "expected_path": expected_path,
            "actual_path": actual_path,
            "path_correct": is_path_correct,
            "expected_distance": expected_distance,
            "actual_distance": actual_distance,
            "distance_correct": is_distance_correct
        })
    return results

def display_evaluation_results(results):
    """Display the evaluation results in a formatted table."""
    print(f"{'Start':<10} {'End':<10} {'Expected Path':<30} {'Actual Path':<30} {'Path OK':<10} {'Expected Distance':<20} {'Actual Distance':<20} {'Distance OK':<10}")
    print("-" * 130)
    for result in results:
        print(f"{result['start']:<10} {result['end']:<10} {str(result['expected_path']):<30} {str(result['actual_path']):<30} {str(result['path_correct']):<10} {result['expected_distance']:<20} {result['actual_distance']:<20.2f} {str(result['distance_correct']):<10}")
