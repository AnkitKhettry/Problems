package datastructures.graphs

object DAGPathsResolver {

  /**
    * Takes as argument the path of the input file, prints all the possible paths originating from the 0 in-degree nodes.
    * Nodes are identified by their indices.
    * @param args
    */
  def main(args: Array[String]): Unit = {

    val sourceFilePath1 = "src/main/resources/input_files/sample_DAG.txt"
    val sourceFilePath2 = "src/main/resources/input_files/sample_DAG_with_cycle.txt"

    val allPossiblePathsInDAG1 = run(sourceFilePath1)
    println("First graph: ")
    allPossiblePathsInDAG1.foreach(println)

    println("-----------------------------------")

    val allPossiblePathsInDAG2 = run(sourceFilePath2)
    println("Second graph: ")
    allPossiblePathsInDAG2.foreach(println)
  }

  /**
    *
    * @param sourceFilePath path of input file
    * @return Required set of all possible paths in the DAG
    */
  def run(sourceFilePath: String): Set[String] = {

    val dagObject = DAG(sourceFilePath)
    val sourceNodes = dagObject.getSourceNodes()  //all nodes with 0 in-degree
    val paths = sourceNodes.flatMap(dagObject.getAllPathsFromNode( _ , Seq() ) )

    paths.map{
      seq => seq.mkString(" -> ")
    }
  }

}
