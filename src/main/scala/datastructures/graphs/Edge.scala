package datastructures.graphs

/**
  * Represents an edge of the DAG, has one source node and one destination node
  * @param sourceNode  Source node index
  * @param destination  Destination node index
  */
case class Edge(sourceNode: Int, destination: Int)