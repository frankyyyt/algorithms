class Graph:
  
  def __init__(self):
    self.V = 0 # Number of vertices
    self.E = 0 # Number of edges
    self.adj = [] # List of lists of adjacent nodes

  def add_vertex(self):
    """ Add a vertex """
    new_vertex = []
    self.adj.append(new_vertex)
    self.V += 1

  def add_edge(self, vertex1, vertex2):
    """ Connect two vertices """
    self.adj[vertex1].append(vertex2)
    self.E += 1 

  def to_string(self):
    """ Represent the graph as a string """
    graph_string = ""
    for k, node in enumerate(self.adj):
      graph_string += "[" + str(k) +"]"
      for inner_node in node:
         graph_string += "-"
    return graph_string

if __name__ == "__main__":
  my_graph = Graph()
  my_graph.add_vertex()
  my_graph.add_vertex()
  assert my_graph.V == 2
  print my_graph.to_string()
  assert my_graph.to_string() == "[0][1]"
  print my_graph.to_string()
  my_graph.add_edge(0, 1)
  assert my_graph.E == 1
  print my_graph.to_string()
  assert my_graph.to_string() == "[0]-[1]"
  my_graph.add_vertex()
  print my_graph.to_string()
  my_graph.add_edge(1, 2)
  assert my_graph.E == 2
  print my_graph.to_string()
  assert my_graph.to_string() == "[0]-[1]-[2]"

  my_graph_2 = Graph()
  my_graph_2.add_vertex()
  my_graph_2.add_vertex()
  my_graph_2.add_vertex()
  my_graph_2.add_edge(0, 2)
  print my_graph_2.to_string()
  assert my_graph_2.to_string() == "[0]-[2][1]"
