import networkx as netX
import time
import matplotlib.pyplot as plot
import sys

print('Hello!!')
print('Hope you\'ve given the input in the respective input file.')
print('Input for BFS and DFS in input12.txt and MST in input3.txt.')

while True:
  print('Select one of the following:')
  print('1 for BFS')
  print('2 for DFS')
  print('3 for MST')
  print('4 to  Quit')
  x = input()

  if x == '1':
    # 	G,startVertex = CreateGraph()
    # 	position = DrawGraph(G)
    # 	# plot.show()
    # 	BFStraversal (Graph, startVertex, position)
    # 	plot.show()


    def BFStraversal (Graph, startVertex, position): 

      visited = [False] * (len(Graph.nodes()))
      queue = []
      queue.append(startVertex)
      visited [startVertex] = True
      # netX.draw_networkx_nodes(Graph,position,nodelist=Graph[startVertex],node_color='r')

      while queue:
        curNode = queue.pop(0)
        for i in Graph [curNode]:
          # plot.pause(1.5)
          # netX.draw_networkx_nodes(Graph,position,nodelist=Graph[curNode],node_color='r')
          # plot.pause(0.5)
          # netX.draw_networkx_nodes(Graph,position,node_color='b')
          if visited[i] == False:
            queue.append(i)
            visited [i] = True
            plot.pause(1.5)
            # for node in Graph:
            # 	if node == curNode:
            # 		node.append('red')
            # 	else: node.append('green')
            # netX.draw_networkx_nodes(curNode, position, node_size=200, node_color='r')
            # netX.draw_networkx_nodes(Graph,position,nodelist=Graph[0],node_color='r')
            netX.draw_networkx_edges(Graph,position,edgelist=[(curNode,i)],width=3,alpha=1,edge_color='b')
            plot.draw()
      return




    def DrawGraph(Graph):
      position = netX.spring_layout(Graph)
      netX.draw(Graph, position, with_labels = True)
      # edge_labels = dict([((u,v,), d['length']) for u, v, d in Graph.edges(data = True)])
      # netX.draw_networkx_edge_labels(Graph, position, edge_labels = edge_labels, label_position = 0.3, font_size = 11)
      return position


    # 	print('Please give inputs in the input1.txt file. \n First line contains number of vertices. \nThen a n*n matrix, containing 0,1 showing an edge between two vertices. \nThe last line contains the start vertex')
    # 	Graph,startVertex = CreateGraph()
    # 	position = DrawGraph(Graph)
    # 	# plot.show()
    # 	BFStraversal(Graph, startVertex, position)
    # 	plot.show()


    def CreateGraph():
      Graph = netX.Graph()
      f = open('input12.txt')
      n = int(f.readline())
      arr = []
      for i in range(n):
        list1 = list(map(int, (f.readline()).split()))
        arr.append(list1)
      startVertex = int(f.readline())
      
      for i in range(n):
        for j in range(n):
          if arr[i][j] > 0:
              Graph.add_edge(i, j) 
      return Graph, startVertex



    # print('Please give inputs in the input12.txt file. \nFirst line contains number of vertices. \nThen a n*n matrix, containing 0,1 showing an edge between two vertices. \nThe last line contains the start vertex')
    Graph, startVertex = CreateGraph()
    position = DrawGraph(Graph)
    # print(type(position))
    # print(type(Graph))
    # plot.show()
    BFStraversal(Graph, startVertex, position)
    plot.show()

  if x == '2':
    def DFSutility(Graph, v, visited, sl):
        visited[v] = True
        sl.append(v)
        for i in Graph[v]:
            if visited[i] == False:
                DFSutility(Graph, i, visited, sl)
        return sl


    def DFS(Graph, startVertex):
        visited = [False] * (len(Graph.nodes()))
        sl = []
        stack = []
        stack.append(DFSutility(Graph, startVertex, visited, sl))
        for i in range(len(Graph.nodes())):
            if visited[i] == False:
              sl = []
              stack.append(DFSutility(Graph, i, visited, sl))
        return stack


    def CreateGraph1():
        Graph = netX.Graph()
        f = open('input12.txt')
        n = int(f.readline())
        arr = []
        for i in range(n):
            list1 = list(map(int, (f.readline()).split()))
            arr.append(list1)
        startVertex = int(f.readline())

        for i in range(n):
            for j in range(n):
                if arr[i][j] > 0:
                    Graph.add_edge(i, j)
        return Graph, startVertex


    def DrawPath(Graph, stack):
      position = netX.spring_layout(Graph)
      netX.draw(Graph, position, with_labels = True)
      # edge_labels = dict([((u,v,), d['length']) for u, v, d in Graph.edges(data = True)])
      # netX.draw_networkx_edge_labels(Graph, position, edge_labels = edge_labels, label_pos = 0.3, font_size = 11)
      plot.pause(1.5)
      for i in stack:
        if len(i) > 1:
          for j in i[ :(len(i)-1)]:
            if i[i.index(j)+1] in Graph[j]:
              netX.draw_networkx_edges(Graph, position, edgelist = [(j,i[i.index(j)+1])], width = 3, alpha = 1, edge_color = 'b')
              plot.pause(1.5)
            else:
              for k in i[1::-1]: 
                if k in Graph[j]:
                  netX.draw_networkx_edges(Graph, position, edgelist = [(j,k)], width = 3, alpha = 1, edge_color = 'b')
                  plot.pause(1.5)
                  break


    # print('Please give inputs in the input12.txt file. \nFirst line contains number of vertices. \nThen a n*n matrix, containing 0,1 showing an edge between two vertices. \nThe last line contains the start vertex')
    Graph, startVertex = CreateGraph1()
    stack = DFS(Graph, startVertex)
    DrawPath(Graph, stack)
    plot.show()
  
  if x == '3':
    def minDistance(distance, MST, V):
      min = sys.maxsize
      for v in range(V):
        if MST[v] == False and distance[v] < min:
          min = distance[v]
          min_index = v
      return min_index



    def prims(Graph, position):
      V = len(Graph.nodes())
      distance = []
      parent = [None]*V
      MST = []

      for i in range(V):
        distance.append(sys.maxsize)
        MST.append(False)
      distance[0] = 0
      parent[0]= -1
      for count in range(V-1):
        u = minDistance(distance, MST, V)
        MST[u] = True
        for v in range(V):
          if (u, v) in Graph.edges():
            if MST[v] == False and Graph[u][v]['length'] < distance[v]:
              distance[v] = Graph[u][v]['length']
              parent[v] = u
      for X in range(V):
        if parent[X] != -1:
          if (parent[X], X) in Graph.edges():
            plot.pause(1.5)
            netX.draw_networkx_edges(Graph, position, edgelist = [(parent[X], X)], width = 3, alpha = 1, edge_color = 'b')
            plot.draw()
      return



    def CreateGraph2():
      Graph = netX.Graph()
      f = open('input3.txt')
      n = int(f.readline())
      arr = []
      for i in range(n):
        list1 = list(map(int, (f.readline()).split()))
        arr.append(list1)

      for i in range(n) :
        for j in range(n)[i:] :
          if arr[i][j] > 0 :
              Graph.add_edge(i, j, length = arr[i][j]) 
      return Graph



    def DrawGraph2(Graph):
      position = netX.spring_layout(Graph)
      netX.draw(Graph, position, with_labels = True)
      edge_labels = netX.get_edge_attributes(Graph,'length')
      netX.draw_networkx_edge_labels(Graph, position, edge_labels = edge_labels, font_size =24)
      return position



    Graph = CreateGraph2()
    position = DrawGraph2(Graph)
    prims(Graph, position)
    plot.show()
  
  if x == '4':
    print('Thank You!!')
    break