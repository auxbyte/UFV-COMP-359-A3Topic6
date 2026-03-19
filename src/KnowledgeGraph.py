from Vertex import Vertex
from typing import Any

# top level object to represent a graph
class KnowledgeGraph:
    def __init__(self):
        self.vertices: dict[Any, Vertex] = {}
    def insert_vertex(self, vid, data):
        if vid not in self.vertices:
            self.vertices[vid] = Vertex(data)

    def vertex_exists(self, vid):
        return vid in self.vertices

    def get_vertex(self, vid):
        return self.vertices.get(vid)

    def remove_vertex(self, vid):
        if vid not in self.vertices:
            return

        vertex = self.vertices[vid]

        # Remove all outgoing edges (vid -> neighbor)
        for neighbor in list(vertex.outgoing):
            self.vertices[neighbor].incoming.pop(vid, None)

        # Remove all incoming edges (neighbor -> vid)
        for neighbor in list(vertex.incoming):
            self.vertices[neighbor].outgoing.pop(vid, None)

        # Finally remove the vertex
        del self.vertices[vid]
