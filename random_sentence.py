import pandas as pd
import numpy as np
import random
import re
from collections import defaultdict

    

def walk_graph(graph, distance=5, start_node=None):

    if distance <= 0:
        return []
  
  
    if not start_node:
        start_node = random.choice(list(graph.keys()))
  
  
    weights = np.array(
        list(markov_graph[start_node].values()),
        dtype=np.float64)
  
    weights /= weights.sum()

  
    choices = list(markov_graph[start_node].keys())
    chosen_word = np.random.choice(choices, None, p=weights)
  
    return [chosen_word] + walk_graph(
        graph, distance=distance-1,
        start_node=chosen_word)
  


if __name__ == "__main__":
    
    path = "lebowskiQuote.txt"
    with open(path) as f:
        text = f.read()
    #print(re.split('\w+', text))
    tokenized_text = [word for word in re.split('\W+', text) if word != '']

    #print(tokenized_text)

    markov_graph = defaultdict(lambda: defaultdict(int))

    last_word = tokenized_text[0].lower()
    for word in tokenized_text[1:]:
        word = word.lower()
        markov_graph[last_word][word] += 1
        last_word = word

        
    for i in range(10):
        print(' '.join(walk_graph(
            markov_graph, distance=random.randint(5,12)), '\n')
