# Import modules and required models
# spaCy import
import spacy
nlp = spacy.load('en_core_web_md')

#Import other dependencies
import re

#Hard-code description of movie to compare to others
previous = """Will he save their world or destroy it? When the Hulk becomes too dangerous 
for the Earth, the Illuminati trick Hulk into a shuttle and launch him into 
space to a planet where the Hulk can live in peace. Unfortunately, Hulk land 
on the planet Sakaar where he is sold into slavery and trained as a gladiator.
""".replace('\n', '') #(.replace method to remove returns.)
# Generate `previous_token`
previous_token = nlp(previous)

# Set up `Movie` object class to use for comparisons
class Movie:
    
    def __init__ (self, title, description):
        
        """
        Relies on spaCy token for existing description `previous`

        Generates spaCy token using `description` argument, then calculates and saves similarity value
        
        Creates an object for each movie, with a similarity value
        """
        
        # Set up spaCy object as part of `self`
        self.nlp = spacy.load('en_core_web_md')

        # Store title and description
        self.title = title
        self.description = description

        # Generate and compare token for description
        self.token = self.nlp(description)
        self.similarity = self.token.similarity(previous_token)

        # Generate user-friendly comparison score string
        self.percent = f"{self.similarity * 100 :.1f}%"

# Define a function that compares a set of other descriptions using the above object
def print_title_most_similar(descriptions, print_scores = False):

    """
        Parses file using Movie object and the call to spaCy inside its __init__ 
    method to compare the descriptions to the previous movie stored in memory.

        The lines are expected separated by line break characters, and the title 
    and description are expected to be separated by a : with optional space 
    characters to either side.

    Returns the title of the most similar movie.
    """

    # Make lines for line-wise comparison.
    in_lines = re.split('\n+', descriptions)

    # Create list comprehension of movie title, description pairs:
    # List comprehension
    split_items = [re.split(" *: *", movie, 2) for movie in in_lines]
    # Filter out any un-split lines, over-write `split_items` with results
    split_items = [item for item in split_items if len(item) == 2]

    # Create  list of movie objects with similarity values

    similar_movies = [Movie(item[0], item[1]) for item in split_items]

    similar_movies.sort(key = lambda movie:movie.similarity, reverse = True)

    if print_scores:
        # Iterate over sorted list, print title, similarity socre and description.
        for movie in similar_movies:
            print(movie.title, movie.percent, movie.description, sep = ', ')
            print()

    print ("The most similar movie is:", similar_movies[0].title)
    
    return similar_movies[0].title

#   If run as main file, load descriptions of other movies and run the logic 
# described above.
if __name__ == '__main__':

    # Hard-code the name of the file containing descriptions to compare
    in_file = "movies.txt"

    # Read in file 'movies.txt', name as `in_file`, contents as `in_text`
    with open(in_file, "rt") as f:
        in_text = f.read()    

    # Call the function defined above with the descriptions stored in `in_text`.
    print_title_most_similar(in_text)