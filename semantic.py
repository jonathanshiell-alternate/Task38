"""
Code snippets as specified
"""

# "SIMILARITY WITH SPACY"
# Load specified module and model
import spacy
nlp = spacy.load('en_core_web_md')

# Compare the strings "cat", "monkey", "banana"
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Print gap for clarity with horizontal line
print(); print("=" * 40); print()

# "Working with vectors" Code as specified - compares each word with each other
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Print gap for clarity with horizontal line
print(); print("=" * 40); print()

# "WORKING WITH SENTENCES" - code as specified
# Compares `sentence_to_compare` with other sentences in `sentences`.

# Set sentence
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

# Set up nlp objects and run comparison
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Print gap for clarity with horizontal line
print(); print("=" * 40); print()

# Write a note about what you found interesting about the similarities
# between cat, monkey and banana and think of an example of your own.
"""
There is more of a common association between monkey and banana than cat and 
banana. This is because there are more examples in literature of monkeys being 
associated with bananas than cats and bananas, and this is reflected in the 
model. This is also reflected in the lack of similarity between apple and both 
cat and monkey, as there is less linkage in the literature used to train the 
model.
"""

# My own examples, based on edits to the input prior code.
# Source: https://genius.com/Subwoolfer-give-that-wolf-a-banana-lyrics
tokens = nlp('wolf grandma monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Print gap for clarity with horizontal line
print(); print("=" * 40); print()

# Let us try yet another example
tokens = nlp("before that wolf eats my grandma give that wolf a banana")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Print gap for clarity with horizontal line
print(); print("=" * 40); print()

# Run the example file with the simpler language model ‘en_core_web_sm’ and 
# write a note on what you notice is different from the model 'en_core_web_md'.
"""
The simpler model tends to produce either similar or lower scores for 
similarity.  This suggests that a higher level of similarity can be observed 
based on a higher level of training, enabling more subtle links to be 
detected.
"""

