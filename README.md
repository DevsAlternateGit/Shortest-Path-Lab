                    # Shortest Path Finding Using Multiple Algorithms

                    An interactive algorithm visualization and comparison lab built to study, demonstrate, and analyze multiple shortest path algorithms under different graph conditions.

                    This project goes beyond computing shortest paths by visually exposing algorithm behavior, constraints, and trade-offs across carefully designed graph structures.

                    ---

                    ## 🚀 Features

                    ### 🔹 Multiple Shortest Path Algorithms

                    The application implements the following algorithms:

                    - Dijkstra’s Algorithm
                    - Bellman–Ford Algorithm
                    - SPFA (Shortest Path Faster Algorithm)
                    - DAG Shortest Path Algorithm
                    - BFS (for equal-weight graphs)
                    - A\* Algorithm (restricted to grid graphs)

                    Each algorithm is executed in a step-by-step manner, making its internal working transparent.

                    ---

                    ### 🔹 Structured Graph Builders

                    Instead of relying only on random graphs, the project provides purpose-built graph generators to highlight algorithm strengths and limitations:

                    - Random Graph (Erdős–Rényi, forced connectivity)
                    - Random DAG (with guaranteed path)
                    - DAG with Negative Weights (no negative cycles)
                    - Dense Graph
                    - Sparse Chain Graph
                    - Equal Weight Graph
                    - Grid Graph (for A\*)

                    These builders ensure meaningful and reproducible demonstrations.

                    ---

                    ### 🔹 Step-by-Step Visualization

                    - Algorithms run as state generators
                    - Each step is rendered as a stable frame
                    - Node and edge colors represent algorithm state
                    - Users can step through execution to observe relaxations, frontier updates, and decisions

                    ---

                    ### 🔹 Algorithm Comparison Mode

                    A dedicated comparison view allows:

                    - Running multiple algorithms on the same graph
                    - Side-by-side result analysis
                    - Comparison using:
                    - Nodes explored
                    - Number of relaxations
                    - Final shortest path cost
                    - Exploration patterns

                    This makes algorithmic differences immediately visible.

                    ---

                    ### 🔹 Internal State Transparency

                    For every step, the application exposes:

                    - Distance table
                    - Parent (predecessor) table
                    - Visited and frontier states
                    - Algorithm decision logs

                    This bridges the gap between theory and execution.

                    ---

                    ### 🔹 Reproducibility with Random Seed

                    - All random graph builders accept a seed
                    - Default seed ensures consistent demos
                    - Seed can be changed for exploration and testing

                    This guarantees fair comparison and debuggability.

                    ---

                    ## 🧠 Educational Focus

                    This project is designed as an algorithm learning tool, not just a solver.

                    It demonstrates:

                    - Why Dijkstra fails with negative weights
                    - Why Bellman–Ford is slower but more general
                    - Why DAG shortest path is optimal on acyclic graphs
                    - Why BFS works only for equal-weight graphs
                    - Why A\* explores fewer nodes using heuristics
                    - How graph structure directly affects algorithm behavior

                    ---

                    ## 🏗️ Project Structure

                    ```md
                    shortest_path_app/
                    │
                    ├── app.py
                    ├── graph_utils.py
                    ├── visualizer.py
                    ├── metrics.py
                    │
                    ├── algorithms/
                    │ ├── dijkstra.py
                    │ ├── bellman_ford.py
                    │ ├── spfa.py
                    │ ├── dag_shortest.py
                    │ ├── bfs_equal.py
                    │ └── a_star.py
                    │
                    ├── builders/
                    │ ├── erdos_renyi.py
                    │ ├── random_dag.py
                    │ ├── negative_dag.py
                    │ ├── dense_graph.py
                    │ ├── sparse_chain.py
                    │ ├── equal_weight.py
                    │ └── grid_graph.py
                    │
                    └── pages/
                    ├── 1_Algorithm_Simulator.py
                    └── 2_Algorithm_Comparison.py
                    ```

                    ---

                    ## 🛠️ Tech Stack

                    - Python
                    - Streamlit – UI and interaction
                    - NetworkX – Graph representation and logic
                    - PyVis – Graph visualization

                    ---

                    ## 🎯 Conclusion

                    This project demonstrates that there is no universally best shortest path algorithm.  
                    The optimal choice depends on graph structure, edge weights, and constraints.

                    By combining visualization, comparison, and enforced correctness, the project provides a clear and practical understanding of shortest path algorithms as taught in Design and Analysis of Algorithms (DAA).
