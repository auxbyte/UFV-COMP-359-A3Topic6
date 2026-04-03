# UFV COMP 359 Assignment 3: Task 6
Implement a knowledge graph data structure.
 * use hash tables for the neighbourhood of each vertex instead of linked lists
 * you do not need to program hash tables yourself---use an API
 * each vertex should be able to store a struct of data, at the very least containing a string
 * each arc should be able to store a struct of data, at the very least containing a string
 * then for vertices u and v, an arc uv between them encodes a relationship or property
 * what is the complexity of inserting a new vertex? a new arc? removing an arc? removing a vertex?
 * demonstrate applying your knowledge base to a dataset, such as a smaller portion of IMDBs free and smaller database (https://datasets.imdbws.com/)

## Usage & Repository Details

### Traversal (Member 4: Sabreen Gill) 
Traversal functionality is implemented in `KnowledgeGraph.py` and includes:
-`get_neighbors(vid)` this returns outgoing neighbors 
-`get_predecessors(vid)` this returns incoming neighbours 
-`bfs(start)` - breafth-first traversal 
-`dfs(start)` - depth-first traversal
-`shortest_path(start, end)` - find the shortest path using BFS 
The methods listed here allow the graph to be explored. They operate on the adjacency dicts (`outgoing` and `incoming`), which are stored in each vertex. 

## Reflection

### Traversal (Member 4: Sabreen Gill) 
For my part, I focused on the implementation of traversal methods which allows the graph to be explored rather than just stored. After reviewing BFS and DFS concepts, I was able to adapt them to the project structure. A challenge I faced was making sure the methods were cleanly integrated with the existing graph design. By using helper methods like `get_neighbors`, I was able to achieve this. This implementation greatly helps in scenarios where you are exploring relationships and finding paths between entities. 

## Complexity Analysis

###Traversal Complexities (Where V = vertices and E = edges) 
-`get_neighbors(vid)`: O(deg(v))
-`get_predecessors(vid)`: O(deg(v))
-`bfs(start)`: O(V + E)
-`dfs(start)`: O(V + E) 
-`shortest_path(start,end)`: O(V + E) 

## References

Member 4: Sabreen Gill 
•	Goodrich, Michael T., Roberto Tamassia, and Michael H. Goldwasser. *Data Structures and Algorithms in Python*. Wiley, 2013.
•	CodeSignal. “Graph Algorithms Implementation: Breadth-First Search (BFS).” https://codesignal.com/learn/courses/getting-deep-into-complex-algorithms-for-interviews-with-python/lessons/graph-algorithms-implementation-breadth-first-search-bfs
•	Cormen, Thomas H., et al. *Introduction to Algorithms*. MIT Press, 2009.
•	OpenAI. “ChatGPT.” https://chat.openai.com/

## Libraries Used
 * Python Standard Library (3.14)
 
## Contributions
 * Parent, Michael [GitHub](https://github.com/auxbyte)
 * Gill, Sabreen [GitHub](https://github.com/sabrreen)
   -Implemented traversal (BFS, DFS, shortest_path)
   -Added helper methods (get_neighbors, get_predecessors)
   -Integrated traversal with KnowledgeGraph structure 
