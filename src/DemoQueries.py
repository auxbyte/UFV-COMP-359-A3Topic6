from KnowledgeGraph import KnowledgeGraph
from VertexData import VertexData
from EdgeData import EdgeData

def _is_person(vertex):
    return vertex.data.label.lower() == "person"

def _is_title(vertex):
    return vertex.data.label.lower() == "title"

def _find_person_ids_by_name(graph, person_name):
    matches = []
    for vid, vertex in graph.vertices.items():
        if _is_person(vertex) and str(vertex.data.data).lower() == person_name.lower():
            matches.append(vid)
    return matches

def _find_title_ids_by_name(graph, title_name):
    matches = []
    for vid, vertex in graph.vertices.items():
        if _is_title(vertex) and str(vertex.data.data).lower() == title_name.lower():
            matches.append(vid)
    return matches

def filmography_of_person(graph, person_name):
    person_ids = _find_person_ids_by_name(graph, person_name)
    results = []

    for person_id in person_ids:
        person_vertex = graph.get_vertex(person_id)

        for title_id, edge_data in person_vertex.outgoing.items():
            title_vertex = graph.get_vertex(title_id)
            if title_vertex is None or not _is_title(title_vertex):
                continue

            results.append({
                "title": title_vertex.data.data,
                "role": edge_data.data
            })

    results.sort(key=lambda x: str(x["title"]).lower())
    return results

def director_of_title(graph, title_name):
    title_ids = _find_title_ids_by_name(graph, title_name)
    directors = []

    for title_id in title_ids:
        title_vertex = graph.get_vertex(title_id)

        for person_id, edge_data in title_vertex.incoming.items():
            person_vertex = graph.get_vertex(person_id)
            if person_vertex is None or not _is_person(person_vertex):
                continue

            if str(edge_data.data).lower() == "director":
                directors.append(person_vertex.data.data)

    return sorted(set(directors), key=lambda x: str(x).lower())

def co_stars_of_person(graph, person_name):
    person_ids = _find_person_ids_by_name(graph, person_name)
    co_stars = set()

    for person_id in person_ids:
        person_vertex = graph.get_vertex(person_id)

        for title_id, edge_data in person_vertex.outgoing.items():
            if str(edge_data.data).lower() not in ("actor", "actress"):
                continue

            title_vertex = graph.get_vertex(title_id)
            if title_vertex is None or not _is_title(title_vertex):
                continue

            for other_person_id, other_edge_data in title_vertex.incoming.items():
                if other_person_id == person_id:
                    continue

                if str(other_edge_data.data).lower() not in ("actor", "actress"):
                    continue

                other_person_vertex = graph.get_vertex(other_person_id)
                if other_person_vertex is None or not _is_person(other_person_vertex):
                    continue

                co_stars.add(other_person_vertex.data.data)

    return sorted(co_stars, key=lambda x: str(x).lower())

def print_filmography(graph, person_name):
    results = filmography_of_person(graph, person_name)
    print(f"\n=== Filmography of {person_name} ===")

    if not results:
        print("No results found.")
        return

    for item in results:
        print(f"- {item['title']} [{item['role']}]")

def print_director_of_title(graph, title_name):
    directors = director_of_title(graph, title_name)
    print(f"\n=== Director(s) of {title_name} ===")

    if not directors:
        print("No results found.")
        return

    for director in directors:
        print(f"- {director}")

def print_co_stars(graph, person_name):
    results = co_stars_of_person(graph, person_name)
    print(f"\n=== Co-stars of {person_name} ===")

    if not results:
        print("No results found.")
        return

    for name in results:
        print(f"- {name}")

def build_small_demo_graph():
    graph = KnowledgeGraph()

    graph.insert_vertex("p1", VertexData("person", "Leonardo DiCaprio"))
    graph.insert_vertex("p2", VertexData("person", "Joseph Gordon-Levitt"))
    graph.insert_vertex("p3", VertexData("person", "Christopher Nolan"))
    graph.insert_vertex("p4", VertexData("person", "Tom Hardy"))

    graph.insert_vertex("t1", VertexData("title", "Inception"))

    graph.insert_arc("p1", "t1", EdgeData("role", "actor"))
    graph.insert_arc("p2", "t1", EdgeData("role", "actor"))
    graph.insert_arc("p3", "t1", EdgeData("role", "director"))
    graph.insert_arc("p4", "t1", EdgeData("role", "actor"))

    return graph

def run_demo():
    graph = build_small_demo_graph()

    print_filmography(graph, "Leonardo DiCaprio")
    print_director_of_title(graph, "Inception")
    print_co_stars(graph, "Leonardo DiCaprio")

if __name__ == "__main__":
    run_demo()