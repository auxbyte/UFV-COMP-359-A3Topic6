from EdgeData import EdgeData
from VertexData import VertexData
from typing import Any

# single vertex or node in a graph
# contains neighbours as edges
class Vertex:
    def __init__(self, data: VertexData):
        self.data = data
        self.outgoing: dict[Any, EdgeData] = {}
        self.incoming: dict[Any, EdgeData] = {}
