import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import igraph
import networkx as nx
import numpy as np
import timeit


print("Karate Network")
karate = igraph.read("karate.gml")
kstart = timeit.default_timer()
#convert igraph to networkx format
k_edges = karate.get_edgelist()
K = nx.Graph(k_edges)
print(nx.info(K))

#Adjacency Matrix
adjK = nx.adjacency_matrix(K)
print(adjK.todense())

#Degree Matrix
degK = np.diag(np.sum(np.array(adjK.todense()), axis=1))
print("Degree Matrix:")
print(degK)

#Laplacian Matrix
lapK = degK - adjK
print("Laplacian Matrix")
print(lapK)

#Eigen Value and Eigen Vector
eValK, eVecK = np.linalg.eig(lapK)
#sorting eigen values and eigen vectors by eigen values
eVecK = eVecK[:, np.argsort(eValK)]
eValK = eValK[np.argsort(eValK)]
print("Eigen Values")
print(eValK)
print("Eigen Vectors")
print(eVecK)

#no of clusters obtained using best cut found by Fiddler's method
kClusters = eVecK[:, 1] > 0

#Finding the nodes in each community

c = np.array(kClusters)
commK = c.tolist()
print(commK)
L1 = []
L2 = []
for label, vert in enumerate(commK):
    elements = vert[0]
    print(label, elements)
    
for label, vert in enumerate(commK):
    if vert[0]:
        L1.append(label)
    else:
        L2.append(label)
print("Cluster1 Nodes:")
print(L1)
print("Cluster2 Nodes:")
print(L2)

kstop = timeit.default_timer()
print("----------------------------------------------------------------------------------------")


print("Dolphins Social Network")
dolphins = igraph.read("dolphins.gml")
dstart = timeit.default_timer()
#convert igraph to networkx format
d_edges = dolphins.get_edgelist()
D = nx.Graph(d_edges)
print(nx.info(D))

#Adjacency Matrix
adjD = nx.adjacency_matrix(D)
print(adjD.todense())

#Degree Matrix
degD = np.diag(np.sum(np.array(adjD.todense()), axis=1))
print("Degree Matrix:")
print(degD)

#Laplacian Matrix
lapD = degD - adjD
print("Laplacian Matrix")
print(lapD)

#Eigen Value and Eigen Vector
eValD, eVecD = np.linalg.eig(lapD)
#sorting eigen values and eigen vectors by eigen values
eVecD = eVecD[:, np.argsort(eValD)]
eValD = eValD[np.argsort(eValD)]
print("Eigen Values")
print(eValD)
print("Eigen Vectors")
print(eVecD)

#no of clusters obtained using best cut found by Fiddler's method
dClusters = eVecD[:, 1] > 0

#Finding the nodes in each community

c = np.array(dClusters)
commD = c.tolist()
print(commD)
L1 = []
L2 = []
for label, vert in enumerate(commD):
    elements = vert[0]
    print(label, elements)
    
for label, vert in enumerate(commD):
    if vert[0]:
        L1.append(label)
    else:
        L2.append(label)
print("Cluster1 Nodes:")
print(L1)
print("Cluster2 Nodes:")
print(L2)
dstop = timeit.default_timer()
print("----------------------------------------------------------------------------------------")

print("Jazz Musicians Network")
jazz = igraph.read("jazz.net")
jstart = timeit.default_timer()
#convert igraph to networkx format
j_edges = jazz.get_edgelist()
J = nx.Graph(j_edges)
print(nx.info(J))

#Adjacency Matrix
adjJ = nx.adjacency_matrix(J)
print(adjJ.todense())

#Degree Matrix
degJ = np.diag(np.sum(np.array(adjJ.todense()), axis=1))
print("Degree Matrix:")
print(degJ)

#Laplacian Matrix
lapJ = degJ - adjJ
print("Laplacian Matrix")
print(lapJ)

#Eigen Value and Eigen Vector
eValJ, eVecJ = np.linalg.eig(lapJ)
#sorting eigen values and eigen vectors by eigen values
eVecJ = eVecJ[:, np.argsort(eValJ)]
eValJ = eValJ[np.argsort(eValJ)]
print("Eigen Values")
print(eValJ)
print("Eigen Vectors")
print(eVecJ)

#no of clusters obtained using best cut found by Fiddler's method
jClusters = eVecJ[:, 1] > 0

#Finding the nodes in each community

c = np.array(jClusters)
commJ = c.tolist()
print(commJ)
L1 = []
L2 = []
for label, vert in enumerate(commJ):
    elements = vert[0]
    print(label, elements)
    
for label, vert in enumerate(commJ):
    if vert[0]:
        L1.append(label)
    else:
        L2.append(label)
print("Cluster1 Nodes:")
print(L1)
print("Cluster2 Nodes:")
print(L2)

jstop = timeit.default_timer()

print("__________________________________________________________________________________")
print("Runtime for Karate", 1000*(kstop-kstart), "ms")
print("Runtime for Jazz", 1000*(jstop-jstart), "ms")
print("Runtime for Dolphins", 1000*(dstop-dstart), "ms")
