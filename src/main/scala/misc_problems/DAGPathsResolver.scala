package misc_problems

import scala.io.Source
import scala.util.Try

object DAGPathsResolver {

  /**
    * Takes as argument the path of the input file, prints all the possible paths originating from the 0 in-degree nodes.
    * @param args
    */
  def main(args: Array[String]): Unit = {

    val sourceFilePath = args.headOption.getOrElse(
      throw new Exception("""
          |Usage: DAGPathsResolver <input_file_path>
        """.stripMargin))

    val allPossiblePathsInDAG = run(sourceFilePath)
    allPossiblePathsInDAG.foreach(println)
  }

  /**
    *
    * @param sourceFilePath path of input file
    * @return Required set of all possible paths in the DAG
    */
  def run(sourceFilePath: String): Set[String] = {

    val dagObject = generateDAGFromSourceFile(sourceFilePath)
    val sourceNodes = dagObject.getSourceNodes()
    sourceNodes.flatMap(dagObject.getAllPathsFromNode(_))
  }

  /**
    * Creates a DAG out of the given source file.
    * @param inputFilePath
    * @return Corresponding DAG
    */
  def generateDAGFromSourceFile(inputFilePath: String): DAG = {

    val lines = Source.fromFile(inputFilePath).getLines().toList

    val errorMsg =
      """
        |Failed to parse input file.
        |Expected format:
        |
        |<number of nodes in the DAG>
        |<Source node index of first edge> , <Destination node index of first edge>
        |<Source node index of second edge> , <Destination node index of second edge>
        |.
        |.
        |<Source node index of last edge> , <Destination node index of last edge>
      """.stripMargin

    val numNodes = Try(lines.head.toInt).getOrElse(throw new Exception(errorMsg))

    val edges = lines.tail.map{
      line =>
        val nodesOfTheEdge = line.split(",")
        val edge = Try(Edge(nodesOfTheEdge(0).trim.toInt, nodesOfTheEdge(1).trim.toInt)).getOrElse(throw new Exception(errorMsg))

        edge
    }.toSet

    DAG(numNodes, edges)
  }

  /**
    * Represents a (possibly disjointed) direct acyclic graph
    * @param numberOfNodes  Number of nodes in the graph
    * @param edges  Set of edges in the graph
    */
  case class DAG(numberOfNodes: Int, edges: Set[Edge]){

    /**
      * @return Returns all node of the DAG with 0 in-degree.
      */
    def getSourceNodes(): Set[Int] = {

      //set of nodes with atleast one incoming edge
      val setOfDestinationNodes = edges.map(_.destination)

      (0 until numberOfNodes)
        .filter( !setOfDestinationNodes.contains(_) )
        .toSet
    }


    /**
      *
      * @param node Given node to find all possible paths from.
      * @return Set of all possible paths from the given node.
      */
    def getAllPathsFromNode(node: Int): Set[String] = {

      //getting all nodes immediately reachable from current node
      val connectedNodes = edges.filter(_.sourceNode == node).map(_.destination)

      //getting all possible paths from given node
      val pathsFromEdge = connectedNodes.flatMap(getAllPathsFromNode(_))

      if (pathsFromEdge.size==0)
        return Set(node.toString)
      else
        return pathsFromEdge.map(node + " -> " + _)
    }
  }

  /**
    * Represents an edge of the DAG, has one source node and one destination node
    * @param sourceNode  Source node index
    * @param destination  Destination node index
    */
  case class Edge(sourceNode: Int, destination: Int)
}
