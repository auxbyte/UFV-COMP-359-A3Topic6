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
    
    def insert_arc(self, u, v, edge_data):
        if u not in self.vertices or v not in self.vertices:
            return False

        source = self.vertices[u]
        dest = self.vertices[v]

        source.outgoing[v] = edge_data
        dest.incoming[u] = edge_data
        return True

    def remove_arc(self, u, v):
        if u not in self.vertices or v not in self.vertices:
            return False

        source = self.vertices[u]
        dest = self.vertices[v]

        if v not in source.outgoing:
            return False

        source.outgoing.pop(v)
        dest.incoming.pop(u)
        return True

    def arc_exists(self, u, v):
        if u not in self.vertices or v not in self.vertices:
            return False

        return v in self.vertices[u].outgoing

    def get_arc(self, u, v):
        if u not in self.vertices or v not in self.vertices:
            return None

        return self.vertices[u].outgoing.get(v)

#Sabreen's contribution starts now 
    
    #get all outgoing neighbours of a vertex 
    def get_neighbors(self, vid):
        #checking if vertex exists in graph
        if vid not in self.vertices:
            return []
            #outgoing is a dict ---> keys are neighbour vertex ids 
            return list(self.vertices[vid].outgoing.keys())
            
    #get all incoming neighbours (who point to this vertex)
    def get_predecessors(self,vid):
        if vid not in self.vertices:
            return []

            #incoming dict stores vertices that connect to this one 
            return list(self.vertices[vid].incoming.keys())
    

