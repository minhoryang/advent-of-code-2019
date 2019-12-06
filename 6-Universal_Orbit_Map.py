import networkx as nx

inputs = open('input.txt').read().split()
inputs = list(map(lambda _: _.split(')'), inputs))

orbits = nx.DiGraph()
orbits.add_edges_from(inputs)
print(sum(nx.shortest_path_length(orbits, source='COM', target=node) for node in orbits.nodes))

#########################

start = set(nx.shortest_path(orbits, source='COM', target='YOU'))
end = set(nx.shortest_path(orbits, source='COM', target='SAN'))
same = start & end
start -= same
end -= same
print(len(start)+len(end)-2)
