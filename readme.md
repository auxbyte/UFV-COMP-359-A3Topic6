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

### Running the IMDb Demo

This project requires IMDb dataset files, which are not included in the repository.

#### Setup

1. Create a folder inside `src` called:

`src/data/`

2. Download the following files from:
https://datasets.imdbws.com/

- title.basics.tsv.gz
- name.basics.tsv.gz
- title.principals.tsv.gz

3. Extract the files and place the `.tsv` files into:

`src/data/`

#### Running the Demo

From the `src` directory, run:

`python RunRealDemo.py`

### Core Data Structures (Member 1: Michael)

Core Data Structures were implemented across the codebase:

- `EdgeData.py` - store edge between two variables
- `KnowledgeGraph.py` - top level object to represent a graph
- `Vertex.py` - single vertex/node in a graph
- `VertexData.py` - data for a vertex

These classes served as a foundation for the other group members to build structure and methods around.

### Traversal (Member 4: Sabreen)

Traversal functionality is implemented in `KnowledgeGraph.py` and includes:

- `get_neighbors(vid)` — returns outgoing neighbors
- `get_predecessors(vid)` — returns incoming neighbors
- `bfs(start)` — breadth-first traversal
- `dfs(start)` — depth-first traversal
- `shortest_path(start, end)` — find shortest path using BFS

These methods allow the graph to be explored using adjacency dictionaries (`outgoing` and `incoming`) stored in each vertex.

### IMDb Loader (Member 5: Zach)

The IMDb data loader is implemented in `IMDBLoader.py` and includes:

- Parsing title.basics.tsv, name.basics.tsv, and title.principals.tsv using Python's csv.DictReader.
- Filtering dataset to include only movies withing the years 2010-2011.
- Filtering principals to include actor, actress, and director.
- Creating vertices for movie IDs and names for titles, and actors, actresses and directors.
- Inserted edges representing these roles between the people and titles.

This loader allows the system to work with a real IMDb dataset and limits it so it's not too big.

### Demo Queries (Member 6: Kirat)

The demo queries are implemented in `DemoQueries.py` and demonstrated using real IMDb data in `RunRealDemo.py`.

The following queries are supported:

- Filmography of a person
- Director(s) of a title
- Co-stars of a person

These queries traverse the knowledge graph using adjacency dictionaries to retrieve relationships between people and titles.

## Reflection

### Structures & Planning (Michael)

For my part, I focused on initial planning and system design. I reviewed the best practices with `Knowledge Graph` implementations and common details. I was able to create the foundational classes for the team to use.
I also planned out the various division of tasks among the group members.

### Traversal (Sabreen)

For my part, I focused on the implementation of traversal methods which allows the graph to be explored rather than just stored. After reviewing BFS and DFS concepts, I was able to adapt them to the project structure. A challenge I faced was making sure the methods were cleanly integrated with the existing graph design. By using helper methods like `get_neighbors`, I was able to achieve this. This implementation greatly helps in scenarios where you are exploring relationships and finding paths between entities.

### IMDb Loader (Zach)

For my part, I focused on the implementation of the data loader that converts the IMDb .tsv files into a knowledge graph. I spent awhile trying to filter the dataset down, as even with a smaller dataset it still has to iterate through the large files. It still isn't the most optimized thing as dictReader is not the fastest, but I managed to filter it down and go through less by tracking only valid movie IDs and person IDs.

### Demo Queries (Kirat)

For my part, I implemented query functions that allow the knowledge graph to be used in a meaningful way. These include filmography lookup, director lookup, and co-star relationships. I first tested my queries using a small manually constructed graph, then integrated them with the IMDb loader to run on real data. A key challenge was ensuring the queries correctly navigated the graph structure using outgoing and incoming edges.

## Complexity Analysis

### Traversal Complexities (Where V = vertices and E = edges)

- `get_neighbors(vid)`: O(deg(v))
- `get_predecessors(vid)`: O(deg(v))
- `bfs(start)`: O(V + E)
- `dfs(start)`: O(V + E)
- `shortest_path(start, end)`: O(V + E)

### IMDb Loader Complexities

Time:
- Loading titles: O(T)
- Loading principals: O(P)
- Loading names: O(N)
- Adding edges: O(E)
- Total: O(T + P + N)
Space:
- Storing vertices: O(T' + N')
- Loading edges: O(P')
- Total: O(T' + P' + N')

### Demo Query Complexities

- Filmography of a person: O(deg(v))
- Director of a title: O(deg(v))
- Co-stars of a person: O(V + E) in worst case

## References

- IMDb. (2024). "IMDb Non-Commercial Datasets." IMDb. https://datasets.imdbws.com/
- Python Software Foundation. (2026) "csv — CSV File Reading and Writing." Python 3.14 documentation.
https://docs.python.org/3/library/csv.html

Sabreen

- Goodrich, Michael T., Roberto Tamassia, and Michael H. Goldwasser. *Data Structures and Algorithms in Python*. Wiley, 2013.
- CodeSignal. “Graph Algorithms Implementation: Breadth-First Search (BFS).” https://codesignal.com/learn/courses/getting-deep-into-complex-algorithms-for-interviews-with-python/lessons/graph-algorithms-implementation-breadth-first-search-bfs
- Cormen, Thomas H., et al. *Introduction to Algorithms*. MIT Press, 2009.
- OpenAI. “ChatGPT.” https://chat.openai.com/

## Libraries Used

* Python Standard Library (3.14)


## Contributions

* Parent, Michael [GitHub](https://github.com/auxbyte)
  - Planned project scheduling & division of work
  - Planned overall structure & implementation detail
  - Defined core Vertex & Arc Data Structures
  - Built top-level KnowledgeGraph class and structure

* Gill, Sabreen [GitHub](https://github.com/sabrreen)
  - Implemented traversal (BFS, DFS, shortest_path)
  - Added helper methods (get_neighbors, get_predecessors)
  - Integrated traversal with KnowledgeGraph structure
  
* Carr, Zach [GitHub](https://github.com/zachcarr16)
  - Implemented IMDb dataset loader (load_imdb)
  - Designed filtering logic for tsv files
  - Integrated dataset parsing with the KnowledgeGraph structure

* Dhami, Kirat [GitHub](https://github.com/KiratDhami1)
  - Implemented demo queries (filmography, director, co-stars)
  - Integrated queries with IMDb dataset
  - Created demo runner for real data (`RunRealDemo.py`)
