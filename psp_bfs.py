import networkx as netX
import time
import matplotlib.pyplot as plot
 

# 	G,startVertex = CreateGraph()
# 	position = DrawGraph(G)
# 	# plot.show()
# 	bfs_traversal (Graph, startVertex, position)
# 	plot.show()


def bfs_traversal (Graph, startVertex, position): 

	visited = [False] * (len(Graph.nodes()))
	queue = []
	queue.append(startVertex)
	visited [startVertex] = True

	while queue:
		curNode = queue.pop(0)
		for i in Graph [curNode]:
			if visited[i] == False:
				queue.append(i)
				visited [i] = True
				plot.pause(1.5)
				# for node in Graph:
				# 	if node == curNode:
				# 		node.append('red')
				# 	else: node.append('green')
				# netX.draw_networkx_nodes(curNode, position, node_size=200, node_color='r')
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
# 	bfs_traversal(Graph, startVertex, position)
# 	plot.show()


def CreateGraph():
	Graph = netX.Graph()
	f = open('input1.txt')
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



print('Please give inputs in the input1.txt file. \nFirst line contains number of vertices. \nThen a n*n matrix, containing 0,1 showing an edge between two vertices. \nThe last line contains the start vertex')
Graph, startVertex = CreateGraph()
position = DrawGraph(Graph)
# plot.show()
bfs_traversal(Graph, startVertex, position)
plot.show()