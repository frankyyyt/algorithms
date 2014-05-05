class Graph:
  
  def __init__(self):
    self.V = 0 # Number of vertices
    self.E = 0 # Number of edges
    self.adj = [] # List of lists of adjacent nodes

  def add_vertex(self):
    """ Add a vertex """
    pass

  def add_edge(self, vertex1, vertex2):
    """ Connect two vertices """
    pass
  
  def to_string(self):
    """ Represent the graph as a string """
    pass

if __name__ == "__main__":
  my_graph = Graph()
  my_graph.add_vertex()
  my_graph.add_vertex()
  assert my_graph.V == 2
