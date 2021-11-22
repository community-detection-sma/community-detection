import networkx as nx
import pandas as pd

import networkx.algorithms.shortest_paths as s

import networkx.algorithms.cluster as nxx

print("Jazz Musicians Network")
jazz = nx.read_weighted_edgelist("jazz.net")
print("no of nodes-", nx.number_of_nodes(jazz))
print("no of edges-", nx.number_of_edges(jazz))
print("avg path length-", nx.average_shortest_path_length(jazz))
print("avg clustering coefficient-", nx.average_clustering(jazz))
nx.draw(jazz,with_labels = True)




print("Karate Club Network")
#Karate Club Network
#karate = nx.karate_club_graph()
# karate = nx.read_weighted_edgelist("karate.net")
karate = nx.read_gml("karate.gml",label = 'id')
print("no of nodes-", nx.number_of_nodes(karate))
print("no of edges-", nx.number_of_edges(karate))
print("avg path length-", nx.average_shortest_path_length(karate))
print("avg clustering coefficient-", nx.average_clustering(karate))
nx.draw(karate,with_labels = True)



#Dolphins Social Media Network
print("Dolphins Social Media Network")
dolphins = nx.read_gml("dolphins.gml",label = 'id')
print("no of nodes-", nx.number_of_nodes(dolphins))
print("no of edges-", nx.number_of_edges(dolphins))
print("avg path length-", nx.average_shortest_path_length(dolphins))
print("avg clustering coefficient-", nx.average_clustering(dolphins))
nx.draw(dolphins,with_labels = True)




sp1 = s.generic.average_shortest_path_length(karate)
sp2 = s.generic.average_shortest_path_length(dolphins)
sp3 = s.generic.average_shortest_path_length(jazz)

avg_clus1 = nxx.average_clustering(karate)
avg_clus2 = nxx.average_clustering(dolphins)
avg_clus3 = nxx.average_clustering(jazz)


data = {'Datasets':['Karate','Dolphins','Jazz'],
       'Nodes':[len(list(karate.nodes())),len(list(dolphins.nodes())), len(list(jazz.nodes()))],
       'Edges':[len(list(karate.edges())),len(list(dolphins.edges())), len(list(jazz.edges()))],
       'Average Path Lengths':[sp1,sp2, sp3],
       'Average Clustering co-efficient': [avg_clus1,avg_clus2, avg_clus3]}

df = pd.DataFrame(data)
df
