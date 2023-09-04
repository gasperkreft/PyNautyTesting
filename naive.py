import networkx as nx
from itertools import permutations
import time

G = nx.fast_gnp_random_graph(8,0.5)

def generate_mappings(elements):
    mappings = []

    # Generate all permutations of elements2
    from itertools import permutations
    perms = permutations(elements)

    # For each permutation, create a mapping dictionary
    for perm in perms:
        mapping = {elements[i]: perm[i] for i in range(len(elements))}
        mappings.append(mapping)

    return mappings

mappings = generate_mappings(list(range(1, 9)))
print(len(mappings))

start = time.time()
for map in mappings:
    H = nx.relabel_nodes(G, map, copy=True)

end=time.time()
elapsed_time = end - start
print(elapsed_time)


