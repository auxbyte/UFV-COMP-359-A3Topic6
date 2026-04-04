# Jack Tse's contribution
# Visualization code for mermaid
# This is a parser that we can paste the output data into and it will generate the mermaid code for us to visualize the relationships between actors, movies, directors, and co-stars.

import re

# Paste the output data here that we got from RunRealDemo.py, 
# and it will generate the mermaid code for us to visualize the relationships 
# between actors, movies, directors, and co-stars.

data = """
=== Filmography of Leonardo DiCaprio ===
- Hubble 3D [actor]
- Inception [actor]
- J. Edgar [actor]
- Shutter Island [actor]

=== Director(s) of Inception ===
- Christopher Nolan

=== Co-stars of Leonardo DiCaprio ===
- Armie Hammer
- Ben Kingsley
- Brady Matthews
- Cheryl Lawson
- Cillian Murphy
- David A. Cooper
- Dileep Rao
- Elliot Page
- Emily Mortimer
- Geoff Pierson
- Gunner Wright
- Jackie Earle Haley
- John Carroll Lynch
- Joseph Gordon-Levitt
- Josh Hamilton
- Kaitlyn Dever
- Ken Watanabe
- Marion Cotillard
- Mark Ruffalo
- Max von Sydow
- Michelle Williams
- Naomi Watts
- Patricia Clarkson
- Pete Postlethwaite
- Ted Levine
- Tom Berenger
- Tom Hardy
"""

# function to convert names to valid node ids by replacing non-alphanumeric characters with underscores
def node_id(name):
    return re.sub(r'\W+', '_', name)

# three dictionaries to store the relationships
filmography = {}
directors = {}
co_stars = {}

# variables to keep track of the current section and main actor for co-stars
current_section = None
main_actor = None

# Parse the text
# We iterate through each line of the data, determine which section we're in (filmography, directors, co-stars), 
# and populate the corresponding dictionaries with the relationships.
for line in data.splitlines():
    line = line.strip()
    if line.startswith("==="):
        if "Filmography" in line:
            current_section = "filmography"
            main_actor = re.search(r'Filmography of (.+?) ===', line).group(1)
            filmography[main_actor] = []
        elif "Director" in line:
            current_section = "directors"
            movie_name = re.search(r'Director\(s\) of (.+?) ===', line).group(1)
            directors[movie_name] = []
        elif "Co-stars" in line:
            current_section = "co_stars"
            co_stars[main_actor] = []
    elif line.startswith("-"):
        content = line[2:].strip()
        if current_section == "filmography":
            movie = content.replace(" [actor]", "")
            filmography[main_actor].append(movie)
        elif current_section == "directors":
            directors[movie_name].append(content)
        elif current_section == "co_stars":
            co_stars[main_actor].append(content)

# First Line of Mermaid code
mermaid_code = ["flowchart LR"]

# for loop to generate the mermaid code for each relationship type 
# actors to movies, directors to movies, and co-stars to main actor
# Actors -> movies
for actor, movies in filmography.items():
    actor_id = node_id(actor)
    for movie in movies:
        movie_id = node_id(movie)
        mermaid_code.append(f'    {actor_id}[{actor}] -->|actor| {movie_id}[{movie}]')

# Directors -> movies
for movie, dirs in directors.items():
    movie_id = node_id(movie)
    for director in dirs:
        director_id = node_id(director)
        mermaid_code.append(f'    {director_id}[{director}] -->|director| {movie_id}[{movie}]')

# Co-stars -> main actor only
for actor, stars in co_stars.items():
    actor_id = node_id(actor)
    for star in stars:
        star_id = node_id(star)
        mermaid_code.append(f'    {star_id}[{star}] -->|co-star| {actor_id}[{actor}]')

# Join all the lines of mermaid code into a single string and print it out
print("\n".join(mermaid_code))