from KnowledgeGraph import KnowledgeGraph
from VertexData import VertexData

# main entry point
def main():
    kg = KnowledgeGraph()

    # Insert vertices
    kg.insert_vertex("A", VertexData("name", "Alice"))
    kg.insert_vertex("B", VertexData("name", "Bob"))

    # Test exists
    print("A exists:", kg.vertex_exists("A"))  # True

    # Test get
    v = kg.get_vertex("A")
    print("A data:", v.data.data)  # Alice

    # Remove vertex
    kg.remove_vertex("A")
    print("A exists after removal:", kg.vertex_exists("A"))  # False

if __name__ == "__main__":
    main()
