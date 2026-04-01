import csv
from KnowledgeGraph import KnowledgeGraph
from VertexData import VertexData
from EdgeData import EdgeData

# Takes about 5 minutes on my slower laptop even with the filters
# Tried to make a max amount of rows for each file
# That ruins the queries since it is ordered by title id, not movie, year, etc
def load_imdb(titles_file = "./data/title.basics.tsv", names_file = "./data/name.basics.tsv", principals_file = "./data/title.principals.tsv"):
    graph = KnowledgeGraph()
    valid_titles = set()
    # opens movie titles
    with open(titles_file, encoding = "utf-8") as f:
        reader = csv.DictReader(f, delimiter = "\t")
        for row in reader:
            # filter only movies
            if row["titleType"] != "movie":
                continue
            # fix to some movies having \N instead of a number for year
            title_year = row["startYear"]
            if title_year == "\\N":
                continue
            # filter out movies from before to keep it to only 2010 and 2011
            title_year = int(title_year)
            if title_year < 2010 or title_year > 2011:
                continue
 
            title_id = row["tconst"]
            title_name = row["primaryTitle"]
            # Adds movie's id and title as a vertex
            graph.insert_vertex(title_id, VertexData("title", title_name))
            # adds id to valid titles, to only load the principals for these movies
            valid_titles.add(title_id)

    # this will only store people in these valid movies
    valid_person_ids = set()
    edges = []
    # opens principal file
    with open(principals_file, encoding = "utf-8") as f:
        reader = csv.DictReader(f, delimiter = "\t")
        for row in reader:
            title_id = row["tconst"]
            # filters out principals for invalid movies
            if title_id not in valid_titles:
                continue
            # filters out roles not used in our queries
            if row["category"] not in ("actor", "actress", "director"):
                continue
            person_id = row["nconst"]
            # skips person ids that are missing
            if person_id == "\\N":
                continue
            valid_person_ids.add(person_id)
            role =  row["category"]
            # saves the edge to add after vertices are done
            edges.append((person_id, title_id, role))

    # opens the names file
    with open(names_file, encoding = "utf-8") as f:
        reader = csv.DictReader(f, delimiter = "\t")
        for row in reader:
            person_id = row["nconst"]
            # only loads people from valid movies and adds as vertex
            if person_id in valid_person_ids:
                graph.insert_vertex(person_id, VertexData("person", row["primaryName"]))
    # all vertices exist, so adds the edges
    for person_id, title_id, role in edges:
        graph.insert_arc(person_id, title_id, EdgeData("role", role))
    return graph