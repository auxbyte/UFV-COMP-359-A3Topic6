from KnowledgeGraph import KnowledgeGraph
from VertexData import VertexData
from EdgeData import EdgeData

def main():
    kg = KnowledgeGraph()

    # insert vertices
    kg.insert_vertex("A", VertexData("name", "Alice"))
    kg.insert_vertex("B", VertexData("name", "Bob"))

    # create edge data
    edge = EdgeData("relation", "friend")

    # test insert arc
    print("Insert arc:", kg.insert_arc("A", "B", edge))

    # test exists
    print("Arc exists A->B:", kg.arc_exists("A", "B"))

    # test get
    arc = kg.get_arc("A", "B")
    print("Arc data:", arc.data if arc else None)

    # test remove
    print("Remove arc:", kg.remove_arc("A", "B"))

    # test exists again
    print("Arc exists after removal:", kg.arc_exists("A", "B"))

if __name__ == "__main__":
    main()