from Case import case_1, case_2, case_3, case_4, case_5, case_6
import random
from functools import reduce
# Class to represent a graph

class Graph:
  
    def __init__(self, vertices, edges):
        self.V = vertices  # No. of vertices
        self.E = edges # No. of edges
        self.graph = []
  
    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
  
    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))
  
    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
   
    def NegCycleBellmanFord(self, src):
        V = self.V;
        E = self.E;
        # print(f"v : {V}, e : {E}")
        dist =[1000000 for i in range(V)]
        parent =[-1 for i in range(V)]
        dist[src] = 0;
    
        # print(self.graph)
        # Relax all edges |V| - 1 times.
        for i in range(self.V - 1):
            for edge in self.graph:
                
                u = edge[0]['id']
                # print(u)
                v = edge[1]['id']
                # print(v)
                w = edge[2]
                # print(w)
                # print("-------------")
    
                if (dist[u] != 1000000 and dist[u] + w < dist[v]):
                
                    dist[v] = dist[u] + w;
                    parent[v] = u;
    
        # Check for negative-weight cycles
        C = -1;   
        for edge in self.graph:  
            u = edge[0]['id']
            v = edge[1]['id']
            w = edge[2]
    
            if (dist[u] != 1000000 and dist[u] + w < dist[v]):
                
                # Store one of the vertex of
                # the negative weight cycle
                C = v;
                break;
            
        if (C != -1):      
            for i in range(V):      
                C = parent[C];
    
            # To store the cycle vertex
            cycle = []      
            v = C
            
            while (True):
                cycle.append(v)
                if (v == C and len(cycle) > 1):
                    break;
                v = parent[v]
    
            # Reverse cycle[]
            cycle.reverse()
    
            # Printing the negative cycle
            return cycle
        else:
            return None
  

# The main function that finds shortest distances
# from src to all other vertices using Bellman-
# Ford algorithm.  The function also detects

# Driver's code

def arbitrage(input_price):
    case_one = case_1.get_pool()
    case_two = case_2.get_pool()
    case_three = case_3.get_pool()
    case_four = case_4.get_pool()
    case_five = case_5.get_pool()
    case_six = case_6.get_pool()
    
    total_case = [case_one, case_two, case_three, case_four, case_five, case_six]
    src_pool = random.choice(total_case)["pools"]
    # src_pool = case_six
    # print(src_pool)
    amount_of_pool = len(src_pool)
    # print(amount_of_pool)

    V = amount_of_pool
    E = V*(V-1)
    graph = Graph(V, E)
    for src_pair in src_pool:
        token_A = src_pair["src_token"]
        token_B = src_pair["dest_token"]
        
        for dest_pair in src_pool:
            token_C = dest_pair["src_token"]
            token_D = dest_pair["dest_token"]
            # if ((token_A == token_C) or (token_A == token_D)) and ((token_B == token_C) or (token_B == token_D)):
            #     pass
            if token_B == token_C :
                weight = src_pair["ratio"]
                graph.addEdge(src_pair, dest_pair, weight)
    
    # print(len(graph.graph))
    cycle = graph.NegCycleBellmanFord(0)
    
    neg_cycle = []
    price_ratio = []
    if cycle == None:
        return cycle, 0
    else:
        for v in cycle[:-1]:      
            for pool in src_pool:
                if v == pool['id']:
                    neg_cycle.append(pool)
                    price_ratio.append(pool['src_price']/pool['dest_price'])
                    break
    result = reduce(lambda x, y: x * y, price_ratio)
    return neg_cycle, result    