import networkx as nx
import random as rand
from utils import *

class Person(object):
    #static variable
    population = 0
    def __init__(self,id_num=-1,ideo=-1):
        self.id_num = id_num if id_num!=1 else Person.population
        Person.population += 1
        self.ideo = ideo if ideo!=-1 else rand.random()
    def __eq__(self,other):
        return self.id_num==other.id_num
    def __hash__(self):
        return hash(self.id_num)

def clamp(x,lo,hi):
    return lo if x<lo else \
           hi if x>hi else x

def update_friendships(graph, node, sigma):
    for nbr in graph.adj[node]:
        graph.adj[node][neighbor]['weight']+=rand.gauss(0,sigma)

def step_rand_walk(graph, node):
    #print(node)
    sum_weights = sum([graph.adj[node][neighbor]['weight'] for neighbor in graph.adj[node]])
    li = [(neighbor, graph.adj[node][neighbor]['weight']/sum_weights) for neighbor in graph.adj[node]]
    #print(li)
    x = sample_wp(li)
    #print("hi",x)
    return x

def test():
    G = nx.Graph()
    G.add_nodes_from([1,2,3,4,5,6])
    G.add_edges_from([(1,2,{'weight':1.0}),
                      (1,3,{'weight':2.0}),
                      (2,4,{'weight':10.0}),
                      (3,5,{'weight':10.0}),
                      (3,6,{'weight':20.0})])
    #print(G.adj)
    for t in range(15):
        print(step_rand_walk(G,step_rand_walk(G,1)))
    p=Person()
    q=Person()
    print(Person.population)
    
if __name__=='__main__':
    test()
