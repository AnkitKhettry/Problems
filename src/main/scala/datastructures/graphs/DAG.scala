package datastructures.graphs

import utils.CycleFoundException

import scala.io.Source
import scala.util.Try

/**
  * Represents a (possibly disjointed) directed acyclic graph
  * @param numberOfNodes  Number of nodes in the graph
  * @param edges  Set of edges in the graph
  */
class DAG(numberOfNodes: Int, edges: Set[Edge]){

  /**
    * @return Returns all nodes in the DAG with 0 in-degree.
    */
  def getSourceNodes(): Set[Int] = {

    val nonZeroInDegreeNodes = edges.map(_.destination).toSet

    val zeroInDegreeNodes = (0 until numberOfNodes).filter{
      node => !nonZeroInDegreeNodes.contains(node)
    }.toSet

    zeroInDegreeNodes
  }

  /**
    * Gets the set of all possible paths from a given node.
    * @param node Given node to find all possible paths from.
    * @return Set of all possible paths from the given node.
    */
  def getAllPathsFromNode(node: Int, upstreamNodes : Seq[Int]): Set[Seq[Int]] = {

    val connectedNodes = edges.filter(_.sourceNode == node).map(_.destination)

    val currentPath = upstreamNodes :+ node

    if (upstreamNodes.contains(node)) throw new CycleFoundException(currentPath.mkString(" -> "))

    if (!connectedNodes.isEmpty) {

      connectedNodes.flatMap{
        cnode => getAllPathsFromNode(cnode, currentPath)
      }
    }
    else Set(currentPath)
  }
}

object DAG{

  /**
    * Creates a DAG object out of the given source file.
    * @param inputFilePath
    * @return Corresponding DAG object
    */
  def apply(inputFilePath: String) = {

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

    val edges = lines.tail.map {
      line =>
        val nodesOfTheEdge = line.split(",")
        val edge = Try(Edge(nodesOfTheEdge(0).trim.toInt, nodesOfTheEdge(1).trim.toInt)).getOrElse(throw new Exception(errorMsg))

        edge
    }.toSet

    new DAG(numNodes, edges)
  }
}