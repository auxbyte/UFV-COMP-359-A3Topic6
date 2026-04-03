from IMDBLoader import load_imdb
from DemoQueries import print_filmography, print_director_of_title, print_co_stars

def main():
    print("Loading IMDb data...")
    graph = load_imdb()

    print("\nFinished loading IMDb data.")

    print_filmography(graph, "Leonardo DiCaprio")
    print_director_of_title(graph, "Inception")
    print_co_stars(graph, "Leonardo DiCaprio")

if __name__ == "__main__":
    main()