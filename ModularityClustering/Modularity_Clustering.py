#!/usr/bin/env python
# coding: utf-8

# In[2]:


import networkx as nx
from BetwenessCluster import Betweness_Clustering as q1
zero=0
one=1
fone=1.0
fzero = 0.0

#Here, we are trying to generate the modularity score which we had found using betweness clustering 
#which applied on "karate" and "dolphins" network.
compList1=[]
graph1 = nx.read_gml('karate.gml', label = 'id')
components1 = q1.gnAlgo(3,graph1)
for scc in components1:
    compList1.append(list(scc.nodes()))
    print(scc.nodes())
adjdict1 = adj_dict_create(graph1)
deg_dict1 = create_degreeTable(adjdict1)
edge_list1 = create_edgeList(graph1)
print("The Modularity score of the above group of communities is : ", modularityScore(compList1,deg_dict1,edge_list1))

compList2=[]
graph2 = nx.read_gml('dolphins.gml', label = 'id')
components2 = q1.gnAlgo(4,graph2)
for scc in components2:
    compList2.append(list(scc.nodes()))
    print(scc.nodes())
adjdict2 = adj_dict_create(graph2)
deg_dict2 = create_degreeTable(adjdict2)
edge_list2 = create_edgeList(graph2)
print("The Modularity score of the above group of communities is : ", modularityScore(compList2,deg_dict2,edge_list2))
#G3 = nx.read_pajek('jazz.net')


#This method will help us converting a graph of GML format to an Adjacency dict
# in which "key" is node label and "value" is a list of nodes to which the key_node connected to.
def adj_dict_create(graph):
    adj_dict1 = {}
    edges = graph.edges()

    #one-way neighbours
    for node in graph.nodes():
        neigh =[]
        for edge in graph.edges():
            if node == edge[0]:
                neigh.append(edge[1])
        adj_dict1[node]=neigh

    #other-way neighbors updation
    reverseEdges = [lsTup[::-1] for lsTup in edges]

    adj_dict2={}
    for node in graph.nodes():
        neigh =[]
        for edge in reverseEdges:
            if node == edge[0]:
                neigh.append(edge[1])
        adj_dict2[node]=neigh

    adj_dict={}
    for node in graph.nodes():
        adj_dict[node] = adj_dict1[node] + adj_dict2[node]
    
    ##call both degree and edge table funcs
    create_degreeTable(adj_dict)
    create_edgeList(graph)
        
    return adj_dict

#degree table, edges per nodes using adj_dict for modularity
def create_degreeTable(adj_dict):
    deg_dict={}
    for node in list(adj_dict.keys()):
        deg_dict[node] = len(adj_dict[node])//2
    return deg_dict

def create_edgeList(graph):
    edge_list= list(graph.edges())
    return edge_list

#This modulairty score function finds out the actual modularity score which basically tries to
#capture the notion of how far the given graph is from a purely random graph which is not close to a real-world scenario
def modularityScore(comps,deg_dict,edge_list):
    modscore = 0.0
    for comp in comps:
        t =0.0
        for u in comp:
            for v in comp:
                edge = tuple(sorted([u,v]))
                if edge in edge_list:
                    Aij = 1.0
                else:
                    Aij = 0.0
                t += (Aij - ((deg_dict[u] * deg_dict[v]) / (2.0 * len(edge_list))))
        modscore+=t
    return modscore / (len(edge_list) * 2.0)


# In[ ]:




