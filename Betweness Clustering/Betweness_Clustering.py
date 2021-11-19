#!/usr/bin/env python
# coding: utf-8

# In[19]:


import networkx as nx
zero=0
one=1
fone=1.0
fzero = 0.0

#we are considering the karate.gml file
graph1 = nx.read_gml('karate.gml', label = 'id')
#Here we have built the algorithm in such a way that, the user can give a value for the number of communities he wants to see
#accordingly the algorithm tries to converge the communities number.

#In this code, we tried to form 3 communities in "karate" network and 4 communities in "dolphins" network.

#gnAlgo refers to the girvan-newman algorithm
components1 = gnAlgo(3,graph1)
print("These are the three possibile communities in karate network")
for scc in components1:
    print(scc.nodes())
    
graph2 = nx.read_gml('dolphins.gml', label = 'id')
components2 = gnAlgo(4,graph2)
print("These are the four possible communities in dolphins network")
for scc in components2:
    print(scc.nodes())


#we will to see first how many connected components are there inside the given network,
#accordingly we take each avialable components and does find the edge with high betwenes value
#with the help of using BFS aided girvan newman algorithm till we reach requried no.of components

def gnAlgo(k,graph):
    flag=0
    cc = nx.connected_components(graph)
    S = [graph.subgraph(set_of_nodes).copy() for set_of_nodes in cc]
    no_of_cc = len(S)
    
    if no_of_cc >=k:
        return S
    else:
        while flag==0:
            T = []
            for comp in list(S):
                if len(list(comp.edges()))>0:
                    #Task1 is to find the edge with highest betweness value
                    u,v = find_edgeBetweness(comp)
                    comp.remove_edge(u,v)
                    t = [comp.subgraph(set_of_nodes).copy() for set_of_nodes in nx.connected_components(comp)]
                    for each_comp in t:
                        T.append(each_comp)
                else:
                    T.append(comp)
                #for i in T:
                    #print(i.nodes())
                no_of_cc = no_of_cc + len(list(nx.connected_components(comp))) - 1
                #print("connected-comp",no_of_cc)
                if no_of_cc >= k:
                    flag=1
                    break
            S = T
            #print(S)
    return S


#This method helps us in finding our required edge which we remove from the graph 
#and see if any more components got added into the list of available components

#it uses bfs search from a start node and find the number of shortest paths available from that node 
# and followed with the flow values of each edge in the number
def find_edgeBetweness(graph):
    
    edge_betweness={}
    
    for edge in graph.edges():
        betw_key = str(edge[0])+"-"+str(edge[1])
        edge_betweness[betw_key]= zero
    
    adj_dict = adj_dict_create(graph)
    #print(adj_dict)
    for start in list(adj_dict.keys()):
        x = bfs(start,adj_dict)
        y = short_paths(x,adj_dict)
        flow_values(y,x,adj_dict,edge_betweness)
    
    for z in list(edge_betweness.keys()):
        edge_betweness[z] = edge_betweness[z]//2
    
    #print(edge_betweness)
    edgeBetw = max(edge_betweness, key = lambda x: edge_betweness[x])
    edgeBetw = edgeBetw.split('-')
    
    return int(edgeBetw[0]),int(edgeBetw[1])




def bfs(start,adj_dict):
    visited=[start]
    ilevel = zero
    present_level_list=[start]
    levels_nodes_bfs_dict={}
    
    while len(present_level_list)!=zero:
        levels_nodes_bfs_dict[ilevel]=present_level_list
        ilevel+=one
        nxt_level_list=[]
        for node in present_level_list:
            present_neigh=adj_dict[node]
            for neigh in present_neigh:
                if neigh not in visited:
                    visited.append(neigh)
                    nxt_level_list.append(neigh)
        present_level_list = nxt_level_list
    
    return levels_nodes_bfs_dict  



#This method will aid us in finding out available shortest paths from a given node.
def short_paths(levels_nodes_bfs_dict,adj_dict):
    vert_weighs={}
    bf_lev = len(levels_nodes_bfs_dict)
    #print(bf_lev)
    for start_nodes in levels_nodes_bfs_dict[zero]:
        vert_weighs[start_nodes]= fone
    
    for present_level in range(1,bf_lev):
        prev_nodes = set(levels_nodes_bfs_dict[present_level-1])
        #print(prev_nodes)
        present_nodes = set(levels_nodes_bfs_dict[present_level])
        #print(present_nodes)
        for node in present_nodes:
            neigh = set(adj_dict[node])
            #parent_ver = prev_nodes.intersection(neigh)
            parent_vertices = prev_nodes & neigh
            x = fzero
            for y in parent_vertices:
                x = x + vert_weighs[y]
            vert_weighs[node] = x
    
    return vert_weighs



#once we know the shortest path values from the node to all other nodes, we do travel in reverse order of bfs traversal
#and does find the flow_values of each edge,which depends on the number of shortest paths which we calculated.
def flow_values(vert_weighs,levels_nodes_bfs_dict,adj_dict,edge_betweness):
    vert_vals = {}
    bf_lev = len(levels_nodes_bfs_dict)
    for end_node in levels_nodes_bfs_dict[bf_lev - one]:
        vert_vals[end_node] = one

    for present_level in range(bf_lev - 2, -1, -1):
        present_nodes = set(levels_nodes_bfs_dict[present_level])
        next_nodes = set(levels_nodes_bfs_dict[present_level + one])
        for node in present_nodes:
            neigh = set(adj_dict[node])
            #child_vertices = next_nodes.intersection(neigh)
            child_vertices = next_nodes & neigh
            if present_level != zero:
                x = fone
            else:
                x = fzero
            for y in child_vertices:
                value = (vert_vals[y]/vert_weighs[y])* vert_weighs[node]
                #flow_weights_sort_key = tuple(sorted([node, y]))
                #flow_weights[flow_weights_sort_key] = value
                
                #summing up of all edge betweness values in one go
                betw_key = str(node)+"-"+str(y)
                reverse_key = str(y)+"-"+str(node)
                betweness_keys = list(edge_betweness.keys())
                if betw_key not in betweness_keys:
                    edge_betweness[reverse_key]=edge_betweness[reverse_key]+value
                else:
                    edge_betweness[betw_key] = edge_betweness[betw_key] + value
                x += value
            vert_vals[node] = x
            

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
        
    return adj_dict


# In[ ]:




