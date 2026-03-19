from Vertex import Vertex
from typing import Any

# top level object to represent a graph
class KnowledgeGraph:
    def __init__(self):
        self.vertices: dict[Any, Vertex] = {}