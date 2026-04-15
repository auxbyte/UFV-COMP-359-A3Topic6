import csv
from KnowledgeGraph import KnowledgeGraph
from VertexData import VertexData
from EdgeData import EdgeData

def load_imdb(titles_file="./data/title.basics.tsv", names_file="./data/name.basics.tsv", principals_file="./data/title.principals.tsv"):

    graph = KnowledgeGraph()
    valid_titles = set()
    valid_person_ids = set()
    pending_edges = []

    with open(titles_file, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        header = next(reader)

        idx_type = header.index("titleType")
        idx_year = header.index("startYear")
        idx_id = header.index("tconst")
        idx_title = header.index("primaryTitle")

        for i, row in enumerate(reader):
            if row[idx_type] != "movie":
                continue
            year = row[idx_year]
            if year == "\\N" or int(year) != 2010:
                continue
            title_id = row[idx_id]
            graph.insert_vertex(title_id, VertexData("title", row[idx_title]))
            valid_titles.add(title_id)

    with open(principals_file, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        header = next(reader)

        idx_t = header.index("tconst")
        idx_cat = header.index("category")
        idx_p = header.index("nconst")

        for i, row in enumerate(reader):
            if i >= 28000000:
                break
            tconst = row[idx_t]
            if tconst not in valid_titles:
                continue

            category = row[idx_cat]
            if category not in ("actor", "actress", "director"):
                continue

            person_id = row[idx_p]
            if person_id == "\\N":
                continue

            valid_person_ids.add(person_id)
            pending_edges.append((person_id, tconst, category))

    with open(names_file, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        header = next(reader)

        idx_id = header.index("nconst")
        idx_name = header.index("primaryName")

        for i, row in enumerate(reader):
            if i >= 750000:
                break
            person_id = row[idx_id]
            if person_id in valid_person_ids:
                graph.insert_vertex(person_id, VertexData("person", row[idx_name]))

    for person_id, title_id, role in pending_edges:
         graph.insert_arc(person_id, title_id, EdgeData("role", role))
    return graph
